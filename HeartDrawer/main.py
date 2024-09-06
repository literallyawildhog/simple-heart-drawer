import turtle
import time

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white") # Change this to any color you like
screen.title("Useless Python Code") # Change this to any title you like

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(1)

color = turtle.Turtle()
color.shape("turtle")
color.speed(1)

def draw_heart():
    pen.color("black") # Change this to any color you like
    pen.begin_fill()

    pen.left(50)
    pen.forward(133)

    pen.circle(50, 200)
    
    pen.right(140)
    pen.circle(50, 200)
    
    pen.forward(133)

def slow_draw():
    for _ in range(1):
        draw_heart()
        time.sleep(0.05)

pen.hideturtle()
pen.speed(1) # Adjust this to make the drawing more faster :)

slow_draw()

turtle.done()
