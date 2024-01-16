import re, pandas


def prep_data(input_file, output_file):
    with open(input_file, "r", encoding="utf-8", errors="ignore") as infile, open(
        output_file, "w", encoding="utf-8"
    ) as outfile:
        for line in infile:
            if "\u200E" not in line:
                outfile.write(line)


def match_data(data_path):
    with open(data_path, "r", encoding="utf-8") as file:
        data = file.read()

    pattern = r"\[(\d{2}\.\d{2}\.\d{4}), (\d{2}:\d{2}:\d{2})\] (\w+ \w+): (.*)"
    matches = re.findall(pattern, data)
    messages = []

    for match in matches:
        message = {
            "date": match[0],
            "time": match[1],
            "name": match[2],
            "text": match[3],
        }
        messages.append(message)
    df = pandas.DataFrame(messages)

    return df
