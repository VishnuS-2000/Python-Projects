import random
from turtle import Turtle
from obstacles import Pole
class Platform(Turtle):
    def __init__(self):
        super().__init__()
        self.obstacle_types=["pole"]
        self.obstacles=[]
        self.shape("square")
        self.shapesize(stretch_wid=0.4,stretch_len=40)
        self.penup()
        self.color("#1B262C")
        self.goto(0,-20)
        self.create_new_obstacle=False
        length=random.randint(2,8)
        start=(300,self.ycor()+length*(21/2))
        self.previous_obstacle=Pole(position=start,length=length)
        self.obstacles.append(self.previous_obstacle)
        for i in range(0,2):
            self.create_obstacle()

    def create_obstacle(self):
            type=random.choice(self.obstacle_types)
            if(type=="pole"):
                length=random.randint(2,8)
                y_coordinate=self.ycor()+length*(21/2)

                new_position=self.find_position(y_coordinate,start=120)

                new_obstacle=Pole(position=new_position,length=length)

                self.obstacles.append(new_obstacle)
                self.previous_obstacle=self.obstacles[len(self.obstacles)-1]

    def move(self):
        if(self.create_new_obstacle and len(self.obstacles)<5):
            self.create_obstacle()
            self.create_new_obstacle = False
        for obstacle in self.obstacles:
            obstacle.move()
            if(obstacle.xcor()<-420):
                obstacle.hideturtle()
                self.obstacles.remove(obstacle)
                self.create_new_obstacle=True
    def find_position(self,position_y,start=200):
        current_x=self.previous_obstacle.xcor()+random.randint(start,300)
        current_y=position_y
        return (current_x,current_y)
    def update_speed(self):
        for obstacle in self.obstacles:
            obstacle.move_speed+=0.00001













