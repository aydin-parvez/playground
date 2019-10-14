import turtle
import math

wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("classic")


for x in range(0, 2000):
    d = x
    alex.goto(d, math.sin(d))


wn._root.mainloop()