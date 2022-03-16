from turtle import Turtle

STARTING_POSITIONS = [(0,0), (0,-20), (0,-40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.tail_growth(position)


    def tail_growth(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_turtles.append(new_turtle)

    def extend(self):
        self.tail_growth(self.all_turtles[-1].position())

    def move(self):
        for turt_num in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[turt_num - 1].xcor()
            new_y = self.all_turtles[turt_num - 1].ycor()
            self.all_turtles[turt_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
