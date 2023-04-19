"This program creates a picture of the american flag."

# ---------------------------------------------------------
# 4/19/23
# McKay Fawcett
# CSIS-1300-01-Sp23
# ---------------------------------------------------------

import turtle

# Create a turtle object and set its speed to fast
flag_turtle = turtle.Turtle()
flag_turtle.speed("fastest")

# Set the turtle's starting position
flag_turtle.penup()
flag_turtle.goto(0, 60)
flag_turtle.pendown()

# Draw the flag's blue rectangle
flag_turtle.color("navy")
flag_turtle.begin_fill()
flag_turtle.forward(200)
flag_turtle.right(90)
flag_turtle.forward(200)
flag_turtle.right(90)
flag_turtle.forward(400)
flag_turtle.right(90)
flag_turtle.forward(200)
flag_turtle.right(90)
flag_turtle.end_fill()

# Draw the white stripes
flag_turtle.color("white")
flag_turtle.penup()
flag_turtle.goto(-80, 40)
flag_turtle.pendown()
for i in range(2):
    flag_turtle.begin_fill()
    for j in range(2):
        flag_turtle.forward(400)
        flag_turtle.right(90)
        flag_turtle.forward(20)
        flag_turtle.right(90)
    flag_turtle.end_fill()
    flag_turtle.penup()
    flag_turtle.goto(-80, flag_turtle.ycor()-40)
    flag_turtle.pendown()

# Draw the rest of the white stripes starting from (-200, 20)
for i in range(4):
    flag_turtle.begin_fill()
    for j in range(2):
        flag_turtle.forward(400)
        flag_turtle.right(90)
        flag_turtle.forward(20)
        flag_turtle.right(90)
    flag_turtle.end_fill()
    flag_turtle.penup()
    flag_turtle.goto(-200, flag_turtle.ycor()-40)
    flag_turtle.pendown()

# Draw the red stripes
flag_turtle.color("red")
flag_turtle.penup()
flag_turtle.goto(-80, 60)
flag_turtle.pendown()
for i in range(3):
    flag_turtle.begin_fill()
    for j in range(2):
        flag_turtle.forward(280)
        flag_turtle.right(90)
        flag_turtle.forward(20)
        flag_turtle.right(90)
    flag_turtle.end_fill()
    flag_turtle.penup()
    flag_turtle.goto(-80, flag_turtle.ycor()-40)
    flag_turtle.pendown()

flag_turtle.penup()
flag_turtle.goto(-200, flag_turtle.ycor()-0)
flag_turtle.pendown()

for i in range(4):
    flag_turtle.begin_fill()
    for j in range(2):
        flag_turtle.forward(400)
        flag_turtle.right(90)
        flag_turtle.forward(20)
        flag_turtle.right(90)
    flag_turtle.end_fill()
    flag_turtle.penup()
    flag_turtle.goto(-200, flag_turtle.ycor()-40)
    flag_turtle.pendown()

# Draw the stars
flag_turtle.color("white")
flag_turtle.penup()
flag_turtle.goto(-190, 50)
flag_turtle.pendown()

dot_size = 5
dot_gap = 11
row_gap = 25

for i in range(5):
    for j in range(10):
        flag_turtle.begin_fill()
        flag_turtle.circle(dot_size)
        flag_turtle.end_fill()

        flag_turtle.penup()
        flag_turtle.forward(dot_gap)
        flag_turtle.pendown()

    flag_turtle.penup()
    flag_turtle.goto(-190, flag_turtle.ycor() - row_gap)
    flag_turtle.pendown()


#Ok, because this was an optional assignment, I wanted to try using ChatGPT. I first started by telling him the assingment. He wrote a code, that show kind of what a flag could look like. It wasn't great. I had him tweek a few things. It was starting to look more like a flag. It took about an hour or so of trial and error with him, before I realized what the problems were and did them myself. I think ChatGPt is useful, but not perfect. The program had 24 errors in it before i changed it. I think it had a good start, but without human intervention It was unable to write a perfect code excatly as I wanted it.