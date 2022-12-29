from collections import Counter
import re

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
    
    def get_all_used_emojis(self, texts):
        if texts is None:
            texts = self.texts
        
        emojis = {}
        for text in texts:
            for emoji in text.emojis:
                if emoji not in emojis:
                    emojis[emoji] = 1
                else:
                    emojis[emoji] += 1
                
        return emojis.items()
    
    def get_most_used_emojis(self, texts, n):
        if texts is None:
            texts = self.texts
        
        emojis = {}
        for text in texts:
            for emoji in text.emojis:
                if emoji not in emojis:
                    emojis[emoji] = 1
                else:
                    emojis[emoji] += 1
        
        sorted_emojis = sorted(emojis.items(), key=lambda x: x[1], reverse=True)
        
        return sorted_emojis[:n]
