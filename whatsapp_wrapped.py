import pandas as pd, emoji

def remove_skin_tones(text):
    text = emoji.demojize(text)
    skin_tones = ['_dark_skin_tone', '_light_skin_tone', '_medium-dark_skin_tone', '_medium-light_skin_tone', '_medium_skin_tone']

    for tone in skin_tones:
        text = text.replace(tone, '')

    text = emoji.emojize(text)
    return(text)

def distinct_emoji_count(df, year, n):
    df_year = df[df['date'].str.contains(year)]
    
    emojis = []
    
    for text in df_year['text']:
        text = remove_skin_tones(text)
        
        emojis += emoji.distinct_emoji_list(text)

    distinct_emoji_count = pd.Series(emojis).value_counts().head(n)
    return(distinct_emoji_count)

def rank_names_by_messages(df, year, n):
    df_year = df[df['date'].str.contains(year)]
    
    name_counts = df_year['name'].value_counts().head(n)
    
    return name_counts

def find_favorite_emojis(df, year, n):

    df_year = df[df['date'].str.contains(year)]
    
    emojis = []
    
    for text in df_year['text']:
         
       text = remove_skin_tones(text)

       pre_emojis = []
       pre_emojis += emoji.emoji_list(text)
       if(pre_emojis):
           for i in pre_emojis:
                emojis += i['emoji']
       continue

            
    emoji_counts = pd.Series(emojis).value_counts().head(n)
    
    return emoji_counts

def find_months_with_most_texts(df, year, n):
    df_year = df[df['date'].str.contains(year)]
    
    df_year['month'] = pd.to_datetime(df_year['date'], format="%d.%m.%Y").dt.month

    month_counts = df_year['month'].value_counts().head(n)
    
    return month_counts

def get_yearly_wrapped(df, year, n):

    distinct_emoji_counts = distinct_emoji_count(df, year, n+5)
    print(distinct_emoji_counts)

    name_counts = rank_names_by_messages(df, year, n)
    print(name_counts)

    emoji_counts = find_favorite_emojis(df, year, n)
    print(emoji_counts)

    month_counts = find_months_with_most_texts(df, year, n)
    print(month_counts)
