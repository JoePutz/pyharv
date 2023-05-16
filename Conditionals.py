x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y: 
    print("x is less than y")
elif x > y: 
    print("x is greater than y")
#elif x == y: 
else:
    print("x is equal to y")

#elif is just if, but stops if the above questions were True. Mutually exclusive ifs
#else can be used to replace elif if there is no other options

score = int(input("Score: "))

if score >= 90 and score <= 100:
#if 90 <= score <= 100:
    print("Grade: A")
elif score >=80 and score < 90:
    print("Grade: B")
elif score >=70 and score < 80:
    print("Grade: C")
elif score >=60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

#You can also just get rid of the upper bound. Because of elif.
#if score >= 90:
#elif score >= 80:
#elif score >= 70:

x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

#Here's an example of using those functions
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#Pythonic version of above:
#def is_even(n):
    #return True if n % 2 == 0 else False

name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

#This can get unwieldy with more names. 

#THE MATCH case

#match name:
 #   case "Harry" | "Hermione" | "Ron":
  #      print("Gryffindor")
   # case "Draco":
    #    print("Slytherin")
 #   case _:
  #      print("Who?")
#Apparently match requires python 3.1, which I don't have. I have only python 3. Weird