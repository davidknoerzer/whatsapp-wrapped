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

    return emoji.emojize(text)


def rank_emoji_distinct(df: pandas.DataFrame, n):
    emojis = []

    for text in df["wa_text"]:
        text = remove_skin_tones(text)

        emojis += emoji.distinct_emoji_list(text)

    return pandas.DataFrame(emojis).value_counts().head(n)


def rank_names_by_messages(df: pandas.DataFrame, n):
    return df["wa_name"].value_counts().head(n)


def rank_months_by_messages(df: pandas.DataFrame, n):
    df["month"] = df.loc[:, "wa_datetime"]
    
    return df["month"].dt.month.value_counts().head(n)
