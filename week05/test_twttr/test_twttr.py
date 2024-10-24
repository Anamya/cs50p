from twttr import shorten

def test_twttr():
    assert shorten('Hi') == 'H'
def test_middle_upper():
    assert shorten('Hello, How Are you?') == 'Hll, Hw r y?'

def test_capitalized_vowel():
    assert shorten('AbOrt') == 'brt'
def test_numbers():
    assert shorten('Tweet 20') == 'Twt 20'
    assert shorten('20') == '20'

def test_punct():
    assert shorten("What's your name") == "Wht's yr nm"
def test_novowel():
    assert shorten('CS50') == 'CS50'
