from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("White")
        self.penup()
        self.goto(0, 265)
        self.write(f"Score: {self.score}  High Score: {self.high_score}",align="center",font=("Times New Roman", 18, "normal"))
        self.hideturtle()

    def display_score(self):
        self.score += 1
        self.write(f"Score: {self.score}  High Score: {self.high_score}",align="center",font=("Times New Roman", 18, "normal"))

    def game_over(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")

        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Times New Roman", 18, "normal"))
