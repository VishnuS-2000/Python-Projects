from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SHAPE="square"

class Snake:
    def __init__(self, length=3):
        x_start = 0
        y_start = 0
        self.snake_segments = []

        for i in range(0, length):
            new_turtle = Turtle(shape=SHAPE)
            new_turtle.goto(x_start, y_start)
            new_turtle.color("white")
            new_turtle.penup()
            x_start -= 20
            self.snake_segments.append(new_turtle)
        self.head = self.snake_segments[0]

    def move(self):

        """moves snake forward"""

        for i in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[i - 1].xcor()
            new_y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def add_segment(self,position):
        new_turtle = Turtle(shape=SHAPE)
        new_turtle.goto(position)
        new_turtle.color("white")
        new_turtle.penup()
        self.snake_segments.append(new_turtle)
    def extend(self):
        self.add_segment(self.snake_segments[-1].position())
