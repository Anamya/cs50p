from jar import Jar
import pytest

def test_init():
    jar = Jar()

def test_set():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_capacity():

    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(1)
    assert jar.size == 4

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

def main():
    test_init()
    test_deposit()
    test_withdraw()
