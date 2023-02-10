#turtle doesnt speed up
#trucks speed up each level
#turtle only moves forward
#turtle hits the car game over
#turtle gets across next level- cars speed up

from turtle import Screen
from player import GamePiece
from car import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor("white")
screen.tracer(0)

turtle = GamePiece()
scoreboard = Scoreboard()
cars = []

for _ in range(25):
    new_car = Car()
    cars.append(new_car)

screen.listen()
screen.onkey(turtle.move_up, "Up")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(cars[0].speed)

    for car in cars:
        car.move_left()

    #detect collision with boundary
    if turtle.ycor() > 290:
        turtle.reset_position()
        scoreboard.increment_score()
        cars[0].speed_up()
        new_car = Car()
        new_car.goto(400,0)
        cars.append(new_car)

    #detect car collision with wall
    for car in cars:
        if car.xcor() < -390:
            car.respawn()

    #detect collision with car
    for car in cars:
        if turtle.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
