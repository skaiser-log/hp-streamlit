import streamlit as st
import leafmap.foliumap as leafmap

markdown = """
A Streamlit map template
<https://github.com/skaiser-log/hp-streamlit>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDU0NnlkMWZxcnBqOHVnZXdsNTh1YmVleWpwNGVyaXE3bzRmdmtkaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/p6RVGDmsXrONHCYG3R/giphy.gif"
st.sidebar.image(logo)


st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:

    m = leafmap.Map(
        locate_control=True, latlon_control=True, draw_export=True, minimap_control=True
    )
    m.add_basemap(basemap)
    m.to_streamlit(height=700)
