def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        return True
    else:
        print("Invalid")
        return False


def is_valid(s):
    # length 2 to 6; starting 2 alphabet
    if (2 <= len(s) <= 6):
        if s.isalpha():
            return True
        elif check_start(s) and check_last(s) and check_zero(s) and mid_letter(s):
            return True
        else:
            return False
    else:
        return False

def mid_letter(s):

    num = ''

    #check where the first digit is!!
    for i in range(0, len(s)):
        if s[i].isdigit():
            num = i
            break

    # from place of 1st digit to untill rest it is only numeric and not the mix
    # this works, as we already consider the case of all alphabet
    if (s[num:].isdigit()):
        return True
    else:
        return False

def check_start(s):
    if s[:2].isalpha():
        #print("Checked 1")
        return True
    else:
        return False

def check_last(s):
    if s[-1].isdigit():
        #print("Checked 2")
        return True
    else:
        return False

def check_zero(s):
    digit = ""
    for i in range(len(s)):
        if s[i].isdigit() == True:
            digit += s[i]

            if digit[0]== "0":
                #print(digit[0])
                return False
            else:
                return True


if __name__ == "__main__":
    main()
