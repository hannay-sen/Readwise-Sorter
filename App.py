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
 
text = st.text_area("Passages", key="text", height=250,
                    placeholder="Paste your passages here…")
 
if st.button("Sort by reading level", type="primary"):
    results = score_all(text)
    if not results:
        st.warning("Paste at least one passage to score.")
    else:
        st.subheader(f"{len(results)} passage(s), easiest first")
 
       
