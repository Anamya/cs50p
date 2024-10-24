def main():
    amount_due()

def amount_due():

    amount = 50
    print(f"Amount Due is: {amount}")
    #coin = int(input("Insert coin: "))

    while amount != 0:
        coin = int(input("Insert coin: "))

        if coin in [5, 10, 25]:
            if amount > coin:
                amount = amount - coin
                print(f"Amount Due: {amount}")

            else:
                change = coin - amount
                print(f"Change Owed: {change}")
                break
        else:
            print(f"Amount Due: {amount}")

main()
