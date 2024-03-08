from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard


def create_bricks():
    x = -320
    y = 300
    colors = ["red", "orange", "green", "yellow"]
    for j in range(8):
        for i in range(8):
            bricks.append(Brick((x, y), colors[j//2]))
            x += 90
        y -= 30
        x = -320


screen = Screen()
screen.bgcolor("black")
screen.setup(width=740, height=800)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -300))
ball = Ball()
bricks = []
create_bricks()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.bounce_x()

    # Detect collision with paddle or with top wall
    if ball.distance(paddle) < 50 and ball.ycor() < -270 or ball.ycor() > 380:
        ball.bounce_y()

    # Detect collision with bricks
    for brick in bricks:
        if ball.distance(brick) < 36:
            ball.bounce_y()
            brick.delete_brick()
            bricks.remove(brick)
            scoreboard.point()

    # Detect paddle misses
    if ball.ycor() < -380:
        ball.reset_position()
        game_is_on = False

screen.exitonclick()
