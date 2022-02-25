from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to Ping Pong")
screen.tracer(0)

ball = Ball()
paddle_l = Paddle(-370, 0)
paddle_r = Paddle(370, 0)
scoreboard = Scoreboard()

screen.listen()

screen.onkey(paddle_l.down, "s")
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce
        ball.bounce_y()


    #detect collision with right paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor()  < -320:
        ball.bounce_x()

    #detect if ball misses either paddle
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset()



    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset()






screen.exitonclick()