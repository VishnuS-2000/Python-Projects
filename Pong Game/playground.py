from turtle import Turtle
COLOR="white"
def draw_lines():
    timmy=Turtle()
    timmy.penup()
    timmy.setheading(90)
    timmy.color(COLOR)
    timmy.width(3)
    timmy.hideturtle()

    for i in range(-280,280,20):
        timmy.penup()
        timmy.goto(0,i)
        timmy.forward(10)
        timmy.pendown()
        timmy.forward(10)

