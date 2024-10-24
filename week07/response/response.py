import validators

def main():
    print(validate_email(input("What is your email address? ")))


def validate_email(email_id):
    if validators.email(email_id) == True:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()

