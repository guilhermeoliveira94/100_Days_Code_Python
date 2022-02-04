from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
tim.pensize(1)
tim.speed("fast")

# Draw a dashed line square:
# for _ in range(4):
#     for _ in range(10):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
#     tim.right(90)
#
# Draw a dashed line triangle:
# for _ in range(3):
#     for _ in range(10):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
#     tim.right(120)
#
#
# def draw_shape(num_sides):  # Draw a dashed line square triangle, square, pentagon, heptagon,(...):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(30)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 200):
#     tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     draw_shape(shape_side_n)

# Random Walk
# for _ in range(2000):
#     tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     tim.forward(30)
#     tim.setheading(random.choice([0, 90, 180, 270]))

# Draw a Spirograph
for i in range(360):
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.circle(100)
    tim.left(5)

screen.exitonclick()
