import sys

#print("hello, my name is", sys.argv[1])

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
