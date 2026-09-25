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


