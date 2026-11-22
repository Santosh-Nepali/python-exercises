## ```Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not.
# Use the prior prime number exercise as a starting point. For example, a GET request for number 31 is given as: http://127.0.0.1:3000/prime_number/31.
# The response must be in the format of {"Number": 31, "isPrime": true}. (4p)
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("prime.html")


@app.route("/prime", methods=["POST"])
def checkPrime():

    # numbers = request.args
    # number = numbers.get("number")
    # receive the JSON data from AJAx
    data = request.get_json(silent=True)

    # Check wether JSON data exists
    if not data or "number" not in data:
        return jsonify({"error": "please provide a number"}), 400
    # check empty input
    if str(data["number"]).strip() == "":
        return jsonify({"error": "Number cannot be empty"}), 400

    # Convert into number
    try:
        number = int(data["number"])
    except:
        return jsonify({"error": "Invalid number"}), 400

    # checking for negative values
    if number <= 0:
        return jsonify({"error": "Negative or zero are not allowd"}), 400

    # check whether number is prime or not
    isPrime = True
    if number < 2:
        isPrime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                isPrime = False
                break

    # sending back the number as result
    return jsonify({"number": number, "isPrime": isPrime})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True, use_reloader=False)
