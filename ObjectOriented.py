#Python can also be function oriented rather than object. But it can do both. 

def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()

#THat worked, but what if we just want to create a student, and then just call taht?

def main():
    name, house = get_student()
    print(f"{name} from {house}")
    #Can also be:
    #student = get_student()
    #print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house
    #Can also be return (name, house) if you want to make it easy to see it as together

#This created a tuple. it's like a list that can't be changed. 
#So once you get the info it cannot be changed
#What if we want it to be changed?
#We can make it a list. That's easy, just write it as return [name, house] brackets means list

#We can also make a dictionary

def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student
    #OR
    #name = input("Name: ")
    #house = input("House: ")
    #return {"name": name, "house": house}

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")
#This shoows what we could do to change so long as it's a list or a dictionary. NOT TUPLES

#CLASSES a mold that can define and get named, that defines it as you want
#Essentially be able to create your own objects that don't necessarily follow the rules of tuples, lists, or dictionaries

class Student:
    ...

def get_student():
    student = Student()
    #classes have attributes that allows you to show what is inside it. 
    student.name = input("Name: ")
    student.house = input("House: ")
    #So this one has a name and house attribute
    return student

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    #so that's the syntax. similar to javascript really. 

#Anytime you use a Class you're creating an Object. 
#So what is above?
#Student is an empty mold. It exists, but doen't necessarily have anything
#When you create one it is an Instance of a Class
#Then you can shape what's inside the individual class. 

#Classes are mutable, but you can make them immutable

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student
#Another way to set this up. 

#MEthods: classes come with functions inside classes that behave in a standard way
#__init__ is one. It defines what's in the class. initialization. 

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        #What does this mean? To initiate a student it requires itself, a new student, and a name, and a house
        #So every student is going to have a name and a house, always
        #self can technically be anything but just call it self. 
        #What self is, is the object that has just been constructed in memory

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

#What happens when we want to add limitaitons on Student? So there isn't errors like no names, or something
#raise exceptions and errors

class Student: 
    def __init__(self, name, house, patronus):
        if not name: 
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        if self.patronus == "Stag":
             return "huh"
        elif self.patronus == "Otter":
            return "ow"
        elif self.patronus == "Jack Russell terrior":
            return "woof"
        else:
            return "/"

def main():
    student = get_student()
    print(student)
    #This will print the __str__ bit
    print("Expecto Patronum!")
    print(student.charm)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

