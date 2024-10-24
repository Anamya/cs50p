import sys
import csv


def main():
    if len(sys.argv) > 3:
        #if the user does specify more than 2 command-line arguments,
        sys.exit('Too Many command-line argument')
    elif (len(sys.argv) < 3):
        #if the user does less than two command-line arguments,
        sys.exit('Too few command-line argument')
    elif len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        if ( input_file.endswith('.csv')):
            get_names(input_file, output_file)
        else:
            sys.exit(f'{input_file} is Not a  CSV')

def get_names(inputFile, outputFile):
    names = []
    with open(inputFile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            last_name, first_name  = row["name"].split(', ')
            names.append({"first": first_name.strip(), "last": last_name.strip(), "house": row["house"]})

    with open(outputFile, "w") as output:
        outReader = csv.DictWriter(output, fieldnames=["first", "last", "house"])
        outReader.writeheader()
        for i in range(len(names)):
            outReader.writerow({'first': names[i]["first"], 'last': names[i]["last"], 'house': names[i]["house"]})

if __name__ == "__main__":
    main()
