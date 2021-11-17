import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from playground import draw_lines
from scoreboard import ScoreBoard
screen=Screen()
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.bgcolor("black")

screen.tracer(0)

screen.listen()

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=ScoreBoard()
screen.onkey(key="Up",fun=r_paddle.up)
screen.onkey(key="Down",fun=r_paddle.down)
screen.onkey(key="w",fun=l_paddle.up)
screen.onkey(key="s",fun=l_paddle.down)
draw_lines()

game_is_on=True
while(game_is_on):
    screen.update()
    ball.move()
    if( ball.ycor()>295 or ball.ycor()<-295):
        ball.bounce_y()

    if(ball.distance(r_paddle)<50 and ball.xcor()>330 and ball.xcor()<350 or ball.distance(l_paddle)<50 and ball.xcor()<-330 and ball.xcor()>-350):
        ball.bounce_x()
    if(ball.xcor()<-400):
        ball.reset_to_center()
        scoreboard.refresh_score(player="right")
        screen.update()
        time.sleep(1)

    if(ball.xcor()>400):
        ball.reset_to_center()
        scoreboard.refresh_score(player="left")
        screen.update()
        time.sleep(1)

    


screen.exitonclick()