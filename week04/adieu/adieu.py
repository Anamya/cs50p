import inflect
import sys


def main():
    get_adieu()

def get_adieu():

    inflector = inflect.engine()
    names = []

    while True:
        try:
            name = input().title().strip()
            # by mistake if auther press enter with out names, it is not added to the names list
            if name != "":
                names.append(name)

        except EOFError:
            #print()
            break


    if len(names) >= 1:
        final_sent = inflector.join(names, final_sep=",")
        #print(f"Adieu, adieu, to {final_sent}")
    elif len(names) > 1:
        final_sent = inflector.join(names, final_sep=",")
    print(f"Adieu, adieu, to {final_sent}")

    #print(len(names))
    #print(names)




main()
