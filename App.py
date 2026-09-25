""Reading Level Sorter: paste passages, see how hard each one is, and sort them by level."""

import pandas as pd
import streamlit as st
 
from levels import LEVELS, score_all
 
st.set_page_config(page_title="Reading Level Sorter", page_icon="📚")
 
st.title("Reading Level Sorter")
st.write(
    "Paste one or more reading passages. Leave a blank line between passages. "
    "The tool scores each one and sorts them from easiest to hardest, "
    "To match readings to students at different levels."
)
 
if "text" not in st.session_state:
    st.session_state.text = ""
 
if st.button("Load example passages"):
    st.session_state.text = EXAMPLE
 
