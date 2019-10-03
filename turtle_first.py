import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("turtle")


def draw_square(size):
    alex.forward(size)
    alex.right(90)
    alex.forward(size)
    alex.right(90)
    alex.forward(size)
    alex.right(90)
    alex.forward(size)


color = 'red'
for x in range(1, 100):
    alex.pencolor(color)
    draw_square(5 * x)
    alex.left(45)
    alex.right(45 + 90)
    if color == 'red':
        color = 'green'
    else:
        color = 'red'


draw_square(200)

wn._root.mainloop()