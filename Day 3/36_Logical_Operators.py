# Logical operators:
# and
#   A and B -> A ánd B have to be true
# or
#   A or B -> A or B has to be true
# not
#   not E -> E has to be False

a = 12
a > 10 and a < 15 # True
a > 10 and a > 15 # False

a > 10 or a > 15 # True
a > 10 or a < 15 # True (both true)

not a > 15 # True
