#import turtle
import turtle as trtl
import random

#make the turtles
drawBot = trtl.Turtle()
drawBot.pensize(3)
drawBot.speed(0)
drawBot.hideturtle()
mazeBot = trtl.Turtle()
mazeBot.color("purple")

#set up mazeBot
mazeBot.penup()
mazeBot.turtlesize(.5)
mazeBot.shape("turtle")
mazeBot.goto(200,250)
mazeBot.pendown()

#Define distance
distance = 15
door_width = 20
wall_width = 10

#define door and barrier
def drawDoor():
    drawBot.penup()
    drawBot.forward(door_width)
    drawBot.pendown()

def drawBarrier():
    drawBot.right(90)
    drawBot.forward(20)
    drawBot.backward(20)
    drawBot.left(90)


#make a for loop 25 times
for i in range(40):
    if i > 4:
        door = random.randint(door_width, distance - 2*door_width)
        barrier = random.randint(2*wall_width, distance - 2*door_width)

        if door < barrier:
            drawBot.forward(door)
            drawDoor()
            drawBot.forward(barrier - door - door_width)
            drawBarrier()
            drawBot.forward(distance - barrier)
        else:
            drawBot.forward(barrier)
            drawBarrier()
            drawBot.forward(door - barrier)
            drawDoor()
            drawBot.forward(distance - door -door_width)

    drawBot.left(90)
    distance += 10


#define mazeBot directions
def botup():
    mazeBot.setheading(90)
    mazeBot.forward(10)
def botright():
    mazeBot.setheading(0)
    mazeBot.forward(10)
def botdown():
    mazeBot.setheading(270)
    mazeBot.forward(10)
def botleft():
    mazeBot.setheading(180)
    mazeBot.forward(10)

#make a screen
wn = trtl.Screen()



#move mazeBot
wn.onkeypress(botup,"Up")
wn.onkeypress(botright,"Right")
wn.onkeypress(botdown,"Down")
wn.onkeypress(botleft,"Left")
wn.listen()

#mainloop
wn.mainloop()