import re
from collections import Counter
from dateutil.parser import parse
import calendar


def filter_by_year(texts, year):
    if year is not None:
        return [text for text in texts if parse(text.date).year == year]
    else:
        return texts


def get_top_months(senders, n, year=None):
    month_counts = Counter()

    for sender in senders.values():
        texts = filter_by_year(sender.texts, year)
        for text in texts:
            date = parse(text.date)
            month_counts[date.month] += 1

    return month_counts.most_common(n)


def get_top_senders(senders, n, year=None):
    total_messages_per_sender = Counter()

    for sender_name, sender in senders.items():
        texts = filter_by_year(sender.texts, year)
        total_messages_per_sender[sender_name] += len(texts)

    return total_messages_per_sender.most_common(n)


def get_top_emojis(senders, n, year=None):
    all_emojis = [emoji for sender in senders.values()
                  for text in filter_by_year(sender.texts, year)
                  for emoji in text.emojis]
    all_emojis_counter = Counter(all_emojis)
    return all_emojis_counter.most_common(n)


def get_top_sender_emojis(sender, n, year=None):
    all_emojis = [emoji
                  for text in filter_by_year(sender.texts, year)
                  for emoji in text.emojis]
    all_emojis_counter = Counter(all_emojis)
    return all_emojis_counter.most_common(n)


"""
def get_top_emojis(senders, n, sender_name=None, year=None):
    if sender_name is not None:
        sender = senders[sender_name]
        texts = filter_by_year(sender.texts, year)

        emoji_counter = Counter(
            [emoji for text in texts for emoji in text.emojis])
        return emoji_counter.most_common(n)
    else:
        all_emojis = [emoji for sender in senders.values()
                      for text in filter_by_year(sender.texts, year)
                      for emoji in text.emojis]
        all_emojis_counter = Counter(all_emojis)
        return all_emojis_counter.most_common(n)
"""


def get_top_words(senders, n, sender_name=None, year=None):
    word_pattern = re.compile(r'\b\w+\b')
    words_counter = Counter()

    for sender_name, sender in senders.items():
        if sender_name is not None and sender_name != sender.name:
            continue

        texts = filter_by_year(sender.texts, year)
        for text in texts:
            for word in word_pattern.findall(text.message):
                words_counter[word] += 1

    return words_counter.most_common(n)


def get_yearly_wrapped_stats(senders, n, year=None):

    print("\nAll-Time: Top 5")
    print("\nMost used emojis")
    for emoji, count in get_top_emojis(senders, n, None):
        print(f"\t{emoji}: {count}")

    print(f"Top Senders:")
    for sender, count in get_top_senders(senders, n, None):
        print(f"\t{sender}: {count} messages")

    print(f"Most active months:")
    for month, count in get_top_months(senders, n, None):
        print(f"\t{calendar.month_abbr[month]}: {count} messages")

    print(f"\nYEAR {year}: Top 5")
    print("Most used emojis:")
    for emoji, count in get_top_emojis(senders, n, year):
        print(f"\t{emoji}: {count}")

    print(f"Top Senders:")
    for sender, count in get_top_senders(senders, n, year):
        print(f"\t{sender}: {count} messages")

    print("Most active months:")
    for month, count in get_top_months(senders, n, year):
        print(f"\t{calendar.month_abbr[month]}: {count} messages")

    print("Individual Emoji Preference:")
    for sender_key, sender in senders.items():
        print(sender_key)
        for emoji, count in get_top_sender_emojis(sender, n, year):
            print(f"\t{emoji}: {count}")
