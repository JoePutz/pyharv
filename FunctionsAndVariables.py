#commandline interface = CLI
print("hello, world")

name = input("What's your name? ")

name = name.strip().title()
#removes unnecessary " ". 
#capitalizes the first letter of each word

print("hello, " + name)
print("hello,", name)
print(f"hello, {name}")
#all are the exact same thing
#Notice the second does not need a " " after 'hello,' apparently the (variable1, variable 2) method puts a " " automatically 
#Notice 3rd requires f in front of string to indicate 

#print(*objects, sep=' ', end='\n', file=sys.stout, flush=False)

print("hello, \"friend\"")
#allows printing of "" within the print

#first, last = name.split(" ")
#splits name into 2 parts if they inputed a first and last name. Named them first and last
#print("hello, " + first)


#int is an integer, no decimal point
# + - * / %

#INTERACTIVE MODE
#in terminal type python3 to get interactive mode
#Ctr + D gets out of interactive mode

#x = 1
#y = 2

#z = x + y

#print(z)
#shows 3


x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)
#The above wont work, because it is strings. 
#Must convert data to integers thru int()

z = int(x) + int(y)
print(z)

#also done with this: 
# x = int(input("What's x? "))
# y = int(input("What's y? "))
#print(x + y)

#float: floating point value

x = float(input("what's x? "))
y = float(input("What's y? "))
print(x + y)
#This gives a decimal answer always

#what if we want to round it?

z = round(x + y)

#what if we want to use , in our big numbers. like instead of 1000000 we have 1,000,000

print(f"{z:,}")
#Does all the ,s automatically

z = round(x /y, 2)
#rounds to the nearest hundredths place or 2 decimal points

print(f"{z:.2f}")
#Exact same thing, means of rounding to the nearest 2 decimal spaces



#Methods we're defining a means of saying "Hello"

def hello(to="world"):
    #The to="world" means that if there's no argument it defaults to world
    print("hello,", to)

name = input("What's your name? ")
hello(name)

#python reads top to bottom. So if you call a function that hasn't been defined yet it won't work.
#However the following does work, because main() is called at the bottom

def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)

main()
