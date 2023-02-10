from turtle import Turtle

GAME_PIECE_SPEED = 20

class GamePiece(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("turtle")
        self.setheading(90)
        self.reset_position()
        
    def move_up(self):
        self.forward(GAME_PIECE_SPEED)

    def reset_position(self):
        self.goto(0,-280)