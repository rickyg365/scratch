import os
import json

from dotenv import load_dotenv
from nasa import get_apod_data, parse_apod
from flask import Flask, render_template, url_for, redirect, request


# Load Token
load_dotenv()

NASA_TOKEN = os.getenv('NASA_TOKEN')


# APOD Data
raw_apod = get_apod_data(NASA_TOKEN)

apod_data = parse_apod(raw_apod)


# Routes
app = Flask("APOD")

@app.route("/", methods=["POST", "GET"])
def home():
    # return jsonify(nasa.apod())
    if request.method == "POST":
        # if 'getpic' in request.form:
        return redirect(url_for("data"))
    else:
        return render_template("getpic.html")

@app.route("/data")
def data():
    # return jsonify(nasa.apod())
    return render_template("data.html", data=raw_apod)


if __name__ == "__main__":
    app.run(debug=True)


