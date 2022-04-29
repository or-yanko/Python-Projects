import os
import turtle
import time
import random
wn = turtle.Screen()
wn.title("Snake Game By or yanko")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)  # turn off the screen updates
# add head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("black")
food.penup()
food.goto(0, 200)
nodes=[]
# scores
txt_score = turtle.Turtle()
txt_score.speed(0)
txt_score.shape("square")
txt_score.color("black")
txt_score.penup()
txt_score.hideturtle()
txt_score.goto(0, 250)
score = 0
high_score = 0
txt_score.write("Socre:0 High Score:  0", align="center", font=("Ariel", 20, "normal"))

def move():
    speedo=15
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + speedo)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - speedo)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - speedo)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + speedo)
    time.sleep(0.1)
def up():
    head.direction = "up"
def down():
    head.direction = "down"
def left():
    head.direction = "left"
def right():
    head.direction = "right"

# keyboard binding
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")

def game_over():
    # check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for node in nodes:
            node.goto(2000, 2000)
        score = 0
        txt_score.clear()
        txt_score.write("Score:{} High Score : {}".format(score, high_score), align="center",font=("Ariel", 20, "normal"))
        nodes.clear()


# main game loop
while True:

    wn.update()
    game_over()
    if head.distance(food) <20:
        # move the food random
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # add node
        node = turtle.Turtle()
        node.speed(0)
        node.shape("circle")
        node.color("blue")
        node.penup()
        nodes.append(node)
        score += 10
        if score > high_score:
            high_score = score
        txt_score.clear()
        txt_score.write("Score:{} High Score : {}".format(score, high_score), align="center",font=("Ariel", 20, "normal"))

    for i in range(len(nodes) - 1, 0, -1):
        x = nodes[i - 1].xcor()
        y = nodes[i - 1].ycor()
        nodes[i].goto(x, y)
    if len(nodes) > 0:
        x = head.xcor()
        y = head.ycor()
        nodes[0].goto(x, y)
    move()
wn.mainloop()