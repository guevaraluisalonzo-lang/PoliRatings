from sentiment.data import clean_text

def test_CleanText_drops_quoted_lines():
    assert clean_text("> you are wrong\nNo, I’m not.") == "No, I’m not."

def test_clean_text_removes_bare_url():
    assert clean_text("check https://youtube.com out") == "check out"

def test_CleanText_squishes_spaces():
    assert clean_text("I like  this") == "I like this"

def test_CleanText_still_leaves_text_with_link():
    assert clean_text('[Feel like we’ve seen this before](https://youtube.com)') == "Feel like we’ve seen this before"

def test_CleanText_combined_with_remove_extra_space_and_remove_link():
    assert clean_text(" While I still read news I use cdc and [NIH](https://www.nih.gov/) often") == "While I still read news I use cdc and NIH often"

def test_CleanText_against_null():
    assert clean_text(None) == ""

def test_CleanText_against_emptytext():
    assert clean_text("") == ""

def test_CleanText_normal_text():
    assert clean_text("Hello") == "Hello"

def test_CleannText_leave_bold_text():
    assert clean_text("**Hello**") == "**Hello**"

def test_CleanText_leave_italicized_text():
    assert clean_text("*Hello*") == "*Hello*"

def test_CleanText_leave_quotes():
    assert clean_text('He called it "great" lol') == 'He called it "great" lol'

def test_clean_text_handles_nan():
    assert clean_text(float("nan")) == ""


def test_clean_text_quote_only_returns_empty():
    assert clean_text("> just a quote") == ""


def test_clean_text_drops_quote_without_space_after_marker():
    assert clean_text(">no space\nreply") == "reply"


def test_clean_text_drops_quote_followed_by_tab():
    assert clean_text(">\tquoted\nreply") == "reply"


def test_clean_text_collapses_newlines_and_tabs():
    assert clean_text("a\n\n b\tc") == "a b c"


def test_clean_text_unescapes_html_codes():
    assert clean_text("a &amp; b") == "a & b"


def test_clean_text_unescapes_before_detecting_quotes():
    assert clean_text("&gt; quoted\nreply") == "reply"


def test_clean_text_removes_zero_width_space():
    assert clean_text("a&#x200B;b") == "ab"


def test_clean_text_removes_multiple_urls():
    assert clean_text("see https://a.com and https://b.org now") == "see and now"


def test_clean_text_keeps_double_quoted_phrases():
    assert clean_text('He called it "great" lol') == 'He called it "great" lol'


def test_clean_text_removes_url_ending_in_parenthesis():
    assert clean_text("see https://en.wikipedia.org/wiki/Foo_(bar) ok") == "see ok"