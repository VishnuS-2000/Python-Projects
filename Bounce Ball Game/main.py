from turtle import Screen
from Character import Character
from platform import Platform
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=800,height=800)

screen.title("Ball Game")
screen.tracer(0)

ball=Character()
platform=Platform()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(key="space",fun=ball.jump)
screen.bgcolor("#D7E9F7")
game_over_condition=False




def check_collision(obstacle):
   y_range=(obstacle.ycor()-(21/2)*obstacle.turtlesize()[0],obstacle.ycor()+(21/2)*obstacle.turtlesize()[0])
   x_range=(obstacle.xcor()-(21/2)*obstacle.turtlesize()[1],obstacle.xcor()+(21/2)*obstacle.turtlesize()[1])
   if(ball.xcor()>=x_range[0] and ball.xcor()<=x_range[1] and ball.ycor()>=y_range[0] and ball.ycor()<=y_range[1]):
       return True


while(not game_over_condition):
    screen.update()
    ball.move()
    if (scoreboard.score % 10 == 0):
        platform.update_speed()
        ball.update_speed()
    if(ball.success):
        platform.create_new_obstacle=True
        ball.success=False
        scoreboard.refresh_score()
    platform.move()
    for obstacle in platform.obstacles:
            if(check_collision(obstacle)):
                game_over_condition=True
                scoreboard.game_over()










screen.exitonclick()
