
# For loop

list_of_items = ["item1, item2"]
for item in list_of_items:
    print("Do something for each item")

start = 0
stop = 11
step = 2

for number in range(start, stop, step): # a = start, b = stop, c = step
    print("Do something for range times")

# While loop

something_is_true = ""

while something_is_true: #condition
    print("Do something for as long as something is true") # do this
    # when function is done, it checks if condition is still true

# when do you use a for loop, when do you use a while loop?

# if you want to do something which each item in a list, use a for loop

# if you want to do something until some condition is met, use a while loop (nr of repetitions is unknown)
# watch out for Infinite Loops!