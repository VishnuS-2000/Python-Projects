from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(340,360)
        self.score=0
        self.write(f"Score:{self.score}",align="center",font=("Ubuntu",18,"bold"))

    def refresh_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}",align="center",font=("Ubuntu",18,"bold"))

    def game_over(self):
        self.goto(0,250)
        self.write("Game Over",align="center",font=("Ubuntu",20,"bold"))