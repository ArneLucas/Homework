# Scope

value = 1

def increase_value():
    value = 2 # Local scope (actually a different variable) ## BAD IDEA to name your local variables the same as a global one
    print(f"value inside function: {value}") # = 2

increase_value()
print(f"value outside function: {value}") # = 1

# Local scope

def drink_potion():
    potion_strength = 2 # -> local variable
    print(potion_strength)

drink_potion() # prints "2"
# print(potion_strength) -> returns error, because the variable only exists in the function

# Global scope

player_health = 100 # -> global variable

def drink_potion():
    potion_strength = 2
    print(player_health)

# A variable created in a function is only available in that function (local scope)
# But if you create a variable within an if-block, while- or for-loop it doesn't count as a local scope (global scope)

enemies = 1 # Global scope

def increase_enemies():
    global enemies # takes the global variable into the function and allows you to modify it
    enemies += 1 # with global statement, you can now change the global variable. However, it is advised against. 
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# This is a better way, so you don't change the global variable.
enemies = 1 # Global scope

def increase_enemies():
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants
# ALL UPPERCASE 
PI = 3.14159
URL = "https://www.google.com"
