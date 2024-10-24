from random import randint
import sys

def main():
    guess_game()


def guess_game():

    while True:
        try:
            level = int(input("Level: "))
            if (level < 0):
                continue

            rand_num = randint(1, level)
            #print(rand_num)

            while True:
                try :
                    guess = int(input("Guess: "))

                    try:
                        if guess < 0:
                            continue
                        if guess < rand_num:
                            print("Too small!")
                            continue
                        elif guess > rand_num:
                            print("Too large!")
                            continue
                        else:
                            sys.exit("Just right!")

                    except ValueError:
                        pass
                except ValueError:
                        pass

        except ValueError:
            pass
        except EOFError:
            print()
            break

main()
