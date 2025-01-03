import streamlit as st

def tab_one():
    """Content and layout for Tab One."""
    st.title("Tab One")
    col1, col2 = st.columns([1, 3])
    with col1:
        date_range, filter_1, filter_2 = render_common_components()
    with col2:
        st.write("Content specific to Tab One")
        # Add tab-specific content here
