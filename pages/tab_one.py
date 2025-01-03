import streamlit as st
from components.common_components import render_common_components

def tab_one():
    st.title("Tab One")
    col1, col2 = st.columns([1, 3])
    with col1:
        date_range, filter_1, filter_2 = render_common_components()
    with col2:
        st.write("Content specific to Tab One")
    
