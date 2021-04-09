from flask import Flask, render_template, request

import folium as fo
import plotly

"""
Program: Simple Map Webapp
Author: Rickyg3
Date: 04/08/2021
"""

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/map')
def map_home():
    """
    long_coord = float(input("choose long: "))
    lat_coord = float(input("choose lat: "))
    start_coord = (long_coord, lat_coord)
    sample_map = fo.Map(location=start_coord, zoom_start=15)

    return sample_map._repr_html_()
    """

    return render_template("map.html")


@app.route('/map/data', methods=['POST', 'GET'])
def mdata():
    if request.method == 'GET':
        return f"The URL /data is accessed directly, go through '/map'"
    if request.method == 'POST':
        map_data = request.form
        print(map_data)
        # From the form file we use the label/input names
        data_coord = f"{float(map_data['longitude'])},{float(map_data['latitude'])}"

        return render_template('data.html', start_coord=data_coord, form_data=map_data)


@app.route('/map_display/<coord>')
def map_show(coord):
    start_coordinates = coord.split(",")
    sample_map = fo.Map(location=start_coordinates, zoom_start=20)

    return sample_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
    # sample_map.save("map.html")
