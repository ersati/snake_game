from turtle import Turtle
ALIGNMENT ="center"
FONT = ('Arial', 18, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.counter = 0
        self.penup()
        self.hideturtle()
        self.color("White")
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.counter}", False, align=ALIGNMENT, font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)
    def add_score(self):
        self.counter += 1
        self.update_score()

