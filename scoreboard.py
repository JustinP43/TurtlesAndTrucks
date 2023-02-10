from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(-350,260)
        self.score = 0
        self.color("black")
        self.write(f"Score: {self.score}",False,align="center",font=("Arial",16,"normal"))

    def increment_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}",False,align="center",font=("Arial",16,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over.",False,align="center",font=("Arial",16,"normal"))
        
