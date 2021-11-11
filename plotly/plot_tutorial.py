import os

from skimage import io
import numpy as np
import pandas as pd

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import plotly.express as px

"""
Plotly Website: https://plotly.com/python/plotly-express/
Dash Website: 

"""

if not os.path.exists("images"):
    os.mkdir("images")


""" Edit Figure Layout """
# colors = {
#     'background': '#111111',
#     'text': '#7FDBFF'
# }
#
# fig = px.bar()  # Create a fig
# fig.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )


""" Save Figure as Image """
# create desired figure
# fig = px.
# fig.write_image(output_path)

# Supported Formats:
# - .png
# - .jpeg
# - .webp

# - .svg
# - .pdf


""" Heatmap Image? """
# data = [[1, 25, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, 5, 20]]
# fig = px.imshow(data,
#                 labels=dict(x="Day of Week", y="Time of Day", color="Productivity"),
#                 x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
#                 y=['Morning', 'Afternoon', 'Evening']
#                 )
# # Move x label to the top
# fig.update_xaxes(side="top")
# fig.show()


""" Scatter Plot """
# Creates a pandas dataframe object
# df = px.data.iris()
# all_dims = ['sepal_length', 'sepal_width',
#             'petal_length', 'petal_width']

# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
# fig.show()


""" Scatter Plot, trend lines, templates, and marginal distribution plots """
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
#                  marginal_x="box", trendline="ols", template="simple_white")
# fig.show()


""" Bar Chart """
# df = px.data.tips()
# fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")
# fig.show()


""" Parallel coordinates, parallel categories, continuous color """
# df = px.data.iris()
# fig = px.parallel_coordinates(df, color="species_id", labels={"species_id": "Species",
#                                                               "sepal_width": "Sepal Width", "sepal_length": "Sepal Length",
#                                                               "petal_width": "Petal Width", "petal_length": "Petal Length", },
#                               color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)
# fig.show()

# df = px.data.tips()
# fig = px.parallel_categories(df, color="size", color_continuous_scale=px.colors.sequential.Inferno)
# fig.show()


""" Hover Labels """
# df = px.data.gapminder()
# fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#                  hover_name="country", log_x=True, size_max=60)
# fig.show()


""" Animations """
# df = px.data.gapminder()
# fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
#                  size="pop", color="continent", hover_name="country", facet_col="continent",
#                  log_x=True, size_max=45, range_x=[100,100000], range_y=[25, 90])
# fig.show()


""" Line Charts """
# df = px.data.gapminder()
# fig = px.line(df, x="year", y="lifeExp", color="continent", line_group="country", hover_name="country",
#               line_shape="spline", render_mode="svg")
# fig.show()


""" Area Chart """
# df = px.data.gapminder()
# fig = px.area(df, x="year", y="pop", color="continent", line_group="country")
# fig.show()


""" Timeline/Gantt Charts """
# df = pd.DataFrame([
#     dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
#     dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
#     dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
# ])
#
# fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Resource")
# fig.show()


""" Funnel Charts """
# data = dict(
#     number=[39, 27.4, 20.6, 11, 2],
#     stage=["Website visit", "Downloads", "Potential customers", "Requested price", "Invoice sent"])
# fig = px.funnel(data, x='number', y='stage')
# fig.show()


""" Pie Charts """
# df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
# df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries'  # Represent only large countries
# fig = px.pie(df, values='pop', names='country', title='Population of European continent')
# fig.show()


""" Sunburst Chart """
# df = px.data.gapminder().query("year == 2007")
# fig = px.sunburst(df, path=['continent', 'country'], values='pop',
#                   color='lifeExp', hover_data=['iso_alpha'])
# fig.show()


""" TreeMaps """
# df = px.data.gapminder().query("year == 2007")
# fig = px.treemap(df, path=[px.Constant('world'), 'continent', 'country'], values='pop',
#                  color='lifeExp', hover_data=['iso_alpha'])
# fig.show()


""" Icicle Chart """
# df = px.data.gapminder().query("year == 2007")
# fig = px.icicle(df, path=[px.Constant('world'), 'continent', 'country'], values='pop',
#                 color='lifeExp', hover_data=['iso_alpha'])
# fig.show()


""" Histograms """
# df = px.data.tips()
# fig = px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug", hover_data=df.columns)
# fig.show()


""" Empirical Cumulative Distribution Function (ECDF) charts """
# df = px.data.tips()
# fig = px.ecdf(df, x="total_bill", color="sex")
# fig.show()


""" Strip Charts """
# df = px.data.tips()
# fig = px.strip(df, x="total_bill", y="time", orientation="h", color="smoker")
# fig.show()


""" Density Contours """
# df = px.data.iris()
# fig = px.density_contour(df, x="sepal_width", y="sepal_length")
# fig.show()


""" Density Heatmap """
# df = px.data.iris()
# fig = px.density_heatmap(df, x="sepal_width", y="sepal_length", marginal_x="rug", marginal_y="histogram")
# fig.write_image("images/sample.svg")


""" Image """
# img = io.imread('https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Crab_Nebula.jpg/240px-Crab_Nebula.jpg')
# fig = px.imshow(img)
# fig.show()


""" Tile Map """
# df = px.data.carshare()
# fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
#                         color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
#                         mapbox_style="carto-positron")
# fig.show()


""" Tile Map GeoJSON Choropleths """
# df = px.data.election()
# geojson = px.data.election_geojson()
#
# fig = px.choropleth_mapbox(df, geojson=geojson, color="Bergeron",
#                            locations="district", featureidkey="properties.district",
#                            center={"lat": 45.5517, "lon": -73.7073},
#                            mapbox_style="carto-positron", zoom=9)
# fig.show()


""" Outline Symbol Map """
# df = px.data.gapminder()
# fig = px.scatter_geo(df, locations="iso_alpha", color="continent", hover_name="country", size="pop",
#                      animation_frame="year", projection="natural earth")
# fig.show()


""" Choropleth Map """
# df = px.data.gapminder()
# print(df.columns)
# fig = px.choropleth(df, locations="iso_alpha", color="lifeExp", hover_name="country", animation_frame="year", range_color=[20,80])
# fig.show()


""" Polar Plot """
# df = px.data.wind()
# fig = px.scatter_polar(df, r="frequency", theta="direction", color="strength", symbol="strength",
#                        color_discrete_sequence=px.colors.sequential.Plasma_r)
# fig.show()


""" Radar Chart """
# df = px.data.wind()
# fig = px.line_polar(df, r="frequency", theta="direction", color="strength", line_close=True,
#                     color_discrete_sequence=px.colors.sequential.Plasma_r)
# fig.show()


""" Polar Bar Chart """
# df = px.data.wind()
# fig = px.bar_polar(df, r="frequency", theta="direction", color="strength", template="plotly_dark",
#                    color_discrete_sequence= px.colors.sequential.Plasma_r)
# fig.show()


""" 3D Scatter Plot """
# df = px.data.election()
# fig = px.scatter_3d(df, x="Joly", y="Coderre", z="Bergeron", color="winner", size="total", hover_name="district",
#                     symbol="result", color_discrete_map={"Joly": "blue", "Bergeron": "green", "Coderre": "red"})
# fig.show()


""" Ternary Charts """
# df = px.data.election()
# fig = px.scatter_ternary(df, a="Joly", b="Coderre", c="Bergeron", color="winner", size="total", hover_name="district",
#                          size_max=15, color_discrete_map={"Joly": "blue", "Bergeron": "green", "Coderre": "red"})
# fig.show()


""" S.P.L.O.M aka Scatter Plot Matrices can add or remove parameters """
# app.layout = html.Div([
#     dcc.Dropdown(
#         id="dropdown",
#         options=[{"label": x, "value": x}
#                  for x in all_dims],
#         value=all_dims[:2],
#         multi=True
#     ),
#     dcc.Graph(id="splom"),
# ])
#
#
# @app.callback(
#     Output("splom", "figure"),
#     [Input("dropdown", "value")])
# def update_bar_chart(dims):
#     fig = px.scatter_matrix(
#         df, dimensions=dims, color="species")
#     return fig
#
#
# app.run_server(debug=True)


""" Plotting to Dash """
# import plotly.graph_objects as go
# fig = go.Figure()  # or any Plotly Express function e.g. px.bar(...)

# df = px.data.election()
# fig = px.scatter_ternary(df, a="Joly", b="Coderre", c="Bergeron", color="winner", size="total", hover_name="district",
#                          size_max=15, color_discrete_map={"Joly": "blue", "Bergeron": "green", "Coderre": "red"})

# fig.add_trace( ... )
# fig.update_layout( ... )


""" Edit Dash Layout """
# colors = {
#     'background': '#111111',
#     'text': '#7FDBFF'
# }
#
# app = dash.Dash(__name__)
#
# app.layout = html.Div(
#     style={"textAlign": 'center'},
#     children=[
#         html.H1(
#             children='Hello Dash',
#             style={
#                 'textAlign': 'center',
#                 'color': colors['text']
#             }
#         ),
#
#         html.Div(
#             children='Dash: A web application framework for your data.',
#             style={
#                 'textAlign': 'center',
#                 'color': colors['text']
#             }
#         ),
#
#         dcc.Graph(figure=fig)
#     ])


""" Reusable Components """


# def generate_table(dataframe, max_rows=10):
#     return html.Table([
#         html.Thead(
#             html.Tr([html.Th(col) for col in dataframe.columns])
#         ),
#         html.Tbody([
#             html.Tr([
#                 html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#             ]) for i in range(min(len(dataframe), max_rows))
#         ])
#     ])
#
#
# app = dash.Dash(__name__)
#
# app.layout = html.Div([
#     html.H4(children='US Agriculture Exports (2011)'),
#     generate_table(df)
# ])


""" Dash Markdown """
app = dash.Dash(__name__)

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])


""" Dash Core Component Gallery """
# website: https://dash.plotly.com/dash-core-components

# print({i: f'Label_{i}' for i in range(10)})

""" Dash External Style Sheets """
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


if __name__ == "__main__":

    app.run_server(debug=True)

    # app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
