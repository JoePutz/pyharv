#called regexes

email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")
#A quick check if the email written is actually an email

#another better method, as above is bad

username, domain = email.split("@")

if username and "." in domain:
    #if username exists AND . is in the domain
    print("Valid")
else:
    print("Invalid")

#Let's check if it's from a university email:
if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

#Of course this is still able to be beaten. We can keep iterating, but that's a lot of work. 

#So what to do? The 're' library does a lot of this stuff for us. 

import re

email = input("What's your email? ")

if re.search(r"^.+@.+\.edu$", email):
    #this is what the above says: search through email, but will use a \ at some point. in the string it should have the pattern: it must start with at least 1 character, @, at least 1 character, ends in .edu
    print("Valid")
else:
    print("Invalid")

#re.search uses these special symbols:
#. any character except newline
#* 0 or more repetitions
#+ 1 or more repetitions
#? 0 or 1 repetition
#{m} m repetitions
#{m,n} m thru n repetitions
#\ is used to indicate you're not using the above for a special sequence(.com uses ., which as above could mean any character)
#r"" is used to indicate that the \ is going to be used in the quotes and isn't going to start a new line
#^ matches the start of the string
#$ matches the end of the string
#[] inside these brackets is something you're looking for
#[^] anything except what's inside the bracket 
# () groups things in the parenthesis
# | or


#if re.search(r"^[^@]+@[^@]+\.edu$", email):
    #So at the start, have at least one but can be more symbols that cannot be the @, @, more symbols that must be more than 1 and cannot be @, end with.com

#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#putting in all acceptable characters: a thru z, A thru Z, 0 thru 9, and _
#alphanumeric + _ is super common so there's a shortcut to get it. \w
#if re.search(r"^\w+@\w+\.edu$", email):
#\w is called a "word character" which is alphanumeric + _

#\d = decimal digit 0-9
#\D = not a decimal digit
#\s = whitespace character 
#\S not a whitespace character
#\w = word character: letters, numbers, _
#\W = not a word character

#What if we want to make an or?
#if re.search(r"^\w+@\w+\.(edu|com|net)$", email):

#FLAGS
#You can also add additional info
#re.IGNORECASE = ignores case
#re.MULTILINE = takes multiple lines. 
#re.DOTALL = configure the . to recognize everything

#if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
#So this is like above, except it does not care about case sensitivity

#if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
#So what this says. After the @ check if there are letters followed by a . If that exists there will be 0 or 1 of them. Then go to more symbols.edu
#Remember the ? is 0 or 1 so the stuff in the () before the ? is 0 or more times

import re

name = input("what's your name? ").strip()
matches = re.search(r"^(.+), ?(.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
    #OR
    #name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")


#OR
if matches := re.search(r"^(.+), ?(.+)$", name): #:= walrus operator when you do if and assign at the same time
    name = matches.group(2) + " " + matches.group(1)

#what if we want to extract info from stuff?


url = input("URL: ").strip()
#We get a url of someone's twitter, which is twitter.com/username. So how to get username?
print(url)
username = url.replace("https://twitter.com/", "")
#Above is saying replacing twitter.com with nothing. 

#This could be a problem with the url not being 100% accurate, like www or some other thing out of the set pattern. Like if someone answers the input in a complete sentence

username = url.removeprefix("httpe://twitter.com/")
#This will only just work if it removes the prefix, or the start of the string is as listed.

username = re.sub(r"^(https?:)?(www\.)?twitter\.com/", "", url)
#substitutes twitter.com with "" from the url
#above regex made http(s) and www. as optional in the url

#lets check if good first

url = input("URL: ").strip()

re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))
#this will check if the url is correct before it stores anything. but if there 

if matches := re.search(r"^https?://(www\.)?twitter\.com/([a-z0-9_]]+)$", url, re.IGNORECASE):
    print(f"USername:", matches.group(1))

