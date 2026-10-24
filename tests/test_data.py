from sentiment.data import clean_text

def test_drops_quoted_lines():
    assert clean_text("> you are wrong\nNo, I'm not.") == "No, I'm not."