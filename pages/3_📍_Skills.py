import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/skaiser-log/hp-streamlit>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDU0NnlkMWZxcnBqOHVnZXdsNTh1YmVleWpwNGVyaXE3bzRmdmtkaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/p6RVGDmsXrONHCYG3R/giphy.gif"
st.sidebar.image(logo)

st.title("Skills")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[40, -100], zoom=4)
        cities = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
        regions = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson"

        m.add_geojson(regions, layer_name="US Regions")
        m.add_points_from_xy(
            cities,
            x="longitude",
            y="latitude",
            color_column="region",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
