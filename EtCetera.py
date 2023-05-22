#a bunch of other stuff

#docs.python.org/3/library/....

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)


#OR I could do it
houses = set()
for student in students: 
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
#Set apparently takes only 1 of each value

balance = 0

def main():
    print("Balance", balance)
    deposit(100)
    withdraw(50)
    print("Balance", balance)

def deposit(n): 
    balance += n

def withdraw(n):
    balance -= n

if __name__ == "__main__":
    main()
#The above gives UNBOUND VARIABLE
#Even if balance was within main it still wouldn't work. 

#So how to fix? 

balance = 0

def main():
    print("Balance", balance)
    deposit(100)
    withdraw(50)
    print("Balance", balance)

def deposit(n): 
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()


class Account: 
    def __init__(self): 
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n
    
    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", balance)

#This of course also works. When to use one or the other? global is good for smaller programs, used sparinglyh
#classes w/ their own implementation are much better for more complicated code. As all the important info is in one central location

#constants
#when decladed constant it cannot be changed. Python doesn't really enforce it. But it does have a means of indication somethign shouldn't be changed

#What if you just want to meow 3 times? But you want to make it so that no one can change that value?
MEOWS = 3

for _ in range(MEOWS):
    print("meow")


class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()
#This should access the class constant MEOWS = 3 to meow 3 times. 

#IMORTANT the all caps is not enforced. it's an honor's system really. It means DO NOT TOUCH but doesn't prohibit touching, apparently

#TYPE HINTS
#Code to check if you're using the right types and information and whatnot. 
#mypy is the popular one. 
#pip install mypy
#mypy.readthedocs.io

def meow(n):
    for _ in range(n):
        print("meow")

number = input("Number: ")
(number)

#This above won't work, because input is a string. Not an int

#how to avoid an error?
def meow(n: int):
    for _ in range(n):
        print("meow")
    
number = input("Number: ")
meow(number)
#This would indicate taht n should be an integer. But we can do more. 
#in the terminal use mypy EtCetera.py 
#For our actual tests Im going to use testmypy.py

#Anyway, that showed that the error in the file had meow incompatible with the str

#Or I can write this

number: int = input("Number: ")
meow(number)
#This doesn't FIX the problem. It is just also allows mypy to find the error a difrerent way

meows: str = meow(number)
print(meows)
#This is silly! It will print: meow, meow, meow, None. 
#Why None? 
#Becuz meow doesn't return anything. It just prints meow. So printing what meow returns it will print none after all the meow prints

#How to avoid this? 

def meow(n: int) -> None: 
    for _ in range(n):
        print("meow")

#Then if we use mypy it will indicate that meow returns None. So it will know something's wrong and put up the error

#OR

def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
#This will all work

#docstrings
#standardizes documentation
#pep.python.org/pep-0257

def meow(n: int) -> str:
    """Meow n times."""
    #The above is the documentation that is the convention. 
    """
    It can also work like this. With the three quotation marks above and below
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    This is all a 3rd party format. Not technically python, but it it the standard.
    """


#CAn I make meow that uses command line inputs? 
import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else: 
    print("usage: meows.py")

#The above gets pretty complciated with the whole -n 8 to make 8 meows and having the intonation of 

#how to make it easier to do command line stuff?
#argparse
#docs.python.org/3/library/argparse.html

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
#descript comes up when using -h to help when using on the command line
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
#help comes up when using -h to help when using on the command line
#default is a default value
#type indicates what type the info should be
args = parser.parse_args()
#This imports sys and figures out all of that for me.

for _ in range(int(args.n)):
    print("meow")


#unpacking
first, _ = input("What's your name? ").split(" ")
print(f"hello, {first}")
#the above is usual unpacking, let's do more complicated stuff


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) *29 + knuts

print(total(100, 50, 25), "Knuts")

#That works

#or we could: 

coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]))
#This works
print(total(coins), "Knuts")
#This does not work. It will just pass all the numbers in coins as a list to galleons

print(total(*coins), "Knuts")
#This does work. * means preserving order to putting into the function
#It has to match up. list much match the number of parameters needed for the funct

print(total(galleons=100, sickles=50, knuts=25), "Knuts")
#this works, obviously

coins = {"galleons": 100, "sickles": 50, "knuts": 25}
#if you have this to use it goes:
print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
#That's pretty verbose but it works
#Can we make it faster? yeah
print(total(**coins), "Knots")
#this works, it passes in 3 values w/ names

#* and ** is also when something takes a variable number of values

def f(*args, **kwargs):
    #This means some number of arguments, and some number of keyword arguments
    print("Positional:", args)
f(100, 50, 25)
#The above works. It's just 3 arguments
f(galleons=100, sickles=50, knuts=25)
#The above works. It's just 3 named/keyword arguments
#docs.python.org/3/library/functions.html#print
#we can see in the documentation of print, it starts with print(*objects) meaning it takes any number of objects, and it will print each of them.
