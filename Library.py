#libraries/modules bunch of data and functions you can add to your program easier

#docs.python.org/3/library/... (whatever the library you want to use)

import random

coin = random.choice(["heads", "tails"])
#get a random answer from the list: heads or tails
print(coin)

#if you only wanted the choice function and nothing else: 
#from rnadom import choice
#now you can just use choice instead of random.choice
#coin = choice(["heads", "tails"])

number = random.randint(1, 10)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card)

import statistics
#this should usually be the top of the file

print(statistics.mean([100, 90]))

#command-line arguments
#allows us to provide arguments when executing it at the command line. so when calling a program in the terminal you can add additional info to the process of just calling the program

import sys

print("hello, my name is", sys.argv[1])
#argv[1] is the list of what is called in the terminal. So, this wouuld be what is the input read out after the initial program is called.

#this could come out w/ an error if nothing is in list

if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) >2:
    print("too many arguments")
else:
    print("hello my name is", sys.argv[1])

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
#sys.exit just ends the program. It will print the thing

#what if we want to put over every name at the prompt
#

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
#this is a slice starting at 1 (instead of 0) and going to the end. 
#sys.arg[1:-1] would go to the second to last element.

#packages
#third party libraries that can be installed on our server or machine
#module implemented in a folder. 

#pypi.org
#is the site that has a lot of these packages.

#pypi.org/project/cowsay
#how to download it? 
#pip is a program that allows us to quickly download packages

#how to install one? pip install x in the terminal
#I just did pip install cowsay

import cowsay

if len(sys.argv) == 2: 
    cowsay.cow("hello, " + sys.argv[1])

if len(sys.argv) == 2:
    cowsay.trex("shut up, " + sys.argv[1])

#requests module can ask to use info from sites and stuff. Essentially APIs.

#application programing interface
#javascript object notation: is language agnostic. non-exclusive. EVeryone really uses it.

import requests
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("http://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) 
print(json.dump(response.json(), indent=2))
#This will convert the json into a python dictionary
#

o = response.json()
for result in o["result"]:
    print(result["trackName"])