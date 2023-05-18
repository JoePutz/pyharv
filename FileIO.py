#File I/O is storing informatino in various ways without using as much memory
#names = []

#for _ in range(3):
#    names.append(input("What's your name? "))

#for name in sorted(names): 
#    print(f"hello, {name}")

#So what happens if we want to add names to a file? 

name = input("What's your name? ")

#file = open("name.txt", "w")
#opens a file and allows you to write in the file
#file.write(name)
#file.close()

#This will overwrite the beginning of the file with what you write here. 
#It doesn't add to it. 
#It OVERWRITES

#What if we want to addd to the file, not overwrite it? 
with open("name.txt", "a") as file:
    file.write(f"{name}\n")
#The \n is to make each new additiona a different line
#This WITH method also closes the file automatically when done

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello," , line.rstrip())
#So this and above we're reading the file, then printing each line as hello, {name} in the file

#we can shorten this
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())

#What if we want to sort it? Well then the above method of shortenign isn't really that good. 
#You can't read and automatically write as well as sort

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        #rstrip() strips the new line at the end of each of the lines

for name in sorted(names):
    print(f"hello, {name}")

#OR

with open("names.txt") as file:
    for line in sorted(file):
        print(f"hello,", line.rstrip())
#This is more compact but it does make it more difficult to make more precise changes

#What if we want to reverse the sorted file? so Z to A?
#for name in sorted(names, reverse=True):

#names.csv: comma separated file. I don't know what the v stands for

with open("students.csv") as file:
    for line in file: 
        row = line.rstrip().split(",")
        #splits the string into pieces separated by the comma
        print(f"{row[0]} is in {row[1]}")

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
        #This can be done to make it neater. labeling what is being called

#Sort by csv values?

students = []

with open("students.csv") as file:
    for line in file: 
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        student.append(student)

for student in sorted(students): 
    print(f"{student['name']} is in {student['house']}")

#but we can do it even better

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
#so sort by what comes out of the key=get_name, if we instead had a key= get_house that returned the house
#it would sort by the alphabetical houses

#we can even do a nameless function
#key=lambda student: student["name"]
#What the above says? 
#using lambda in place of an actual named function
#for every student, return the student[name]

#what happens if csv has a comma in the information and not just to separate values but as part of the value?
 