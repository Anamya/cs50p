def main():

    pct = get_fraction()
    #print(pct)
    fuel_status = get_fuel(pct)

def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map (int, fraction.split("/"))
            result = round(x/y*100)
            if result >= 0 and result <= 100:
                    return result

        except (ValueError, ZeroDivisionError):
            #print("Can't be convertd")
            pass

def get_fuel(c):

    if c <= 1:
        print("E")

    elif c >= 99 and c <= 100:
        print("F")

    else:
        print(f"{c}%")

main()
