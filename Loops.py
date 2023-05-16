x = 0

while x < 3:
    print("Meow")
    x += 1

for _ in [0, 1, 2]:
    #in range(3): Same as above but simpler. range(3) is the list of 0, 1, 2
    print("Meow")
#This works automatically in Python. i is automatically set as 0, in the list. 
# NOTE [] is LIST not ARRAY

#Fun thing. _ is used when the variable isn't ever going to be used again

print("meow\n" * 3, end="")
#\n breaks it by line
#end="" removes the last \n so there isn't an unnecessary line break

while True:
    n = int(input("What's n? "))
    if n > 0:
        break
#Neat trick, infinite loop with a break once we get what we want. Rather than asking to make certain n is positive every time.

for _ in range(n):
    print("meow")



def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()


students = ["Hermione", "Harry", "Ron"]

print(students[0])
#shows hermione

for student in students:
    print(student)

for i in range(len(students)):
    print(i + 1, students[i])
    #This will show 1 Hermione, 2 Harry, 3 Ron

#dict
#dictionary, data structure that lets you associate one value w/ another
#keys and values. Basically objects from JS. 

students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", 'Slytherin']
#This is over complicated. 

students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin"
}

print(students["Hermione"])
#gives Gryffindor

for student in students:
    print(student)
    #Shows the keys, so herm, har, ron, dra

for student in students:
    print(student, students[student], sep=", ")
    #herm, gryf
    #har, gryf
    #etc.

#lets be more complicated
students= [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"}, 
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
#This is a list of dictionaries

for student in students:
    print(student["name"], student["patronus"], sep=", ")


def main():
    print_column(3)
    print_row(4)
    print_square(3)

def print_column(height):
    for _ in range(height):
        print("#")
    #print("#\n" * height, end=""), same as above

def print_row(width):
    print("?" * width)

def print_square(size):
    #For each row in square
    for i in range(size):
        #print("#" * size)
        #For each brick in row
        for j in range(size):
            #print brick
            print("#", end="")
        #go to next line
        print()

main()