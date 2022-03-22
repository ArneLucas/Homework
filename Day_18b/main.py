import colorgram as cg

# rgb_colors = []
# colors = cg.extract("image.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()
timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()

color_list = [(42, 104, 172), (234, 206, 114), (228, 151, 85), (187, 47, 75), (118, 88, 47), (231, 117, 145),
              (111, 108, 188), (215, 60, 78), (54, 178, 111), (114, 185, 137), (120, 177, 214), (200, 17, 41),
              (115, 170, 35), (33, 57, 112), (221, 53, 47), (25, 142, 108), (181, 168, 224), (155, 224, 193),
              (28, 163, 174), (85, 35, 39), (32, 45, 83), (232, 167, 181), (77, 36, 34), (234, 171, 162), (111, 43, 38),
              (152, 208, 221)]

timmy.seth(225)
timmy.fd(300)
timmy.seth(0)
num_of_dots = 100

for dot_count in range(1, (num_of_dots + 1)):
    timmy.dot(20, random.choice(color_list))
    timmy.fd(50)

    if dot_count % 10 == 0:
        timmy.seth(90)
        timmy.fd(50)
        timmy.seth(180)
        timmy.fd(500)
        timmy.seth(0)

screen = t.Screen()
screen.exitonclick()
