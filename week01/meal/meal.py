def main():
    timing = input("What is the time in 24hr System? ")

    #print(convert(timing))
    time = convert(timing)

    if  7.0 <= time <= 8.0:
        print("Breakfast time")

    elif 12.0 <= time <= 13.0:
        print("Lunch time")

    elif 18.0 <= time <= 19.0:
        print("Dinner time")
    else:
        print("")

def convert(time):
    hour, minute = time.split(":")

    mint = round(int(minute)/60.0, 2)

    timing = int(hour) + mint
    #print(timing)
    return(timing)




if __name__ == "__main__":
    main()
