#1.
# G Y K
import turtle

#Set up the window
screen = turtle.Screen()
screen.bgcolor("Dark Green")
screen.title("Turtle Graphics Example")

g = turtle.Turtle()
g.shape('classic')
g.color('White')

g.shapesize(1, 1)
for i in range(3):
    g.backward(100)
    g.left(90)

g.left(90)
g.left(90)
g.forward(50)
g.left(90)
g.forward(50)
g.left(90)
g.left(90)
g.forward(70)


y = turtle.Turtle()
y.shape('classic')
y.color('Black')
y.shapesize(1, 1)
y.penup()
y.forward(100)
y.pendown()
y.left(90)
y.left(90)
y.left(45)
y.forward(50)
y.right(90)
y.forward(50)
y.left(90)
y.left(90)
y.forward(50)
y.right(45)
y.forward(70)



k = turtle.Turtle()
k.shape('classic')
k.color('red')
k.penup()
k.forward(150)
k.pendown()
k.right(90)
k.forward(100)
k.right(90)
k.right(90)
k.forward(50)
k.right(45)
k.forward(50)
k.right(90)
k.right(90)
k.forward(50)
k.right(90)
k.right(90)
k.right(90)
k.forward(50)






































screen.exitonclick()