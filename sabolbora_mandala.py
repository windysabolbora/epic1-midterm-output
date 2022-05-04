import turtle

forw = 1
t = turtle.Turtle()
t.speed(0)

while True:
    t.forward(forw)
    t.left(120)
    t.left(1)
    forw += 1

turtle.done()