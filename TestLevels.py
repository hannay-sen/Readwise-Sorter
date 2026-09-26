from levels import grade_to_level, split_passages, score_all

def test_grade_to_level():
    assert grade_to_level(1)[0] == 1
    assert grade_to_level(4)[0] == 2
    assert grade_to_level(7)[0] == 3
    assert grade_to_level(10)[0] == 4
    assert grade_to_level(15)[0] == 5

def test_split_passages():
    assert split_passages("a\n\nb\n\n\n\nc") == ["a", "b", "c"]
    assert split_passages("   ") == []

def test_sorted_easiest_first():
    text = ()
    results = score_all(text)
    assert results[0]["original_order"] == 2
    assert results[0]["grade"] <= results[1]["grade"]
