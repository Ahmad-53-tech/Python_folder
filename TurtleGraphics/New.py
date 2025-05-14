import turtle
import random

#Set up the window
screen = turtle.Screen() # Create a screen object to control the window.
screen.bgcolor("Dark Green") # Set the background color to light blue.
screen.title("Turtle Graphics Example") # Set the title of the window.



def shapes(sides):
    angle = 360 / sides
    shp = turtle.Turtle()
    shp.shape("classic")
    colors = ['aquamarine', 'peru', 'magenta', 'pale violet red', 'bisque', 'AliceBlue', 'blue', 'cyan', 'ivory',
              'pink']
    color_chosen = random.randint(0, 9)
    shp.color(colors[color_chosen])
    shp.shapesize(2, 2)
    for i in range(sides):
        shp.forward(100)  # Move forward 100 units
        shp.left(angle)


shapes(3)
shapes(4)
shapes(5)
shapes(6)
shapes(7)
shapes(8)
shapes(9)
shapes(10)



screen.exitonclick()








