with open("/Users/lucas/Desktop/demo.txt") as file:
    contents = file.read()
    print(f"Absolute path: {contents}")

with open("../../../../../demo.txt") as file:
    contents = file.read()
    print(f"Relative path: {contents}")

