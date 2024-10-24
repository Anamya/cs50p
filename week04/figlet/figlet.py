from pyfiglet import Figlet
import sys
import random

def main():
    figlet_call()

def figlet_call():
    figlet = Figlet()
    fonts = figlet.getFonts()

    valid_arg = ["-f", "--font"]

    # IN below two lines you get random number between 0 to length of all the fonts available in pyfiglet
    font_index = random.randrange(0, len(fonts))

    #set random font as default
    set_font = fonts[font_index]

    # check if there is arg passed or not
    if not (len(sys.argv) == 1 or len(sys.argv) == 3):
        #print(sys.argv[1])
        sys.exit("Invalid usage")

    if (len(sys.argv) == 3):
        if (sys.argv[1] not in valid_arg) or (sys.argv[2] not in fonts):
            sys.exit("Invalid usage")
        else:

            # if valid font is provided in command line, then the default set_font is overwritten by the user preference
            set_font = sys.argv[2]

    input_text = input("Input: ")

    figlet.setFont(font=set_font)
    print(figlet.renderText(input_text))


main()
