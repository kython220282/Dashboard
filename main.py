import streamlit as st

from pages.tab_one import tab_one
from pages.tab_two import tab_two

st.set_page_config(layout="wide")  # Optional: Full-width layout

# Tab navigation
tabs = st.tabs(["Tab One", "Tab Two"])

with tabs[0]:
    tab_one()

with tabs[1]:
    tab_two()
