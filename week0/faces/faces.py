def main():

    message = str(input("Write text: "))
    convert(message)

def convert(to_convert):
    faces = to_convert.replace(":)", "🙂").replace(":(", "🙁")
    print(faces)

main()
