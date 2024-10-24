import random


def main():
    problem = 10
    score = 0
    chance = 3

    level_selected = get_level()

    while problem != 0:
        if chance  == 3:
            x, y = generate_integer(level_selected)
        try:
            user_answer = int(input(f"{x} + {y} = "))
            answer = x + y

            if answer == user_answer:
                score += 1
                problem -= 1
                chance = 3
                continue
            else:
                print("EEE")
                chance = chance - 1

                if chance == 0:
                    print(f"{x} + {y} = {answer}")
                    chance = 3
                    problem -= 1
                    continue


        except ValueError:
            pass

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y



if __name__ == "__main__":
    main()
