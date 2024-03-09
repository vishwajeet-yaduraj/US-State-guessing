from turtle import Turtle


class Names(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.hideturtle()
        self.color("black")
        self.penup()

    def go(self, x, y):
        self.goto(x, y)

    def writes(self, anything):
        self.write(anything)
