import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
#setup screen
wn = turtle.Screen()
wn.title("Max's Snake Game!")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("green")
food.penup()
food.goto(0,0)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.clear()
pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

#functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
     head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#key listeners
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#main loop
while True:
    wn.update()
    #check head collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        delay = 0.1
        score = 0
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        # Clear the segments list
        segments.clear()

    #check food and head collision
    if head.distance(food) < 1:
        score += 1
        #delay -= 0.001   IS THIS NEEDED?
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        #food go to random location on grid
        x = random.randint(-14, 14)
        y = random.randint(-14, 14)
        food.goto(20*x, 20*y)
        #add body segment to Snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    #function that moves head ↓
    move()

    #check collision between head and body segment
    for segment in segments:
        if segment.distance(head) < 20:
            delay = 0.1
            score = 0
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()
    time.sleep(delay)

#END OF CODE#
