from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-140, y=220)
        self.write(f"{self.l_score}", move=False, align='left', font=('Consolas', 50, 'bold'))
        self.goto(x=140, y=220)
        self.write(f"{self.r_score}", move=False, align='right', font=('Consolas', 50, 'bold'))
