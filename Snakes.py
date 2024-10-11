import turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POS:
            self.add_seg(i)   # passing iterator value
    def add_seg(self, i):
        temp_turtle = turtle.Turtle("square")
        temp_turtle.color("white")
        temp_turtle.penup()
        temp_turtle.goto(i)
        self.segments.append(temp_turtle)

    def extend(self):
        self.add_seg(self.segments[-1].position())   # -1 means last seg & position is built function

    def move(self):
        for j in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[j - 1].xcor()
            new_y = self.segments[j - 1].ycor()
            self.segments[j].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.segments[0].setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.segments[0].setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.segments[0].setheading(0)

