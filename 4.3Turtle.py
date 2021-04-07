import turtle
import random

def screenLeftClick(x, y) :
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)
def screenRightClick(x, y) :
    turtle.penup()
    turtle.goto(x, y)
def screenMidClick(x, y) :
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.forward(100)

    window.exitonclick()

# 변수 선언
pSize, tSize = 10, 0
r, g, b = 0.0, 0.0, 0.0

turtle.title("거북거북")
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()

# draw_square()


# turtle.shape('turtle')
#
# turtle.forward(200)
# turtle.right(90)
# turtle.done

