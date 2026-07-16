import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_LINE_X = 280

class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            random_y = random.randint(-250, 250)
            new_car.goto(START_LINE_X, random_y)
            self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)


    def collision(self, player):
        for car in self.all_cars:
            if player.distance(car) < 30:
                return True

    def speed_increase(self):
        self.car_speed += MOVE_INCREMENT
