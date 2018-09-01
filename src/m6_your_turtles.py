"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Lucus Bendzsa.
"""
###############################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

bert = rg.SimpleTurtle('turtle')
bert_pen = rg.Pen
bert.speed = 10

size = 100

bert_pen('blue', 20)

for k in range(5):
    size = size - 20
    bert.pen_down()
    bert.draw_circle(size)


kurt = rg.SimpleTurtle('turtle')
kurt_pen = rg.Pen ('red', 40)
#This pen does not work for some reason will as on this in class.
kurt.speed = 10

size_kurt = 150

for k in range (10):
    kurt.forward(200 - k)
    kurt.right(90 - k)
    kurt.forward(200)
    kurt.right(90)
    kurt.pen_down()
    size_kurt = size_kurt -10

bert.clear()
kurt.clear()

George = rg.SimpleTurtle('turtle')
George_pen = rg.Pen
George.speed = 10

for k in range (4):
    George.draw_regular_polygon(10,50)

h_turtle = rg.SimpleTurtle('turtle')
h_turtle_pen = rg.Pen('red', 30)
h_turtle.speed = 10
#this makes an H
h_turtle.right(180)
h_turtle.pen_up()
h_turtle.forward(300)
h_turtle.pen_down()
h_turtle.forward(30)
h_turtle.right(180)
h_turtle.forward(15)
h_turtle.right(90)
h_turtle.forward(15)
h_turtle.right(90)
h_turtle.forward(15)
h_turtle.right(180)
h_turtle.forward(30)
#this makes an I
h_turtle.right(90)
h_turtle.pen_up()
h_turtle.forward(20)
h_turtle.right(270)
h_turtle.pen_down()
h_turtle.right(180)
h_turtle.forward(10)
h_turtle.pen_up()
h_turtle.forward(4)
h_turtle.pen_down()
h_turtle.forward(15)

window.close_on_mouse_click()