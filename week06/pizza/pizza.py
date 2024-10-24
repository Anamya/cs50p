import sys
from tabulate import tabulate
import csv ;
#from StringIO import StringIO

def main():

    try:
        csv_file = sys.argv[1]
        if len(sys.argv) == 2:
            if csv_file.endswith('.csv'):
                ascii_art(csv_file)
            else:
                sys.exit('Not a CSV File')

    except IndexError:
        sys.exit('Too few command-line argument')
    except (FileNotFoundError):
        sys.exit("File Doesn't exist")

def ascii_art(csv_file):
    menu = []
    with open(csv_file, newline='') as file:
        csvReader = csv.reader(file, delimiter=',')
        for row in csvReader:
            #print(row)
            menu.append(row)
        print(tabulate(menu, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
