import turtle

#Set up the window
screen = turtle.Screen() # Create a screen object to control the window.
screen.bgcolor("Dark Green") # Set the background color to light blue.
screen.title("Turtle Graphics Example") # Set the title of the window.

# Create a turtle object - turtle relies on tkinter under the hood to create graphics
t = turtle.Turtle() # creates the turtle that will draw.
t.shape('classic') # See python docs for more shapes
t.color('White') # View colors from here: https://cs111.wellesley.edu/reference/colors

t.shapesize(2,2) # Stretch the turtle's shape (width, height)
# Moving the turtle
# t.forward(100) # Move forward 100 units
# t.right(90) # Turn right by 90 degrees

for i in range(10):
    t.forward(10) # Move without drawing
    t.penup() # Lift the pen to stop drawing
    t.forward(10)
    t.pendown()















screen.exitonclick()

