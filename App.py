"""Readwise Sorter: paste passages, see how hard each one is, and sort them by level."""
import pandas as pd
import streamlit as st

from levels import LEVELS, score_all

st.set_page_config(page_title="Readwise Sorter", page_icon="📚")

st.title("Readwise Sorter")
st.write(
    "Paste one or more reading passages. Leave a blank line between passages. "
    "The tool scores each one and sorts them from easiest to hardest, "
    "so you can match readings to students at different levels."
)

EXAMPLE = """My name is Hannay. I like to learn new words. I use an app on my phone. I learn a little every day.

I taught English to students online. Some of them could already read well, but others were just beginning. Every day, I tried to choose the right story for each student.

In August 2024, floods closed every English test center near me. My college deadline was only a week away, so I took the Duolingo English Test from home and made it in time.

Today I study computer science in California, where I focus on machine learning. This summer, I built a research pipeline that transformed raw sleep recordings into structured data for classification models.

This application estimates passage difficulty using established readability formulas, enabling educators to systematically differentiate instruction across heterogeneous classrooms containing learners with substantially different proficiency levels."""

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

        table = pd.DataFrame([{
            "Level": f"{r['level']} · {r['level_name']}",
            "Grade": r["grade"],
            "Reading ease": r["reading_ease"],
            "Words": r["words"],
            "Preview": r["passage"][:60] + ("…" if len(r["passage"]) > 60 else ""),
        } for r in results])
        st.dataframe(table, hide_index=True, width="stretch")

        for r in results:
            with st.expander(f"Level {r['level']} ({r['level_name']}) · passage {r['original_order']}"):
                st.write(r["passage"])
                st.caption(f"Grade {r['grade']} · {r['words']} words · {r['sentences']} sentences")
                if r["hard_words"]:
                    st.write("Words to pre-teach: " + ", ".join(sorted(r["hard_words"])))

with st.expander("How levels are decided"):
    st.write(
        "Each passage gets a Flesch-Kincaid grade level, based on sentence length "
        "and syllables per word. The grade is grouped into five levels:"
    )
    ranges = ["grade 2 and below", "grades 3–5", "grades 6–8", "grades 9–12", "college level"]
    for (number, name, _), rng in zip(LEVELS, ranges):
        st.write(f"**Level {number}, {name}:** {rng}")
