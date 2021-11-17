import random
import turtle
from turtle import Turtle
COLORS=["#E02401","#FF0075","#150050","#F0A500","#1C7947","#1E3163"]
SHAPE="square"
DISTANCE=0.08
class Pole(Turtle):
    def __init__(self,position,length):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.shapesize(stretch_wid=length,stretch_len=1)
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.move_speed=DISTANCE
        self.goto(position)

    def move(self):
        self.goto(self.xcor()-self.move_speed,self.ycor())



