import turtle
import random

wn = turtle.Screen()
andy = turtle.Turtle()

def colorPicker():
	color = "%06x" % random.randint(0, 0xFFFFFF)
	hexColor = '#'+color
	print (hexColor)
	print (type(hexColor))
	print ("hexColor length is " + str(len(hexColor)))
	andy.pencolor(hexColor)

#call threeDeeEr using coord pairs
# threeDeeEr(-150,50)

letterHeight = 100
letterWidth = 50
letterThreeD = 40

originX = 0
originY = 0

def slopeFinder(x,y):
	slope = ((y - originY)/(x - originX))
	return slope

def nextPointFinder(slope, x, y):
	triangleDictionary = dict()
	x2 = x + ((d)/(math.sqrt(1 + math.pow(slope, 2))))
	y2 = y + slope * ((d)/(math.sqrt(1 + math.pow(slope, 2))))
	d['x'] = x
	d['y'] = y
	d['x2'] = x2
	d['y2'] = y2
	d['slope'] = slope
	return triangleDictionary

def threeDeeEr(x,y):
	andy.setheading(30)
	andy.pu()
	andy.goto(x,y)
	andy.pd()
	andy.forward(letterThreeD)
	andy.pu()

def straightUp(x,y):
	andy.setheading(90)
	andy.pu()
	andy.goto(x,y)
	andy.pd()
	andy.forward(letterHeight)
	andy.pu()

def straightOver(x,y):
	andy.setheading(0)
	andy.pu()
	andy.goto(x,y)
	andy.pd()
	andy.forward(letterWidth)
	andy.pu()


# A
colorPicker()
straightUp(-190,-50)
straightUp(-140,-50)
straightOver(-190,50)
straightOver(-190,0)

colorPicker()
threeDeeEr(-190,50)
threeDeeEr(-140,-50)
threeDeeEr(-140,50)
threeDeeEr(-190,-50)

colorPicker()
straightUp()




wn.exitonclick()
