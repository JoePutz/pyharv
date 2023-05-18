#Testing to see if your code works. 
#We test using the convention test_{the name of the file being tested}
#so test_UnitTest.py

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
    print(hello("David"))

def square(n):
    return n + n

def hello(to="world"):
    #print("hello,", to)
#The above is hard to test. Why? Because tests don't really do print easily, they're better with return
#It is better to make it a return and then change the main to print what is returned. 
    return f"hello, {to}"
#This would work much better

if __name__ == "__main__":
    main()


#You can make a package of all files in a folder. 
#Not going to do it here. But as an example. I can make a folder called test
#In that folder I can make all my single test files
#I can use 'pytest test' in the command line to test every file in the test folder

