from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard

screen = Screen()
screen.tracer(0)


screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("ping-pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.Move_speed)
    screen.update()
    ball.Move()
    
# detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.Bounce_y()

# detect collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.Bounce_x()

# detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

# detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()

screen.exitonclick()