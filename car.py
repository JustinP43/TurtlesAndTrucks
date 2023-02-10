from turtle import Turtle, colormode
import random

colormode(255)

SPEED_INCREMENT = .9
STARTING_SPEED = .1
MAXIMUM_X_VAL = 400
MINIMUM_X_VAL = -400
MAXIMUM_Y_VAL = 260
MINIMUM_Y_VAL = -250

class Car(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.pu()
        self.setheading(180)
        self.paint()
        self.place()
        self.respawn_timer = 0
        self.speed = .1

        
    def place(self):
        x_cor = random.randint(MINIMUM_X_VAL, MAXIMUM_X_VAL)
        y_cor = random.randint(MINIMUM_Y_VAL, MAXIMUM_Y_VAL)
        self.goto(x_cor,y_cor)

    def move_left(self):
        if self.respawn_timer == 0:
            self.showturtle()
            self.forward(10)
        else:
            self.respawn_timer -= 1

    def speed_up(self):
        self.speed *= SPEED_INCREMENT

    def paint(self):
        r = random.randint(0,255)
        b = random.randint(0,255)
        g = random.randint(0,255)

        my_tuple = (r, b, g)
        self.color(my_tuple)
        
    def respawn(self):
        self.hideturtle()
        self.respawn_timer = random.randint(0,10)
        y_cor = random.randint(MINIMUM_Y_VAL, MAXIMUM_Y_VAL)
        self.goto(MAXIMUM_X_VAL,y_cor)
