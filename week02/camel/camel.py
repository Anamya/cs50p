def main():
    msg = input("Camel Message: ")


    #if everything is already in lowecase print as it is
    if msg.islower():
        print(msg)

    #else call the function snake_case()
    else:
        print(snake_case(msg))
    #print('\n')

def snake_case(m):
    #print(".......")

    snake = ''
    for character in m:

        if character.islower():
            snake += character

        else:
            snake += '_' + character.lower()

    return(snake)

main()
