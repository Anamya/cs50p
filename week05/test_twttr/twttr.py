def main():
    msg = input("What is the tweet? ")
    shorten_msg = shorten(msg)
    print(shorten_msg)

def shorten(shorten_msg):
    edited = ""
    for letter in shorten_msg:
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            edited += letter
    return(edited)


if __name__ == "__main__":
    main()
