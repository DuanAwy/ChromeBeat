import streamlit as st

with st.expander(""):
    color = st.color_picker(" Pick A Color for you Day🥳", "#00f900")
    st.write("The current color is", color)