from flask import Flask, render_template, request

from reference.irl_items import *
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


'''
Add functions
to search databse using tags or name
to add a new item

'''


@app.route('/display')
def display():
    data = website_items.items
    return render_template("items.html", form_data=data)


@app.route('/page1/data',  methods=['POST', 'GET'])
def custom_func():
    if request.method == 'GET':
        return f"The URL /data is accessed directly, go through '/map'"
    if request.method == 'POST':
        form_input = request.form
        new_item = Item(form_input["name"], form_input["description"], int(form_input["quantity"]), form_input["tags"])
        website_items.add_item(new_item)
        # input2 = form_input["input2"]
        # print(input1, input2)

        return render_template('data.html', form_data=form_input)


if __name__ == '__main__':
    website_items = ItemContainer("Website Items")
    website_items.load_csv("reference/website_items.csv", 'name')
    app.run(debug=True)
    # sample_map.save("map.html")
