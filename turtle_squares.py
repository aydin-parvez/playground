import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("classic")


def draw_square(size):
    for i in range(0, 4):
        if i % 2 == 0:
            alex.pencolor("gold")
        else:
            alex.pencolor("red")
        alex.forward(size)
        alex.right(90)


for x in range(0, 20):
    draw_square(10 + 20*x)
    alex.penup()
    alex.setheading(90)
    alex.forward(10)
    alex.left(90)
    alex.forward(10)
    alex.setheading(0)
    alex.pendown()


wn._root.mainloop()