from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

home = Screen()
home.setup(1000, 600)
home.tracer(0)
home.listen()
home.bgcolor("black")

scoreboard = Scoreboard()
scoreboard2 = Scoreboard()

paddle_1 = Paddle((-485, 0))
paddle_2 = Paddle((475, 0))

ball = Ball()

home.onkeypress(paddle_1.up, "w")
home.onkeypress(paddle_1.down, "s")
home.onkeypress(paddle_2.up, "Up")
home.onkeypress(paddle_2.down, "Down")

scoreboard2.center()
scoreboard.start()

play = True
while play:
    ball.move()
    ball.contact(paddle_1, paddle_2)

    if ball.xcor() >= 500:
        ball.refresh()
        scoreboard.p1s += 1
        scoreboard.score()

    elif ball.xcor() <= -500:
        ball.refresh()
        scoreboard.p2s += 1
        scoreboard.score()

    home.update()
    time.sleep(ball.fast)

    if scoreboard.p1s > 6 or scoreboard.p2s > 6:
        play = False

home.exitonclick()
