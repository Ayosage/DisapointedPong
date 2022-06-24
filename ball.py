from turtle import Turtle
import random
import math


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.pu()
        self.move_x = 10
        self.move_y = 10
        self.fast = 0.1

    def move(self):
        x = self.xcor() + self.move_x
        y = self.ycor() + self.move_y
        self.goto(x, y)

    def contact(self, p1, p2):
        p1x = abs(self.xcor() - p1.xcor())
        p2x = abs(self.xcor() - p2.xcor())
        if self.distance(p1) < 65 and p1x < 10:
            self.bounce_x()
        if self.distance(p2) < 65 and p2x < 10:
            self.bounce_x()

        if self.ycor() > 290:
            self.bounce_y()
        if self.ycor() < -290:
            self.bounce_y()

    def bounce_y(self):
        self.move_y *= -1
        self.fast *= 0.9

    def bounce_x(self):
        self.move_x *= -1
        self.fast *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.bounce_x()
        self.fast = 0.1

