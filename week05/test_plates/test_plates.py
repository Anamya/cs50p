from plates import is_valid


def test_length():
  assert is_valid('CS50') == True
  assert is_valid("ABCDE563") == False
  assert is_valid("A") == False

def test_last_number():
  assert is_valid('CDCS50') == True
  assert is_valid('CDC050') == False

def test_check_first():
  assert is_valid('CDCS50') == True
  assert is_valid("12AB12") == False
  assert is_valid("12ABAA") == False
  assert is_valid("12234") == False

def test_check_middle():
   assert is_valid("PI3.14") == False
   assert is_valid("BA1P22") == False
   assert is_valid("ABCD63P") == False

