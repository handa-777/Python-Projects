import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(239, 151, 52), (168, 50, 68), (22, 109, 164), (42, 50, 115), (231, 80, 57), (212, 133, 173), (117, 181, 212), (141, 98, 47), (106, 192, 175), (219, 61, 108), (5, 158, 88), (93, 172, 60), (17, 172, 201), (242, 204, 67), (125, 38, 64), (2, 92, 114), (233, 175, 9), (152, 210, 221), (2, 119, 60), (247, 205, 2), (69, 46, 56), (76, 47, 43), (82, 51, 48), (19, 37, 83), (232, 169, 184), (155, 213, 184)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()