import re
from collections import Counter
from datetime import datetime
from sender import Sender
from text import Text

def get_top_months(senders, n, year=None):
    month_counts = Counter()

    for sender_name, sender in senders.items():
        if year is not None:
            texts = sender.get_texts_by_year(year)
        else:
            texts = sender.texts
        for text in texts:
            date = datetime.strptime(text.date, '%d.%m.%y')
            month_counts[date.month] += 1

    return month_counts.most_common(n)

def get_top_senders(senders, n, year=None):
    total_messages_per_sender = Counter()

    for sender_name, sender in senders.items():
        if year is not None:
            texts = sender.get_texts_by_year(year)
            for text in texts:
                if text.date.split('.')[2] == year:
                    total_messages_per_sender[sender_name] += 1
        else:
            texts = sender.texts
            for text in texts:
                total_messages_per_sender[sender_name] += 1     

    return total_messages_per_sender.most_common(n)
    
def get_top_emojis(senders, n, sender_name=None, year=None):
    if sender_name is not None:
        sender = senders[sender_name]
        if year is not None:
            texts = sender.get_texts_by_year(year)
        else:
            texts = sender.texts
        
        emoji_counter = Counter([emoji for text in texts for emoji in text.emojis])
        return emoji_counter.most_common(n)
    else:
        all_emojis = [emoji for sender in senders.values() for text in sender.texts for emoji in text.emojis]
        all_emojis_counter = Counter(all_emojis)
        return all_emojis_counter.most_common(n)


def get_top_words(senders, n, sender_name=None, year=None):
    word_pattern = re.compile(r'\b\w+\b')
    words_counter = Counter()

    for sender_name, sender in senders.items():
        if sender_name is not None and sender_name != sender.name:
            continue
        
        if year is not None:
            texts = sender.get_texts_by_year(year)
        else:
            texts = sender.texts
        
        for text in texts:
            for word in word_pattern.findall(text.message):
                words_counter[word] += 1

    return words_counter.most_common(n)


def get_yearly_wrapped_stats(senders, n, year=None):

    print(f"\n{file}")

    print("\nAll-Time: Most used emojis")
    for emoji, count in get_top_emojis(senders, n, None, None):
        print(f"\t{emoji}: {count}")

    print(f"All-Time: Top Senders:")
    for sender, count in get_top_senders(senders, n, None):
        print(f"\t{sender}: {count} messages")

    print(f"All-Time: Most active months:")
    for month, count in get_top_months(senders, n, None):
        print(f"\t{month}: {count} messages")

    print(f"\nYEAR {year} STATS")
    print("Most used emojis:")
    for emoji, count in get_top_emojis(senders, n, None, "22"):
        print(f"\t{emoji}: {count}")

    print(f"Top Senders:")
    for sender, count in get_top_senders(senders, n, "22"):
        print(f"\t{sender}: {count} messages")

    print("Most active months:")
    for month, count in get_top_months(senders, n, "22"):
        print(f"\t{month}: {count} messages")

    print("Individual Emoji Preference:")
    for sender_name, sender in senders.items():
        print(f"{sender.name}")
        if year is not None:
            texts = sender.get_texts_by_year(year)
        else:
            texts = sender.texts
        for emoji, count in get_top_emojis(senders, n, sender.name, "22"):
            print(f"\t{emoji}: {count}")

file = 'data/chat_blud-bruda.txt'
#file = 'data/chat_luca-renz.txt'
#file = 'data/chat_ohana.txt'
#file = 'data/chat_philipp-yanni.txt'
#file = 'data/chat_sugus-rangers.txt'

with open(file, 'r') as f:
    text = f.read()

regex = re.compile(r'\[(?P<date>\d{2}.\d{2}.\d{2}), (?P<time>\d{2}:\d{2}:\d{2})] (?P<sender>.+?): (?P<message>.+)')

senders = {}

for line in text.split('\n'):
    match = regex.search(line)
    
    if match:
        sender_name = match.group('sender')
        date = match.group('date')
        time = match.group('time')
        message = match.group('message')
        
        text = Text(date, time, message)
        
        if sender_name not in senders:
            senders[sender_name] = Sender(sender_name)
        
        senders[sender_name].add_text(text)


get_yearly_wrapped_stats(senders, 5, "22")