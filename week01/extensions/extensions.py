def main():
    file = input("File name?: ")
    extension(file)

def extension(f):
    end = f.split(".")[-1].strip().replace("\n", "").casefold()

    if end in ("gif", "png"):
        print("image/"+ end)
    elif end in ("jpg", "jpeg"):
        print("image/jpeg")
    elif end in ("pdf","zip"):
        print("application/"+ end)
    elif end in ("txt"):
        print("text/plain")
    else:
        print("application/octet-stream")

main()
