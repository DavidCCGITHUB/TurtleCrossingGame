from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        self.setheading(180)
        self.x_cor = random.randrange(-300, 300)
        self.update_position()
        self.setx(self.x_cor)


    def move_cars(self):
        if self.xcor() > -320:
            self.forward(self.speed)
        else:
            self.update_position()


    def update_position(self):
        color = random.choice(COLORS)
        self.color(color)
        y_cor = random.randrange(-230, 230)
        self.setx(320)
        self.sety(y_cor)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT




