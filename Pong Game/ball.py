import random
import time
from turtle import Turtle
SHAPE="circle"
DISTANCE=0.1
SPEED_INCREMENT=0.01
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color("blue")
        self.penup()
        self.goto(0,0)
        self.turtlesize(0.8)
        self.xmove=DISTANCE
        self.ymove=DISTANCE

    def move(self):
        self.goto(self.xcor()+self.xmove,self.ycor()+self.ymove)
    def bounce_y(self):
        self.ymove=-(self.ymove)
    def bounce_x(self):
        self.xmove=-(self.xmove)
        self.ymove=self.ymove
        self.increment_speed()
    def reset_to_center(self):
        self.xmove=-self.xmove
        self.ymove=-self.ymove
        self.reset_speed()
        self.home()

    def increment_speed(self):
        sign_x=self.xmove/abs(self.xmove)
        self.xmove=self.xmove+SPEED_INCREMENT*sign_x
        sign_y=self.ymove/abs(self.ymove)
        self.ymove=self.ymove+SPEED_INCREMENT*sign_y

    def reset_speed(self):
        sign_x=self.xmove/abs(self.xmove)
        self.xmove=DISTANCE*sign_x
        sign_y=self.ymove/abs(self.ymove)
        self.ymove=DISTANCE*sign_y








