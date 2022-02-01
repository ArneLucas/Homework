import random

random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random()
print(random_float)

# random float between 0 and 5:

# My way:
# random_1_5 = random.randint(0,4)+random.random()
# print(random_1_5)

# Course says:
# random_1_5 = random.random() * 5
# print(random_1_5)
