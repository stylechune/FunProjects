# Welcome to SNEK
# My own little version of the classic Snake game
# Sara Keating

# importing all the modules and setting up the screen
import turtle
from itertools import cycle
from random import *
import time
wn = turtle.Screen()
# leaving room at the top for title, score and rules
wn.setup(600, 800)
wn.title("SNEK")
wn.bgcolor("black")
COLORS = cycle(["red", "blue", "green", "yellow"])
wn.tracer(0)
delay = 0.1
score = 0
highscore = 0
segments = []


# function for drawing title
def title(turtle, string):
    turtle.penup()
    turtle.goto(-75, 340)
    # having each letter be a different colour in the name
    for letter in string:
        turtle.color(next(COLORS))
        turtle.write(letter, move=True, font=("Comic Sans MS", 40))


# function for writing rules
def writeRules():
    rules.penup()
    rules.goto(0, 260)
    rules.color("white")
    varText = "Click on the arrows to move the snake (circles) \n Avoid hitting the borders or yourself \n " \
              "Eat as many chips (triangles) as possible!"
    return varText


# function for score chart
def scoreChart(turtle, score, highscore):
    # drawing a black box to cover up previous score
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(-300, 195)
    turtle.color("black", "black")
    turtle.begin_fill()
    for t in range(4):
        turtle.forward(50)
        if t == 0 or t == 2:
            turtle.forward(550)
        turtle.left(90)
    turtle.end_fill()
    # writing new score
    turtle.goto(0, 200)
    turtle.color("white")
    varText = f"Score: {score} High score: {highscore}"
    turtle.write(varText, align="center", font=("Eras Demi ITC", 25, "bold"))


# drawing the barrier, using multiples of the head's movements
def drawBarrier(turtle):
    turtle.penup()
    turtle.color("magenta")
    turtle.pensize(3)
    turtle.goto(-290, -390)
    turtle.pendown()
    for i in range(4):
        turtle.forward(580)
        turtle.left(90)


# moving the head continuously, depending on the input of the next function
def move(turtle):
    if turtle.direction == "up":
        y = turtle.ycor()
        turtle.sety(y + 20)
    elif turtle.direction == "down":
        y = turtle.ycor()
        turtle.sety(y - 20)
    elif turtle.direction == "right":
        x = turtle.xcor()
        turtle.setx(x + 20)
    elif turtle.direction == "left":
        x = turtle.xcor()
        turtle.setx(x - 20)


# making it so the user can't backtrack on the snake, and setting direction of the snake so it can move
def down():
    if head.direction != "up":
        head.direction = "down"


def up():
    if head.direction != "down":
        head.direction = "up"


def right():
    if head.direction != "left":
        head.direction = "right"


def left():
    if head.direction != "right":
        head.direction = "left"


titleturtle = turtle.Turtle()
titleturtle.hideturtle()
title(titleturtle, "SNEK")

rules = turtle.Turtle()
rules.hideturtle()
varRules = writeRules()
rules.write(varRules, align="center", font=("Eras Demi ITC", 15, "normal"))

scorer = turtle.Turtle()
scorer.hideturtle()
scoreChart(scorer, score, highscore)

barrier = turtle.Turtle()
barrier.hideturtle()
drawBarrier(barrier)

# creating the head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("magenta")
head.penup()
# making it the center of the bordered square
head.goto(0, -80)
# setting the direction initially to stop so it doesn't move right away
head.direction = "stop"

# creating first piece of food
food = turtle.Turtle()
food.color("orange")
food.shape("triangle")
food.shapesize(0.5, 0.5)
food.penup()
food.goto(0, 20)

# setting the keybindings
wn.listen()
wn.onkey(up, "Up")
wn.onkey(down, "Down")
wn.onkey(right, "Right")
wn.onkey(left, "Left")


# main gameplay loop
while True:
    wn.update()
    # setting a delay so the snake doesn't move super fast
    time.sleep(delay)
    # if snake collides with food
    if head.distance(food) < 20:
        # sending new piece to random spot within borders
        x = randint(-280, 270)
        y = randint(-370, 170)
        food.goto(x, y)
        # adding a new segment of a different colour
        newsegment = turtle.Turtle()
        newsegment.speed(0)
        newsegment.shape("circle")
        newsegment.color(next(COLORS))
        newsegment.penup()
        segments.append(newsegment)
        # updating the score
        score += 10
        if score > highscore:
            highscore = score
        scoreChart(scorer, score, highscore)
    # having the segments follow the segment ahead of it, starting from the last segment
    for i in range(len(segments)-1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    # special case for the first segment, it must go where the head goes
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    # moving head here so that the first segment does not go over top of it
    move(head)
    # creating conditions for if snake hits one of the borders
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 180 or head.ycor() < -380:
        # pausing program for a second to signify collision
        time.sleep(1)
        # resetting the coordinates and direction
        head.goto(0, -80)
        head.direction = "stop"
        # hiding the segments where they can't be seen
        for s in segments:
            s.goto(5000, 5000)
        # clearing the list
        segments.clear()
        # resetting the score
        score = 0
        scoreChart(scorer, score, highscore)
    # doing the same for if the snake head hits a segment
    for s in segments:
        # checking for collision
        if s.distance(head) < 15:
            time.sleep(1)
            head.goto(0, -80)
            head.direction = "stop"
            for d in segments:
                d.goto(5000, 5000)
            segments.clear()
            score = 0
            scoreChart(scorer, score, highscore)
