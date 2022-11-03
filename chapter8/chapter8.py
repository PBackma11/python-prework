# def NAME_OF_FUNCTION(PARANMETERS):
    # these lines
    # belong
    # to the code block
    # for the function

from urllib import response


def hello():
    print("Hello")
# This has only been saved for later
# Next, we will show how to call it:
hello()
# In cases like calling this function within a function
# The function inside will be called first
print(hello())
# ------------------------------------------------------------
def hello1(name, age=55):
    print(f"Hello, {name}, you are {age} years old")
hello1(name="Kevin")
# Using parameters to input and call items to a function
# Default arguments must take place after non-default arguments

# --------------------------------------------------------------

def say_hello(name, age):
    print(f"Hello {name} you are {age} years old")

def say_goodbye():
    print("Goodbye")

def greet_back(feeling):
    if feeling=="good":
        print("Awesome, I feel good too!")
    elif feeling=="bad":
        print("I am so sorry")
    elif feeling=="stressed":
        print("Coding can be hard to learn")
    else:
        print("Well, have a good day!")

# Driver Code
while True:
    response=input("What do you want to do? Say Hello[H] Say Goodbye[G] Talk to me[T], Quit[Q]")
    if response.lower()=='q':
        say_goodbye()
        break
    elif response.lower()=='h':
        name=input("What is your name? ")
        age=input("What is you age? ")
        say_hello(name, age)
    elif response.lower()=='g':
        say_goodbye()
    elif response.lower()=='t':
        f=input("How are you today? ")
        greet_back(f)
    else:
        print("Invalid Input")