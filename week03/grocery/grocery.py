def main():

    grocery_list()

def grocery_list():

    groceries = {}

    while True:
        try:
            item = input().upper()

            if item in groceries:
                groceries[item] +=1
            else:
                groceries[item] =1


        except EOFError:
            break

    for item, quantity in sorted(groceries.items()):
        print(quantity ,item)





main()
