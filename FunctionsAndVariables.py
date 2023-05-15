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

first, last = name.split(" ")
#splits name into 2 parts if they inputed a first and last name. Named them first and last
print("hello, " + first)