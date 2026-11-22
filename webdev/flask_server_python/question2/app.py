## Implement a Flask backend service that receives an English word as a parameter and returns its Finnish translation in JSON format. The English–Finnish dictionary is stored in a separate JSON file on disk (10p)
from flask import Flask, request, render_template, jsonify, json
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("translation.html")


@app.route("/translateEnglishFinnish/<word>", methods=["GET"])
def getdata(word):

    file_path = os.path.join(app.root_path, "dictionary.json")

    with open(file_path, "r", encoding="utf-8") as file:
        dictionary = json.load(file)

        word = word.lower()
        print(word)

        translation = dictionary.get(word)
        print(translation)

        if translation is None:
            return jsonify({"error": "Word is not found"}), 404

        return jsonify({"english": word, "finnish": translation}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True, use_reloader=False)
