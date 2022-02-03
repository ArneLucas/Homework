# FizzBuzz
# devisable by 3: Fizz
# devisable by 5: Buzz
# devisable by 3 and 5: FizzBuzz

start_at = int(input("Start at:\n"))
end_at = int(input("End at:\n"))+1
for num in range(start_at,end_at):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)