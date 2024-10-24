def main():
    question = input("What is the answer to the great question of life, the universe and everything? ")
    deep(question)

def deep(q):

    if q.strip() == "42":
        print("Yes")
    elif q.lower() == "forty-two":
        print("Yes")
    elif q.lower() == "forty two":
        print("Yes")
    else:
        print("No")

main()
