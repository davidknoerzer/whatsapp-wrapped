from flask import *
import re, pandas
from whatsapp_wrapped import *

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/whatsapp-wrapped", methods=["POST"])
def whatsapp_wrapped():
    if "file" not in request.files:
        return "No file part in the request", 400

    file = request.files["file"]
    if file.filename == "":
        return "No file selected", 400

    year = request.args.get("year")

    cleaned_lines = process_lines(file)
    df = extract_data(cleaned_lines)

    n = 3

    filtered_df = df.loc[df["wa_datetime"].dt.year == int(year)]

    name_rank = rank_names_by_messages(filtered_df, n)
    emoji_rank = rank_emoji_distinct(filtered_df, n)
    month_rank = rank_months_by_messages(filtered_df, n)

    print("RESPONSE:")

    response = {
        "name_rank": name_rank.to_json,
        "emoji_rank": emoji_rank.to_json,
        "month_rank": month_rank.to_json,
    }

    print(response)

    return response
    # return render_template("whatsapp_wrapped.html", name=f.filename)


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


if __name__ == "__main__":
    app.run(debug=True)
