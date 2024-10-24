import sys
import os
from PIL import Image, ImageOps

def main():
    try:
        #

        if len(sys.argv) > 3:
            #if the user does not specify exactly two command-line arguments,
            sys.exit('Too Many command-line argument')

        elif (len(sys.argv) < 3):
            #if the user does not specify exactly two command-line arguments,
            sys.exit('Too few command-line argument')

        elif len(sys.argv) == 3:
            input_file = sys.argv[1]
            output_file = sys.argv[2]

            if input_file.endswith('.jpg') or input_file.endswith('.jpeg') or input_file.endswith('.png'):
                 #check input output file extension
                 if check_file_extensions(input_file, output_file):
                     get_shirt(input_file,output_file)
                 else:
                    sys.exit('File extension does not match')
            else:
                #if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
                sys.exit('Not a Valid Image')

    except (FileNotFoundError):
        #if the specified input does not exist.
        sys.exit(f"Could not read {sys.argv[1]}")

def check_file_extensions(input, output):
    input_ext = os.path.splitext(input)[1].lower()
    output_ext = os.path.splitext(output)[1].lower()
    return input_ext == output_ext

def get_shirt(img, out_img):
    try:
        shirt = Image.open("shirt.png")
        before = Image.open(img)
        size = shirt.size
        before = ImageOps.fit(image= before, size=size)
        before.paste(shirt, mask=shirt)
        before.save(out_img, format=None)

    except FileNotFoundError:
        exit("Could not find the image file")


if __name__ == "__main__":
    main()

