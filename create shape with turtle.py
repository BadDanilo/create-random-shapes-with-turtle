import turtle
import random

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(0)

# Function to draw a random geometric shape
def draw_shape():
    # Generate a random number between 3 and 10 for the number of sides of the shape
    num_sides = random.randint(3, 10)
    
    # Set the color of the shape to a random color
    t.color(random.random(), random.random(), random.random())
    
    # Draw the shape with the given number of sides
    for _ in range(num_sides):
        t.forward(50)
        t.right(360 / num_sides)

# Move the turtle to a random position on the screen
def move_turtle():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()

# Draw 10 random shapes at different positions on the screen
for _ in range(50):
    move_turtle()
    draw_shape()

# Hide the turtle and display the result
t.hideturtle()
turtle.done()
