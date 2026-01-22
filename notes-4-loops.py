
# Auther - Nishaan Gill

import turtle

window = turtle. Screen ()
window.bgcolor("green")
#change the colour of the screen
#to  whatever you like


#TMNT - turtles
mikey = turtle.Turtle()
mikey.turtlesize(10) #size
mikey.color ("orange") #color
mikey.shape("square") #shape
mikey.speed(2)

mikey.forward(500)
mikey.left(90)
mikey.forward(500)
mikey.speed(2)
mikey.penup()
mikey.forward(500)
mikey.forward(500)

# MAKE 100 COOKIES
for counter in range (100):
# Make sure that turtle is pointing east
mikey.setheading(90)
# change the cookie colour
mikey.color("brown")
# draw a cirlce
mikey.penup()
mikey.goto(-5 + counter, -30 + counter)
mikey.pendown()
mikey.circle(30)
# put a chocolate chip on the top left side
mikey.penup()
mikey.goto(-10 + counter , 10 + counter)
mikey.stamp()
# chocolate chip on the top right
mikey.goto(10 + counter ,10 + counter)
mikey.stamp()
# chocolate chip on the bottom right
mikey.goto(10 + counter,-10 + counter)
mikey.stamp()
# chocolate chip on the bottom left
mikey.goto(-10 + counter,-10 + counter)
mikey.goto()
#chocolate chip in the middle
mikey.goto(0 + counter,0 + counter)
mikey.stamp()


window.exitonclick()



# Create a function that makes a cookie
# at (x, y)
def make_cookie(x: int, y: int):
    # Make sure that turtle is pointing east
    mikey.setheading(0)
    # change the cookie colour
    mikey.color("brown")
    # draw a circle
    mikey.pu()
    mikey.goto(-5 + x, -30 + y)
    mikey.pd()
    mikey.circle(30)

    # put a chocolate chip on the top left side
    mikey.pu()
    mikey.goto(-10 + x, 10 + y)
    mikey.stamp()

    # chocolate chip on the top right
    mikey.goto(10 + x, 10 + y)
    mikey.stamp()

    # choco chip on the bottom right
    mikey.goto(10 + x, -10 + y)
    mikey.stamp()

    # ch chip on the bottom left
    mikey.goto(-10 + x, -10 + y)
    mikey.stamp()

    # ch chip in the middle
    mikey.goto(0 + x, 0 + y)
    mikey.stamp()

mikey.speed(0)
# Make cookies in random locations
# Make a 1000 cookies
for _ in range(1000):
    x = random.randrange(-700, 701)
    y = random.randrange(-700, 701)
    make_cookie(x, y)

window.exitonclick()
