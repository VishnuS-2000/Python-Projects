from turtle import Turtle

COLOR="white"
FONT=("Arial",24,"bold")
ALIGNMENT="center"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.r_score=0
        self.l_score=0
        self.goto(-50,250)
        self.write(self.l_score,align=ALIGNMENT,font=FONT)
        self.goto(50,250)
        self.write(self.r_score,align=ALIGNMENT,font=FONT)
    def refresh_score(self,player):
        if(player=="left"):
            self.l_score+=1
        else:
            self.r_score+=1

        self.clear()
        self.goto(-50,250)
        self.write(self.l_score,align=ALIGNMENT,font=FONT)
        self.goto(50,250)
        self.write(self.r_score,align=ALIGNMENT,font=FONT)

