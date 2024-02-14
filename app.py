from flask import *
import re, pandas
from whatsapp_wrapped import *
from datetime import date

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("./index.html")


@app.route("/api/whatsapp-wrapped", methods=["POST"])
def whatsapp_wrapped():
    if "file" not in request.files:
        return "No file part in the request", 400

    file = request.files["file"]
    if file.filename == "":
        return "No file selected", 400

    year = date.today().year -1


    cleaned_lines = process_lines(file)
    df = extract_data(cleaned_lines)
    
    # TODO calculate number of entries to do based on group size

    n = 5

    filtered_df = df.loc[df["wa_datetime"].dt.year == int(year)]

    name_rank = pandas.DataFrame(rank_names_by_messages(filtered_df, n))
    emoji_rank = pandas.DataFrame(rank_emoji_distinct(filtered_df, n))
    month_rank = pandas.DataFrame(rank_months_by_messages(filtered_df, n))

    print("START PRINT")
    print(name_rank)
    print(emoji_rank)
    print(month_rank)
    print("END PRINT")

    name_rank_json = name_rank.to_json(orient='index')
    emoji_rank_json = emoji_rank.to_json(orient='index')
    month_rank_json = month_rank.to_json(orient='index')

    response = {
        "nameRank": name_rank_json,
        "emojiRank": emoji_rank_json,
        "monthRank": month_rank_json,
    }

    return response

def process_lines(file):
    for line in file:
        decoded_line = line.decode("utf-8")
        if "\u200E" not in decoded_line:
            yield decoded_line.strip()


def extract_data(lines):
    pattern = r"\[(\d{2}\.\d{2}\.\d{4}), (\d{2}:\d{2}:\d{2})\] ([\w\s]+): ([\s\S]*)"

    messages = []

    for line in lines:
        match = re.match(pattern, line)
        if match:
            datetime = pandas.to_datetime(
                match.group(1) + "-" + match.group(2), format="%d.%m.%Y-%H:%M:%S"
            )
            messages.append(
                {
                    "wa_datetime": datetime,
                    "wa_name": match.group(3),
                    "wa_text": match.group(4),
                }
            )

    return pandas.DataFrame(messages)