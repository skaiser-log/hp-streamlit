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

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.split_map(
            left_layer="ESA WorldCover 2020 S2 FCC", right_layer="ESA WorldCover 2020"
        )
        m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")

m.to_streamlit(height=700)
