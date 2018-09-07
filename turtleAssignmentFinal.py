import turtle
import math
import random

wn = turtle.Screen()

andy = turtle.Turtle()
myTurtle = turtle.Turtle()

andy.hideturtle()
andy.speed(0)

myTurtle.speed(0)
myTurtle.hideturtle()

def colorChanger():
    color = "%06x" % random.randint(0, 0xFFFFFF)
    hexColor = '#'+color
    andy.pencolor(hexColor)

myTurtle.pu()
myTurtle.goto(-200,-100)
myTurtle.pd()

#I put this in here because it looks awesome and I wanted to better understand the code
#loaded from gist: https://gist.github.com/viebel/5349bcca144c41b8f83af39079bf59ad
def hilbert2(step, rule, angle, depth, t):
   if depth > 0:
      a = lambda: hilbert2(step, "a", angle, depth - 1, t)
      b = lambda: hilbert2(step, "b", angle, depth - 1, t)
      left = lambda: t.left(angle)
      right = lambda: t.right(angle)
      forward = lambda: t.forward(step)
      myTurtle.pencolor("black")
      print("Depth = " + str(depth))
      if rule == "a":
        left(); b(); forward(); right(); a(); forward(); a(); right(); forward(); b(); left();
      if rule == "b":
        right(); a(); forward(); left(); b(); forward(); b(); left(); forward(); a(); right();

hilbert2(5, "a", 90, 6, myTurtle)

### From here down is all me
pointX1 = -100
pointY1 = -100

pointX2 = 100
pointY2 = -100

pointX3 = 100
pointY3 = 100

pointX4 = -100
pointY4 = 100

dx = 4
dy = (math.sqrt((math.pow((-100-0),2))+(math.pow((-100-0),2)))/25)

def rotater():
    global pointX1
    print("pointX1 was " + str(pointX1) + " and is now " + str(pointX1 - dx))
    pointX1 += dx
    global pointY1
    print("pointY1 was " + str(pointY1) + " and is now " + str(pointY1 + dy))
    pointY1 -= dy

    global pointX2
    print("pointX2 was " + str(pointX2) + " and is now " + str(pointX2 + dx))
    pointX2 += dx
    global pointY2
    print("pointY2 was " + str(pointY2) + " and is now " + str(pointY2 - dy))
    pointY2 += dy

    global pointX3
    print("pointX3 was " + str(pointX3) + " and is now " + str(pointX3 - dx))
    pointX3 -= dx
    global pointY3
    print("pointY3 was " + str(pointY3) + " and is now " + str(pointY3 + dy))
    pointY3 += dy

    global pointX4
    print("pointX4 was " + str(pointX4) + " and is now " + str(pointX4 + dx))
    pointX4 += dx
    global pointY4
    print("pointY4 was " + str(pointY4) + " and is now " + str(pointY4 - dy))
    pointY4 -= dy

andy.pu()
andy.goto(pointX1, pointY1)
andy.pd()

while pointY1 > -141.421356237:
    colorChanger()
    andy.goto(pointX2, pointY2)
    andy.goto(pointX3, pointY3)
    andy.goto(pointX4, pointY4)
    andy.goto(pointX1, pointY1)
    rotater()

#reverse q2
dy = dy * -1

while pointY1 < -100:
    colorChanger()
    andy.goto(pointX2, pointY2)
    andy.goto(pointX3, pointY3)
    andy.goto(pointX4, pointY4)
    andy.goto(pointX1, pointY1)
    rotater()

#reverse q3
dy = dy * -1
dx = dx * -1

while pointX1 > -141.421356237:
    colorChanger()
    andy.goto(pointX2, pointY2)
    andy.goto(pointX3, pointY3)
    andy.goto(pointX4, pointY4)
    andy.goto(pointX1, pointY1)
    rotater()
