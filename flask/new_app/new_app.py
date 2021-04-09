from flask import Flask, render_template, request

import folium as fo

"""
Program: Simple Map Webapp
Author: Rickyg3
Date: 04/08/2021
"""

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/page1')
def web_page1():
    return render_template("web1.html")


@app.route('/page1/data',  methods=['POST', 'GET'])
def custom_func():
    if request.method == 'GET':
        return f"The URL /data is accessed directly, go through '/map'"
    if request.method == 'POST':
        form_input = request.form
        input1 = form_input["input1"]
        input2 = form_input["input2"]
        # print(input1, input2)

        return render_template('data.html', form_data=form_input)


if __name__ == '__main__':
    app.run(debug=True)
    # sample_map.save("map.html")
