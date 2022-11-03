from turtle import Turtle
import random
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
COLOR=["#A3C930"]
class Snake:

    def __init__(self):
      self.segment=[]
      self.create_snake()
      self.head=self.segment[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:

            new_segment=Turtle("square")
            new_segment.color("white")

            new_segment.penup()
            new_segment.goto(i)
            self.segment.append(new_segment)
            new_segment.clear()
            new_segment.shapesize()
        self.segment[0].shape("snake_head.gif")
        self.segment[0].shapesize(1)

        global random_color
        random_color=random.choice(COLOR)
        for _ in self.segment:
            _.color(random_color)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color(random_color)
        new_segment.penup()

        new_segment.goto(self.segment[-1].position())
        self.segment.append(new_segment)

    # def tailhit(self):
    #     seg1=random.randint(1,len(self.segment))
    #     seg2=random.randint(1,len(self.segment))
    #
    #         game_status=False
    #


    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):

            new_x=self.segment[seg_num-1].xcor()
            new_y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
            self.head.shape("snake_head+y.gif")

    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)
           self.head.shape("snake_head-y.gif")

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head.shape("snake_head.gif")

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.shape("snake_head-x.gif")

    def vanish(self):
        for seg in self.segment:
            seg.hideturtle()
    # def start_again(self):
    #     for i in self.segment:
    #         for x in range(3):
    #             i.goto(STARTING_POSITIONS[x])