import random
import turtle
import colorgram
from turtle import Turtle,Screen

timmy=Turtle()
turtle.colormode(255)


def generate_colors():
    colors=colorgram.extract('hirstpainting2.jpg',30)
    rgbcolors=[]
    for color in colors:
        if(abs(color.rgb.r-color.rgb.g)>8 and abs(color.rgb.g-color.rgb.b)>8):
            newcolor=(color.rgb.r,color.rgb.g,color.rgb.b)
            rgbcolors.append(newcolor)
    return rgbcolors




def draw_painting(x_dots,y_dots,dot_size,gap_size):
    screen=Screen()
    timmy.penup()
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)
    timmy.pendown()
    number_of_dots=x_dots*y_dots

    for i in range(1,number_of_dots+1):
        timmy.dot(dot_size,random.choice(colors))
        timmy.penup()
        timmy.forward(gap_size)
        timmy.pendown()
        if(i % 10==0):
            timmy.penup()
            timmy.setheading(90)
            timmy.forward(gap_size)
            timmy.setheading(180)
            timmy.forward(gap_size*x_dots)
            timmy.setheading(0)
            timmy.pendown()
    screen.exitonclick()


colors=generate_colors()

timmy.hideturtle()
screen=Screen()

timmy.speed("fastest")

draw_painting(x_dots=10,y_dots=10,dot_size=30,gap_size=50)
