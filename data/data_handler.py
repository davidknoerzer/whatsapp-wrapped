import re
from text import Text
from sender import Sender


def prep_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if u'\u200E' not in line:
                outfile.write(line)


def scan_data(data):
    sender_dict = {}

    regex = re.compile(
        r'\[(?P<date>\d{2}.\d{2}.\d{4}), (?P<time>\d{2}:\d{2}:\d{2})] (?P<sender>.+?): (?P<message>.+)')

    with open(data, 'r', encoding='utf-8') as f:
        data = f.read()

    for line in data.split('\n'):
        match = regex.search(line)

        if match:
            sender_name = match.group('sender')
            date = match.group('date')
            time = match.group('time')
            message = match.group('message')

            text = Text(date, time, message)

            if sender_name not in sender_dict:
                sender_dict[sender_name] = Sender(sender_name)

            sender_dict[sender_name].add_text(text)
    return sender_dict
