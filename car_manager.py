from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
MAX_CARS = 20

class CarManager:
    def __init__(self):
        self.cars = []
        self.max_cars = MAX_CARS
        self.cur_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        spawn_count = 1
        for _ in range(spawn_count):
            if len(self.cars) >= self.max_cars:
                break
            t = Turtle("square")
            t.shapesize(stretch_wid=1, stretch_len=2)
            t.color(choice(COLORS))
            t.penup()
            t.goto(randint(300, 2000), randint(-300, 300))
            t.setheading(180)
            t.move_distance = self.cur_speed
            self.cars.append(t)


    def move(self):
        for car in self.cars:
            car.forward(car.move_distance)

    def level_up(self):
        self.cur_speed += MOVE_INCREMENT
        self.max_cars += 1

        for car in self.cars:
            car.move_distance += MOVE_INCREMENT

    def reset(self):

        for car in self.cars:
            car.hideturtle()
        self.cars = []