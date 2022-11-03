from turtle import Screen
import time
import random
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from highscore import high_score
import pyttsx3
from pygame import mixer
import os

screen = Screen()
screen.setup(width=600, height=600)

back_list = ["final.png","untitled.png","final2.png"]
rand_back = random.choice(back_list)
screen.bgpic(rand_back)

screen.addshape("snake_head.gif")
screen.addshape("snake_head+y.gif")
screen.addshape("snake_head-y.gif")
screen.addshape("snake_head-x.gif")

screen.title("                                                                                Snake")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

mixer.init()
mixer.music.load("Theme.mp3")

engine = pyttsx3.init()


def listen():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.up, "w")

    screen.onkey(snake.down, "Down")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.right, "d")
listen()



is_game_on = True
scoreboard.write(arg=f"Score: 0", move=False, align='center', font=('Segoe UI', 18, 'bold'))
real_time_score=0
mixer.music.play(-1)


while is_game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    # scoreboard.pencolor("white")

    if snake.head.distance(food) < 15:

        food.refresh()
        snake.extend()
        real_time_score += 1
        scoreboard.clear()
        scoreboard.write(arg=f"Score: {real_time_score}", move=False, align='center', font=('Segoe UI', 18, 'bold'))
        chew=mixer.Sound("eat.mp3")
        chew.play()



    # Collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -310 or snake.head.ycor() > 310 or snake.head.ycor() < -310:
        print("u collided with wall")
        scoreboard.gameover()
        is_game_on = False
        high_score.append(real_time_score)
        mixer.music.stop()
        death=mixer.Sound("Death.mp3")
        death.play()
        user_choice = screen.textinput(title="Play Again with same level", prompt="Do you want to play again same level?")
        if user_choice.lower() == "yes":
            is_game_on = True
            for i in snake.segment:
                i.penup()
            snake.head.goto(0,0)
            snake.head.shape("snake_head.gif")
            snake.head.setheading(0)
            scoreboard.clear()

            scoreboard.penup()
            scoreboard.goto(0, 270)

            scoreboard.write(arg=f"Score: {real_time_score}", move=False, align='center', font=('Segoe UI', 18, 'bold'))
            listen()
            mixer.music.play()

        else:
            scoreboard.clear()
            scoreboard.penup()
            scoreboard.goto(0, 0)

            if real_time_score > 0:
                scoreboard.write(arg=f"Game over!!!Your score is {real_time_score} 😊", move=False, align='center',font=('Segoe UI', 18, 'bold'))
                engine.setProperty("rate",125)
                engine.say(f"Your score is {real_time_score} amazingg!")
                engine.runAndWait()
                gameover=mixer.Sound("gameover.mp3")
                gameover.play(-1)


            else:
                scoreboard.write(arg=f"Game over!!!Your score is {real_time_score} ", move=False, align='center',font=('Segoe UI', 18, 'bold'))
                engine.setProperty("rate", 125)
                engine.say(f"Your score is {real_time_score} better luck next time")
                engine.runAndWait()
                gameover = mixer.Sound("gameover.mp3")
                gameover.play(-1)


    seg=[]
    for i in snake.segment:
        if i==snake.head:
            pass

        elif snake.segment[0].distance(i)<0.75:
            scoreboard.gameover()
            is_game_on = False
            print("tail")
            mixer.music.stop()
            death = mixer.Sound("Death.mp3")
            death.play()
            user_choice = screen.textinput(title="Play Again with same level",prompt="Do you want to play again same level?")
            if user_choice.lower() == "yes":
                is_game_on = True
                for i in snake.segment:
                    i.penup()
                snake.head.goto(0, 0)
                snake.head.shape("snake_head.gif")
                snake.head.setheading(0)
                scoreboard.clear()

                scoreboard.penup()
                scoreboard.goto(0, 270)
                # scoreboard.pendown()
                scoreboard.write(arg=f"Score: {real_time_score}", move=False, align='center',  font=('Segoe UI', 18, 'bold'))
                listen()
            else:
                scoreboard.clear()
                scoreboard.penup()
                scoreboard.goto(0, 0)

                scoreboard.write(arg=f"Game over!!!Your score is {real_time_score} 😊", move=False, align='center', font=('Segoe UI', 18, 'bold'))
                engine.setProperty("rate", 125)
                engine.say(f"Your score is {real_time_score} amazingg!")
                engine.runAndWait()
                gameover = mixer.Sound("gameover.mp3")
                gameover.play(-1)

print(high_score)




































screen.exitonclick()