# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# Simple function:

def greet():
    print(f"Hello")
    print("Good morning")
    print("Would you like some coffee?")

greet()

# Function with input (parameter/argument):

def greet_with_name(name): # --> 'name' is parameter
    print(f"Hello, {name}")
    print("Good morning")
    print("Would you like some coffee?")

greet_with_name("Mel") # --> 'Mel' is argument

# Function with more than 1 input:

def greet_with_name_and_breakfast(name,breakfast): # --> postional arguments: parameter1,parameter2
    print(f"Hello, {name}")
    print("Good morning")
    print(f"Would you like some {breakfast}?")

greet_with_name_and_breakfast("Mel", "coffee") # --> argument1, argument2

def my_function(a,b,c):
    print(f"Do something with {a}")
    print(f"Then do something with {b}")
    print(f"Finally do something with {c}")

my_function(3,2,1)  # --> postional arguments: order = 3, 2, 1
my_function(c=3,b=2,a=1) # --> keyword arguments: order = 1, 2, 3