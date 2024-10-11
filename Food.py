import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  #scaling attributes
        self.color("aqua")
        self.speed("fastest")
        random_x = random.randint(-280,280)  #screen size 600 by 600
        random_y = random.randint(-280, 280) # so -300 to 300 and adjusting with snake block 20/20
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-280, 280)  # screen size 600 by 600
        random_y = random.randint(-280, 280)  # so -300 to 300 and adjusting with snake block 20/20
        self.goto(random_x, random_y)


