from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.p1s = 0
        self.p2s = 0
        self.ht()
        self.pu()
        self.pencolor("white")

    def start(self):
        self.goto(-40, 240)
        self.write(f"{self.p1s}", False, "center", ("arial", 40, "bold"))
        self.goto(40, 240)
        self.write(f"{self.p2s}", False, "center", ("arial", 40, "bold"))

    def score(self):
        self.clear()
        self.pu()
        self.goto(-40, 240)
        self.write(f"{self.p1s}", False, "center", ("arial", 40, "bold"))
        self.goto(40, 240)
        self.write(f"{self.p2s}", False, "center", ("arial", 40, "bold"))


    def center(self):
        self.pencolor("white")
        self.goto(0, - 300)
        self.pd()
        self.goto(0, 300)
        self.pu()

