# Reading Level Sorter

A small web app that helps teachers match reading passages to students at different levels.
Paste in passages, and it scores how hard each one is to read, sorts them from easiest to hardest,
and lists the harder words worth teaching before students read.

## Why I built it

I taught English online to students aged 7 to 20, often with five reading levels in the same class.
Picking the right passage for each student took a lot of guessing. This tool replaces some of that
guessing with data.

## How it works

- Each passage gets a Flesch-Kincaid grade level, based on sentence length and syllables per word (using `textstat`).
- The grade is grouped into five levels, from Beginner (grade 2 and below) to Advanced (college level).
- Passages are sorted easiest first, with a list of difficult words for each one.

## Run it locally

```
pip install -r requirements.txt
streamlit run app.py
```

## Tests

```
pip install pytest
pytest
```

## Built with

Python, Streamlit, textstat, pandas
