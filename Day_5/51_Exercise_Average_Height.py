# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇


# can't use sum() or len()

total_height = 0
n = 0

for height in student_heights:
    total_height += height
    n += 1

ave_height = round(total_height / n)
print(f"The average student height is {ave_height}")