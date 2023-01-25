from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

ball_speed = 15

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Python Pong")
screen.bgcolor("black")
screen.delay(0)
screen.tracer(0)

game_is_on = True

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
while game_is_on:
    sleep(0.1)
    screen.update()
    ball.forward(ball_speed)
    ball.bounce_from_top()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:  # Bounce from right paddle
        ball.setheading(180 - ball.heading())
        ball_speed += 2
    if ball.xcor() > 380:  # Right paddle misses
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()
        sleep(1)
        ball_speed = 15
        ball.kick_off()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:  # Bounce from left paddle
        ball.setheading(180 - ball.heading())
        ball_speed += 2
    if ball.xcor() < -380:  # Left paddle misses
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()
        sleep(1)
        ball_speed = 15
        ball.kick_off()

screen.exitonclick()
