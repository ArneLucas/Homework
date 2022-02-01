# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Angela.lower() -> angela
# Angela.count("a") -> 1
# lo_case_name = Angela.lower()
# lo_case_name.count("a") -> 2

lo_case_names = name1.lower() + name2.lower()
first_digit = lo_case_names.count("t") + lo_case_names.count("r") + lo_case_names.count("u") + lo_case_names.count("e")
second_digit = lo_case_names.count("l") + lo_case_names.count("o") + lo_case_names.count("v") + lo_case_names.count("e")

love_score = int(str(first_digit)+str(second_digit))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you go alright together.")
else:
    print(f"Your score is {love_score}.")