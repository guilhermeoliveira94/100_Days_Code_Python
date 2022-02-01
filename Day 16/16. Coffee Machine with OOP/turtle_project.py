from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")
timmy.speed(10)
for i in range(100):
    timmy.circle(5*i)
    timmy.circle(-5*i)
    timmy.left(i)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
