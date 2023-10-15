from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) #turn off the animation first so that we can't see the initial position of the paddle
#and once we have this tracer(0), we have to update the screen in the following code

#create the right and left paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

#create the ball object
ball = Ball()

#show the score
score = Scoreboard()
score.update_scoreboard()

#control the right paddle
screen.listen()
screen.onkey(r_paddle.up,"Up") #When you use a function as parameter, you don't want to add the parantheses,
#otherwise it won't work
screen.onkey(r_paddle.down,"Down")

#left paddle being controlled by w and s
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) #slow down the movement
    screen.update()
    ball.move()

    # detect collsions with the wall - 判断位置还是放在main.py里
    if ball.ycor() >= 280 or ball.ycor() <= -280: #only need to consider the y-axis bcz
        # if the ball collades the left/right wall, that would be your fault of not moving the paddles in time
        #bounce the ball
        ball.bounce_y()

    # detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) <50 and ball.xcor() < -320: #the paddle height(length) is 100, from the center of paddle to the edge would be 50
        #ball xcor is greater than 340 will check if the ball to the paddle<50 but doesn't hit the paddle
        #bounce the ball
        ball.bounce_x()

    # detect when right paddle misses, and will detect which side of player get a point
    if ball.xcor() > 380:
        #reset the ball
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()