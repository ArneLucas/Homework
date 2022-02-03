# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇


# can't use sum() or len()

def av_height_func(student_heights):
  total_height = 0
  num_of_heights = 0
  for height in student_heights:
      total_height += height
      num_of_heights += 1

  ave_height = round(total_height / num_of_heights)
  print(f"The average student height is {ave_height}")

av_height_func(student_heights)

# av_height_func([150, 140, 130, 120, 110, 100])