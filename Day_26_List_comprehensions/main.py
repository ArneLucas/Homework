# List Comprehension
# old
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)
# new
new_list2 = [n+1 for n in numbers]
print(new_list2)

# new_list = [new_item for item in list]

# with condition:
# new_list = [new_item for item in list if test]