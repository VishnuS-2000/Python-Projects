from turtle import Turtle
COLOR="blue"
def draw_boundary():
    timmy=Turtle()
    timmy.color(COLOR)
    start=(-293,292)
    timmy.penup()
    timmy.goto(start)
    timmy.pendown()
    timmy.width(3)
    timmy.hideturtle()
    for i in range(1,5):
        timmy.forward(580)
        timmy.right(90)