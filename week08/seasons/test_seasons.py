from week08.seasons.seasons import get_age, convert_age

def main():
    test_get_age()
    test_convert_age()

def test_get_age():
    assert get_age('2023-08-21') == 366
    assert get_age('2022-08-21') == 731
    assert get_age('2024-08-20') == 1

def test_convert_age():
    assert convert_age(366) == 'Five hundred twenty-seven thousand forty'
    assert convert_age(731) == 'One million, fifty-two thousand, six hundred forty'
