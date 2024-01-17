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


def rank_emoji_distinct(df, n):
    emojis = []

    for text in df["wa_text"]:
        text = remove_skin_tones(text)

        emojis += emoji.distinct_emoji_list(text)

    emoji_rank = pandas.Series(emojis).value_counts().head(n)
    return emoji_rank


def rank_names_by_messages(df, n):
    name_rank = df["wa_name"].value_counts().head(n)

    return name_rank


def rank_months_by_messages(df, n):
    df["month"] = df.loc[:, "wa_datetime"]

    print(df["month"].dt.month)

    month_rank = df["month"].dt.month.value_counts().head(n)

    return month_rank
