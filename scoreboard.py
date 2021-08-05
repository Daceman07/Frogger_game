from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def update(self):
        self.clear()
        self.level += 1
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def game_over(self):
        self.goto(-70, 0)
        self.write(f"Game Over", align="Left", font=FONT)