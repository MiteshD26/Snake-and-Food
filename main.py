import turtle
import time
import Snakes
from Food import Food
from scoreboard import Scoreboard

snake = Snakes.Snake()
food = Food()
scoreboard = Scoreboard()

SRC = turtle.Screen()
SRC.setup(width=600, height=600)
SRC.bgcolor("Black")
SRC.title("SNAKE GAME")

SRC.tracer(0)    # now screen is off


segments = []                              # for storing all segments in one list
game_is_on = True

SRC.listen()
SRC.onkey(snake.up,"Up")
SRC.onkey(snake.down, "Down")
SRC.onkey(snake.left,"Left")
SRC.onkey(snake.right,"Right")
SRC.onkey(snake.up,"w")
SRC.onkey(snake.down, "s")
SRC.onkey(snake.left,"a")
SRC.onkey(snake.right,"d")

while game_is_on:
    SRC.update()
    time.sleep(0.1)

    snake.move()

    # detecting collisions with FOOD

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.clear()
        scoreboard.display_score()
        snake.extend()

    # detecting collisions with Wall
    if snake.head.xcor() > 287 or snake.head.xcor() < -287 or snake.head.ycor() > 287 or snake.head.ycor() < -287:
        game_is_on = False
        scoreboard.game_over()

    # detecting collisions with SELF

    for j in snake.segments:
        if snake.head == j:
            pass
        elif snake.head.distance(j) < 10:
            game_is_on = False
            scoreboard.game_over()









SRC.exitonclick()


