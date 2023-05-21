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
