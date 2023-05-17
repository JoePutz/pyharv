#Exceptions are problems and errors and whatnot

#print("Hello, world)
#Syntax error: you messed up the writing so you need to fix the writing

x = int(input("What's x? "))
print(f"x is {x}")
#if you input not an int:
#ValueError: the value doesn't work w/ what the program is trying to do

#try  and except are keywords to help w/ errors

try: 
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
#Have to pair these together. 

#NameError: When the values in your code aren't defined well, or you're doing something wrong.
#What if print x was at the bottom, so if x is nothing you'd get the NameError

try: 
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")



while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")
#This will keep prompting to ask what is x? until a correct answer is given.

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
#This will create a loop of just what's x? but doesn't say "not an int", 
#Pass will just jump back to the try
main()

#raise: Python allows us to raise errors. with this thing. But that's for a later lesson. 