import turtle

# Changes the shape/pointer to a turtle
pen = turtle.Pen('turtle')

# Changes width of pen
pen.pensize(4)

# Center
pen.home()
pen.showturtle()

# Starts drawing with red pen
pen.color('red')
pen.pensize(4)
pen.left(145)
pen.forward(100)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(100)

# Starts drawing with blue pen
pen.color('blue')
pen.left(75)
pen.forward(100)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(100)

# End of drawing
turtle.done()