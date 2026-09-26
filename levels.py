"""Scoring logic for the reading-level tool (kept separate from the UI so it's easy to test)."""
import textstat

# Five levels, matching a class with five reading levels.
# Each level covers a range of U.S. grade levels (Flesch-Kincaid).
LEVELS = [
    (1, "Beginner", 2),       # grade 2 and below
    (2, "Elementary", 5),     # grades 3-5
    (3, "Intermediate", 8),   # grades 6-8
    (4, "Upper intermediate", 12),  # grades 9-12
    (5, "Advanced", float("inf")),  # college level
]


def grade_to_level(grade):
    """Turn a grade-level score into one of the five levels."""
    for number, name, max_grade in LEVELS:
        if grade <= max_grade:
            return number, name
    return LEVELS[-1][0], LEVELS[-1][1]


def split_passages(text):
    """Split pasted text into passages wherever there is a blank line."""
    blocks = [b.strip() for b in text.replace("\r\n", "\n").split("\n\n")]
    return [b for b in blocks if b]


def score_passage(passage):
    """Return the reading scores and level for one passage."""
    grade = max(0.0, textstat.flesch_kincaid_grade(passage))
    number, name = grade_to_level(grade)
    return {
        "level": number,
        "level_name": name,
        "grade": round(grade, 1),
        "reading_ease": round(textstat.flesch_reading_ease(passage), 1),
        "words": textstat.lexicon_count(passage),
        "sentences": textstat.sentence_count(passage),
        "hard_words": textstat.difficult_words_list(passage),
    }


def score_all(text):
    """Score every passage and sort from easiest to hardest."""
    results = []
    for i, passage in enumerate(split_passages(text), start=1):
        row = score_passage(passage)
        row["passage"] = passage
        row["original_order"] = i
        results.append(row)
    return sorted(results, key=lambda r: r["grade"])
