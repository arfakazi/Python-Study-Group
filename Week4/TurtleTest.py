import turtle

def draw_heart():
    turtle.color('red')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90, 200)
    turtle.left(120)
    turtle.circle(-90, 200)
    turtle.forward(180)
    turtle.end_fill()

def draw_joker_face():
    joker.penup()
    joker.goto(-50, 150)
    joker.pendown()
    joker.color('black')

    # Left eye
    joker.begin_fill()
    joker.circle(10)
    joker.end_fill()

    joker.penup()
    joker.goto(50, 150)
    joker.pendown()

    # Right eye
    joker.begin_fill()
    joker.circle(10)
    joker.end_fill()

    # Smile
    joker.penup()
    joker.goto(-60, 100)
    joker.setheading(-60)
    joker.pendown()
    joker.circle(70, 120)

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
joker = turtle.Turtle()
joker.speed(2)

# Draw the heart
draw_heart()

# Draw the joker's face
draw_joker_face()

# Hide the turtle after drawing
joker.hideturtle()

# Display the heart with joker's face
turtle.done()
