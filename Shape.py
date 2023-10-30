import turtle

shapeSides = int(input("Please Input the number of sides the shape has: "))
sidesLength = int(input("Please Input, the length of the sides: "))
lineColor = (input("What color are the lines of the shape?: "))
shapeFill = (input("What color is the inside of the shape?: "))

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()

pen.color(lineColor)
pen.fillcolor(shapeFill)

pen.begin_fill()
for _ in range(shapeSides):
    pen.forward(sidesLength)
    pen.right(360 / shapeSides)
pen.end_fill()

screen.exitonclick()
