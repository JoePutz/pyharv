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

import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    #we get csv.reader() from import csv. this will just read the file
    for row in reader:
        students.append({"name": row[0], "home": row[1]})
    #can also be written
    #for name, home in reader:
        #students.append({"name": name, "home": home})
        #The name, home division will automatically split the file row into those two parts in order

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

#If we had the csv file automatically divide the info for us
#The FIRST LINE would read: name,home
#Then we could rewrite the above code as follows
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
#DictReader reads the rows as dictionaries intead of just plain reading it
#And the first row is just going to be the titles of the columns


import csv
name = input("What's your name? ")
home = input("what's your home? ")

with open("students.csv", "a") as file:
    #the a is for appending, not just reading
    writer = csv.writer(file)
    writer.writerow([name, home])
    #could also use writer = csv.DictWriter(file, fieldnames=["name", "home"])
    #writer.writerow({"name": name, "home": home})

#What's the difference? with .writer() it must be done left to right in order.
#with DictWriter the information will be formatted as fieldnames regardless of the order of info provided

import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
#The above would create a gif. Looping between multiple images when placed at the end of the terminal to call the program
