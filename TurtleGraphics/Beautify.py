import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Graphics Example")
colors = ['aquamarine', 'peru', 'magenta', 'pale violet red', 'bisque', 'AliceBlue', 'blue', 'cyan', 'ivory',
              'pink']

t = turtle.Turtle()
t.pensize(2)
t.speed(0)
for x in range(360):
    t.pencolor(colors[x % len(colors)])
    t.width(x // 100 + 1)
    t.forward(x)
    t.right(88)





turtle.hideturtle()
screen.exitonclick()




