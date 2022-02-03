# calculate the total of the even numbers between 0 and 100:

total_of_even_numbers = 0

for number in range(2,101,2):
    total_of_even_numbers += number
print(f"The total of even numbers is {total_of_even_numbers}")

# another way:

total_of_even_numbers2 = 0
start_at = int(input("Start at:\n"))
end_at = int(input("End at:\n"))+1
for number in range(start_at,end_at):
    if number % 2 == 0:
        total_of_even_numbers2 += number
print(f"The total of even numbers is {total_of_even_numbers2}")