counter = 0
x = 0.
y = 1.0
while counter < 50:
    z = x + y
    x = y
    y = z
    ratio = z/y;
    counter = counter + 1
    print(str(ratio) + " " + str(z))
