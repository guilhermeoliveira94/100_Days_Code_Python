# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 36)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
my_screen = t.Screen()
tim.speed("fastest")
tim.hideturtle()

color_list = [(239, 229, 84), (191, 11, 71), (206, 158, 98), (113, 179, 205), (162, 170, 35), (26, 117, 170),
              (212, 137, 168), (161, 71, 37), (9, 35, 83), (32, 135, 74), (121, 181, 138), (232, 70, 41), (239, 221, 5),
              (210, 85, 131), (80, 20, 77), (12, 58, 35), (238, 162, 190), (176, 45, 90), (15, 44, 125), (7, 102, 64),
              (121, 38, 23), (22, 167, 197), (7, 87, 97), (147, 207, 218), (161, 209, 186), (80, 154, 93),
              (239, 173, 154), (92, 40, 23), (176, 185, 219), (113, 97, 8), (101, 121, 167), (254, 3, 88)]

# start the motion of the turtle
tim.penup()
tim.setpos(-250, -250)
position = tim.pos()
m = -250
for i in range(11):
    for j in range(11):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.forward(50)
    m += 50
    tim.setpos(-250, m)

my_screen.exitonclick()
