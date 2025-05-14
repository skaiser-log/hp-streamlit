import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
An online web app showcasing some of my skill in GIS, Phyton and Web Development. My LinkedIn profile: 
<https://www.linkedin.com/in/silvio-kaiser/>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDU0NnlkMWZxcnBqOHVnZXdsNTh1YmVleWpwNGVyaXE3bzRmdmtkaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/p6RVGDmsXrONHCYG3R/giphy.gif"
st.sidebar.image(logo)

# Customize page title
st.title("SILVIO KAISER")

st.markdown(
    """
    Driven by accelerating decision making with Data by leveraging the power of GIS, Python and Web Development.
    """
)

st.header("GIS (ArcGIS PRO, QGIS) | Python | WebGIS | GeoBIM | Data Engineering")

markdown = """
Starting my academic journey in my hometown of Munich, I ventured to the Netherlands to specialize in water management, focusing on Delta Management and Spatial Planning & Design. My global perspective was further enriched with a minor at Waterloo University in Canada, where I delved into global development and green entrepreneurship. The most transformative experience, however, was my internship at IDOM in Spain. There, I had the opportunity to apply my skills to two significant Saudi Arabian projects, both aimed at revolutionizing sustainable water use and network design. This blend of specialized education and practical, international experience equips me as a versatile asset for addressing complex environmental challenges.

"""

st.markdown(markdown)

# Initialize the map
m = leafmap.Map(center=[-100, 40], zoom=3, style="basic", projection="globe")

# Display the map in Streamlit
st.title("3D Buildings in Leafmap")
m.to_streamlit()