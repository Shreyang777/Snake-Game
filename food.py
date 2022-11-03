from turtle import Turtle
import random
COLOR=["#96ceb4","#c83349","#eeac99","#d6d4e0","#b8a9c9","#f4a688"]
class Food(Turtle):

     def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color(random.choice(COLOR))
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

     def refresh(self):
        self.color(random.choice(COLOR))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

