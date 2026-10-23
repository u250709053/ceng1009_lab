import turtle
#--setup--
wn=turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
#--functions--

def drawPoly(tess, side, somesize):
    angle=360/side
    for i in range(side):
        tess.fd(somesize)
        tess.left(angle)

def drawSpiral(tess,angle):
    size=1
    for i in range(100):
        tess.fd(size)
        tess.right(angle)
        size+=3

def drawEquitriangle(tess, somesize):
    drawPoly(tess, 3, somesize)
def drawStar(someturtle, size):
    for i in range(5):
        someturtle.forward(size)
        someturtle.right(144)

def drawSprite(someturtle, legs, Lenght):
    angle=360/legs
    for i in range(legs):
        someturtle.forward(Lenght)
        someturtle.backward(Lenght)
        someturtle.left(angle)
# #Exercise 1
# tess.pensize(3)
# tess.pencolor("hotpink")
# drawPoly(tess, 8, 50)
# #--Finish--
# wn.exitonclick()

# #Exercise 2
# tess.pencolor("blue")
# for i in range(20):
#     drawPoly(tess,4, 100)
#     tess.left(18)
# wn.exitonclick()

# #Exercise 3
# tess.pencolor("blue")
# tess.penup()
# tess.pensize(2)
# tess.goto(-170, 0)
# tess.pendown()
# drawSpiral(tess, 90)
#
# tess.penup()
# tess.goto(170, 0)
# tess.pendown()
# drawSpiral(tess, 89)
#
# wn.exitonclick()


# #Exercise 4
# darwEquitriangle(tess,100)
# wn.exitonclick()


# #Exercise 5
# tess.color("hotpink")
# for i in range(5):
#     drawStar(tess,50)
#     tess.penup()
#     tess.forward(250)
#     tess.right(144)
#     tess.pendown()
# wn.exitonclick()

#Exercise 6
drawSprite(tess, 15, 120)

wn.exitonclick()
