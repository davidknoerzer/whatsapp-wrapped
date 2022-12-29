from datetime import datetime
import re

class Text:
    def __init__(self, date, time, message):
        self.date = date
        self.time = time
        self.message = message
        self.emojis = re.findall(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U0001F3FB-\U0001F3FC\U0001F3FD-\U0001F3FE\U0001F3FF]', message)
        skin_tones = ['\U0001F3FB', '\U0001F3FC', '\U0001F3FD', '\U0001F3FE', '\U0001F3FF',]
        for skin_tone in skin_tones:
            if skin_tone in self.emojis:
                self.emojis.remove(skin_tone)

    
    def parse_datetime(self):
        return datetime.strptime(f'{self.date} {self.time}', '%d.%m.%y %H:%M:%S')