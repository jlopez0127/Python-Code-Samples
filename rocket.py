import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.color('white')

# Draw the planet (circle)
pen.penup()
pen.color('grey')
pen.begin_fill('grey')
pen.goto(0, -100)
pen.pendown()

radius = 100
angle = 360
pen.circle(radius, angle)

# Draw the spaceship body (rectangle)
pen.penup()
pen.color('white')
pen.begin_fill()
pen.goto(-25, 100)
pen.pendown()

for _ in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
   
#Window space ship
pen.color('yellow')
pen.penup()
pen.goto(0, 150)
pen.pendown()
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# Spaceship fins
pen.color('red')  

# Draw the first fin
pen.penup()
pen.goto(-30, 80)
pen.pendown()
pen.goto(-20, 100)
pen.goto(-10, 80)
pen.goto(-30, 80)

#second fin
pen.penup()
pen.goto(-10, 80)
pen.pendown()
pen.goto(0, 100)
pen.goto(10, 80)
pen.goto(-5, 80)

#third fin
pen.penup()
pen.goto(15, 80)
pen.pendown()
pen.goto(25, 100)
pen.goto(35, 80)
pen.goto(15, 80)

# spaceship tip (triangle)
pen.penup()
pen.goto(0, 200)
pen.pendown()
pen.color('red')  
pen.begin_fill()
pen.goto(25, 200)
pen.goto(0, 250)
pen.goto(-25, 200)
pen.end_fill()

turtle.done()
screen.exitonclick()
