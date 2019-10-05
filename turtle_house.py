import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("classic")

house_length = 400
house_height = 200
roof_length = 283
door_length = 40
door_height = 80
# draw house
alex.forward(house_length)
alex.right(90)
alex.forward(house_height)
alex.right(90)
alex.forward(house_length)
alex.right(90)
alex.forward(house_height)

# draw roof
alex.right(45)
alex.forward(roof_length)
alex.right(90)
alex.forward(roof_length)

# draw door
alex.penup()
alex.goto(180, -200)
alex.setheading(90)
alex.pendown()
alex.forward(door_height)
alex.right(90)
alex.forward(door_length)
alex.right(90)
alex.forward(door_height)

wn._root.mainloop()