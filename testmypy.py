#def meow(n: int):
#    for _ in range(n):
#        print("meow")
    
#number = input("Number: ")
#meow(number)

#import sys

#if len(sys.argv) == 1:
#    print("meow")
#else: 
#    print("usage: meows.py")

#if len(sys.argv) == 1:
#    print("meow")
#elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#    n = int(sys.argv[2])
#    for _ in range(n):
#        print("meow")
#else: 
#    print("usage: meows.py")

import argparse

#parser = argparse.ArgumentParser(description="Meow like a cat")
#parser.add_argument("-n", default=1, help="number of times to meow", type=int)
#args = parser.parse_args()
#This imports sys and figures out all of that for me.

#for _ in range(int(args.n)):
#    print("meow")

#def main():
#    yell("this", "is", "cs50")
    #notice no []

#def yell(*words):
#    uppercased = map(str.upper, words)
#    print(*uppercased)
#def yell(*words):
#    uppercased = [word.upper() for word in words]
#    print(*uppercased)

#if __name__ == "__main__":
#    main()

# students = ["Hermione", "Harry", "Ron"]

# for i, student in enumerate(students, -2):
#     print(i + 1, student)

# n = int(input("What's n? "))
# for i in range(n):
#     print("🐑" * i)

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock

if __name__ == "__main__":
    main()