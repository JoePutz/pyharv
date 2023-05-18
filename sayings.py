def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()
#What this means?
#If I imported anything from this file. Even if I only tried to import 1 method, it would stillr read the entire file
#therefore if I just wrote main() at the end, if I import it would print everything including the hello world, goodbye wolrd stuff
#This __name__ keeps this from happening. only works if run from the command line.