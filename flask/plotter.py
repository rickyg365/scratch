from flask import Flask

import folium as fo
import plotly

"""
 
"""

app = Flask(__name__)


@app.route('/')
def index():
    long_coord = float(input("choose long: "))
    lat_coord = float(input("choose lat: "))
    start_coord = (long_coord, lat_coord)
    sample_map = fo.Map(location=start_coord, zoom_start=15)

    return sample_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
    # sample_map.save("map.html")
