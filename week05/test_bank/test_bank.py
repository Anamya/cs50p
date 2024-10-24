from bank import value


def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0

def test_h():
    assert value("Hi") == 20
    assert value("hi") == 20

def test_other_greetings():
    assert value("Whats up") == 100
    assert value("whats up") == 100
