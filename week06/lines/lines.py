import sys

def main():

    try:
        input_file = sys.argv[1]
        if len(sys.argv) == 2:
            if input_file.endswith('.py'):
                count_lines(input_file)
            else:
                sys.exit('Not a Python File')

        elif len(sys.argv) > 2:
            sys.exit('Too Many command-line argument')

    except IndexError:
        sys.exit('Too few command-line argument')
    except (FileNotFoundError):
        sys.exit("File Doesn't exist")


def count_lines(file_name):

    line_count = 0
    with open(file_name) as file:
        for line in file:
            #print(line)
            if not (line.lstrip().startswith("#") or line.strip() == ""):
                line_count += 1
                #print(line_count)
    print(line_count)

if __name__ == "__main__":
    main()
