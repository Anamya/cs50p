import sys
import csv

# CS50 submitted
def main():
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        if len(sys.argv) == 3:
            if ( input_file.endswith('.csv')): # & output_file.endswith('.csv')):
                get_names(input_file, output_file)
            #else:
            #    sys.exit(f"Could not read {input_file}")

        elif len(sys.argv) > 3:
            sys.exit('Too Many command-line argument')

    except IndexError:
        sys.exit('Too few command-line argument')
    except (FileNotFoundError):
        sys.exit(f"Could not read {sys.argv[1]}")

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
