from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",15,"bold")

class ScoreBoard(Turtle):
    def __init__(self):
        file = open("data.txt", mode="r")
        super().__init__()
        self.score = 0
        self.high_score = int(file.read())
        self.hideturtle()

        self.goto(0, 260)
        self.color("white")
        self.write(f"Score:{self.score} High Score:{self.high_score}", False, align=ALIGNMENT, font=FONT)


    def refresh_score(self):
        """Updates the Score"""
        self.goto(0, 260)
        self.score=self.score+1
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", False, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over",align=ALIGNMENT,font=("Courier",18,"bold"))
    #     self.goto(0,-30)
    #     self.write("Press Space to Restart",align=ALIGNMENT,font=("Courier",12,"bold"))
    def reset_scoreboard(self):
        """Resets scoreboard"""

        if(self.score>self.high_score):
            self.high_score=self.score
            with open("data.txt","w") as file:
                file.write(str(self.high_score));
        self.score=0
        print(self.high_score)
