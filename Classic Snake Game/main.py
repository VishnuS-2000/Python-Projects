from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import boundary
screen = Screen()
screen.setup(width=600, height=600)
scoreboard = ScoreBoard()

def Game():
    screen.clear()
    game_is_on=True
    alignment = "center"
    font_style = ("Courier", 15, "bold")
    scoreboard.write(f"Score:{scoreboard.score} High Score :{scoreboard.high_score}",align=alignment,font=font_style)
    screen.tracer(0)
    snake = Snake()
    food = Food()
    screen.listen()
    screen.bgcolor("black")
    screen.title("Snake Game")


    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    while(game_is_on):
        boundary.draw_boundary()
        screen.update()
        time.sleep(0.1)
        snake.move()

        if(snake.head.distance(food)<15):
            food.refresh()
            snake.extend()
            scoreboard.refresh_score()

        if(snake.head.xcor()>=285 or snake.head.xcor()<=-285 or snake.head.ycor()>=285 or snake.head.ycor()<=-285):
            game_is_on=False


        for segment in snake.snake_segments[1:]:
            if(snake.head.distance(segment)<10):
                game_is_on=False

    if(not game_is_on):
        scoreboard.reset_scoreboard()
        Game()





Game()
screen.exitonclick()




