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

#Property: it allows us to make classes act in specific ways that can't be messed with as easily. 
#Stops people getting around the requirements of a class
#@property

class Student:

    # Getter: gets attribute
    @property
    def house(self):
        return self._house
        #Ths _house separates it from self.house directly. self.house will be used in init
    
    #Setter: sets attribute
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    #So you no longer need to make errors for such values through the init or by direct change
    #REMEMBER to only use _key in the setter and getter. But it can be done, but really it can be circumvented in python by doing it elsewhere. But dont!

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

#@classmethod: a method that will not have access to self. 
#How does this work? Learning. We're going to use the Sorting Hat as an example
import random

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

hat = Hat()
hat.sort("Harry")

# a lot of the above is unnecessary. Let's clean it up

class Hat: 
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")

#And that's it. we don't need to create new hats. We just can refer to the class and the function in that class to use 
#we use cls instead of self. cls just is teh short for class. cls.function() works so long as the function exists w/in the class
#It creates the class as a container, because we aren't goign to be making more sorting hats. Just darwing on the function therein


#So with all that info lets redo Student

class Student:
    def __init__(self, name, house): 
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    #So this is the method for creating an object of the current class

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()

#Inheritance. Making it so that a class takes the traits from a different higher class
#called parents and descendants

class Professor:
    def __init__(self, name, subject):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.subject = subject
#This is very similar to student. A lot of the same attributes between it and student.

#So how to fix that? 

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard): 
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

#super().__init__() means, go to the super class (in this case it is Wizard) and use it's init function

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Potions")
#all the above will work. albus is just a wizard. 

#operator overloading
#taking common symbols like + or - and make them mean something else. 
#like in regex or when joining two strings together. 

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

galleons  = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)
print(total)

#That all works. 
#But wouldn't be easy if I could just say potter + weasley = total? and it just worked?
#We can do that.

#object.__add__(self, other)

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
#This should make total = potter + weasley 

#all the opperators can be found: docs.python.org/3/reference/datamodel.html#special-method-names
