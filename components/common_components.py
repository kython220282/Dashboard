import streamlit as st

def render_common_components():
    """Render common filters used across all tabs."""
    st.header("Filters")
    date_range = st.date_input("Select Date Range", [])
    filter_1 = st.selectbox("Filter 1", ["Option 1", "Option 2", "Option 3"]) #Update the Filter name and options
    filter_2 = st.multiselect("Filter 2", ["Option A", "Option B", "Option C"]) #Update the Filter name and options
    return date_range, filter_1, filter_2
