from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown()


    def gameover(self):
        self.goto(0,100)
        self.write(arg="Game Over", move=False, align='center', font=('Segoe UI', 18, 'bold'))


    # def input(self):
    #
    #     py





