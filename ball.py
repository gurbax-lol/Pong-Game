from turtle import Turtle
from random import choice

BALL_START_TRAJECTORY = [30, 45, 60, 120, 135, 150,
                         210, 225, 240, 300, 315, 330]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed("fastest")
        self.kick_off()

    # def move(self):
    #     new_x = self.xcor() + 10
    #     new_y = self.ycor() + 10
    #     self.goto(new_x, new_y)

    def bounce_from_top(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.setheading(360 - self.heading())

    def kick_off(self):
        self.home()
        self.setheading(choice(BALL_START_TRAJECTORY))
