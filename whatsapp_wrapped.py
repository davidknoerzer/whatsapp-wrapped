import pandas, emoji


def remove_skin_tones(text):
    text = emoji.demojize(text)
    skin_tones = [
        "_dark_skin_tone",
        "_light_skin_tone",
        "_medium-dark_skin_tone",
        "_medium-light_skin_tone",
        "_medium_skin_tone",
    ]

    for tone in skin_tones:
        text = text.replace(tone, "")

    text = emoji.emojize(text)
    return text


def rank_emoji_distinct(df, year, n):
    df_year = df[df["date"].str.contains(year)]

    emojis = []

    for text in df_year["text"]:
        text = remove_skin_tones(text)

        emojis += emoji.distinct_emoji_list(text)

    emoji_rank = pandas.Series(emojis).value_counts().head(n)
    return emoji_rank


def rank_names_by_messages(df, year, n):
    df_year = df[df["date"].str.contains(year)]

    name_rank = df_year["name"].value_counts().head(n)

    return name_rank


def rank_months_by_messages(df, year, n):
    df_year = df[df["date"].str.contains(year)]

    df_year["month"] = pandas.to_datetime(df_year["date"], format="%d.%m.%Y").dt.month

    month_rank = df_year["month"].value_counts().head(n)

    return month_rank
