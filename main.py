import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkey(player.move_up,"Up")

NUMBER_CARS = 30

cars=[]

for _ in range(NUMBER_CARS):
    car = CarManager()
    cars.append(car)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move_cars()
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.reposition()
        scoreboard.level_update()
        for car in cars:
            car.increase_speed()



screen.exitonclick()


