def main():
    message = input("Whats the greetings? ")

    print(greetings(message.strip()))

def greetings(m):

    if m.startswith("hello") or m.startswith("Hello"):
        return("$0")
    elif m.startswith("h") or m.startswith("H"):
        return("$20")
    else:
        return("$100")

main()
