def main():
    print(remove_vowels())

def remove_vowels():
    msg = input("What is the tweet? ")
    edited = ""
    for letter in msg:

        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            edited += letter
    return(edited)

main()
