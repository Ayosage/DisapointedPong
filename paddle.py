from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=7, stretch_len=1)
        self.color("white")
        self.pu()
        self.goto(position)

    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)


    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)


