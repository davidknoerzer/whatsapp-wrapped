from collections import Counter


class Sender:
    def __init__(self, name):
        self.name = name
        self.texts = []
        self.texts_by_year = {}

    def add_text(self, text):
        self.texts.append(text)
        year = text.date[-2:]
        if year not in self.texts_by_year:
            self.texts_by_year[year] = [text]
        else:
            self.texts_by_year[year].append(text)

    def get_texts_by_year(self, year):
        return self.texts_by_year[year]

    def get_all_used_emojis(self, texts=None):
        if texts is None:
            texts = self.texts

        emojis = Counter(
            emoji for text in texts for emoji in text["content"].emojis)
        return dict(emojis)

    def get_most_used_emojis(self, texts=None, n=None):
        if texts is None:
            texts = self.texts
        if n is None:
            n = len(texts)

        emojis = Counter(
            emoji for text in texts for emoji in text["content"].emojis)
        return emojis.most_common(n)
