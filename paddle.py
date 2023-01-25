from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(x=start_x, y=0)

    def go_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def go_down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)
