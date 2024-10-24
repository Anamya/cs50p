import sys
from datetime import date
import inflect

p = inflect.engine()

def get_age(dob):
    try:
        birthday = date.fromisoformat(dob)
        #print(date.today())
        return (date.today() - birthday).days

    except ValueError:
        return sys.exit("Invalid date")

def convert_age(days):
    age_minutes = int(days) * 24 * 60
    return(p.number_to_words(age_minutes, andword="").capitalize())

def main():
    birthday = get_age(input("Enter Birthday: "))
    #print(birthday)
    print(f"{convert_age(birthday)} minutes")

if __name__ == "__main__":
    main()
