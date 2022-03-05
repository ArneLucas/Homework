# import another_module

# # print(another_module.another_variable)


# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle") # change shape to turtle
# timmy.color("coral") # change color to coral
# timmy.forward(100) # moves timmy 100 paces forward

# my_screen = Screen()
# print(my_screen.canvheight) # canvheight is an attribute of the my_screen object

# my_screen.exitonclick() # exitonclick is a method of the my_screen object

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Picachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)