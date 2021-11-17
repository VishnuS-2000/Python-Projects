import time
from turtle import Turtle
SHAPE="circle"
COLOR="#2940D3"
JUMPHEIGHT=250
STEP=0.3
class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_wid=1.5,stretch_len=1.5)
        self.color(COLOR)
        self.goto(-40,0)
        self.activate_jump=False
        self.step=STEP
        self.success=False
        self.move_speed=STEP

    def spin(self):
           self.setheading(self.heading()+1)
    def move(self):
            self.spin()
            if(self.activate_jump):
                    self.goto(self.xcor(), self.ycor() + self.step)
                    if(self.ycor()>JUMPHEIGHT):
                        self.step=-STEP
                    elif(self.ycor()<0):
                        self.step=STEP
                        self.activate_jump=False
                        self.success=True


    def jump(self):
        self.activate_jump=True
    def update_speed(self):
        self.move_speed+=0.00001






