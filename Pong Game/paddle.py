from turtle import Turtle

SHAPE="square"
LENGTH=3
COLOR="white"
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.setheading(90)
        self.paddle_start = (self.xcor(), self.ycor()+2.5)
        self.paddle_end = (self.xcor(), self.ycor()-2.5)

    def up(self):
            if(self.ycor()<=250):
                self.forward(20)
    def down(self):
            if(self.ycor()>=-250):
                self.backward(20)










