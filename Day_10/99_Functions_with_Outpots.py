def format_name(f_name, l_name):
    title_case_name = f_name.title() + " " + l_name.title()
    return title_case_name

f_name = input("What's your first name? ")
l_name = input("What's your last name? ")
formatted_name = format_name(f_name, l_name)

print(formatted_name)