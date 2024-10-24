def main():

    expression = input("what is the expression? ")

    x, y, z = expression.split(" ")

    print(interpreter(x, y, z))

def interpreter(x, y, z):

    x = float(x)
    z = float(z)

    if y == "+":
        return(x + z)
    elif y == "-":
        return(x - z)
    elif y == "/":
        return(x / z)
    elif y == "*":
        return(x * z)

main()
