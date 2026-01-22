# Recursion
# Author: Nishaan
# October 20

# We're drawing trees (recursively)

import turtle

# Create a turtle that draws
wn = turtle.screen()
t = turtle.Turtle()

# Dictionary to holf colours
 LEAF_COLOURS = {
 "spring":"c28cae"
 "summer": "a8d4ad"
 "winter": "92b9bd"
 "fall": "e57a44"

def draw_tree(level: int, branch_length: float):
        """A recursive function to draw trees
        level - the levels of branches
        branch_length - length of branch to draw
        """
        # Base case is when level is 0
        if level == 0:
            # Create a leaf
            t.color(LEAF_COLOURS ["fall"])
            t.stamp()
            t.color("brown")
            return
    # For all other levels
    else:
        # 1. Go forward branch_length pixels
t.forward(branch_length)
        # 2. Turn to the left and draw a -1 level tree
      t.left(37)
        draw_tree(level - 1, branch_length * 0.8)
        # 3. Turn to the right and draw a -1 level tree
        t.right(74)
        draw_tree(level - 1, branch_length * 0.8)
        # 4. Go back to where we started
        t.left(37)    # point north
        t.backward(branch_length)

# Set up the turtle
t.left(90)
t.color("brown")
t.pensize(5)
t.shape("turtle")
t.penup()
t.goto(0, -180)
t.pendown()
#Setup screen
wn = turtle.Screen()
wn.bgcolor("grey")
# Start drawing
draw_tree(8, 128)
# Wait for click to close
wn.exitonclick()













def factorial (num: int) -> int:
 """Returns the factorial of a a given number
calculated recusrively"""
# If the number is greater than one
if num > 1
   return num * factorial(num - 1)
else:
    return 1









 #draw_complicated_tree(5, 128)
print(factorial (3))    #6
print(factorial (4))    #24
print(factorial(100))   #
