import turtle
import time

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Useless Python Code")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(1)

color = turtle.Turtle()
color.shape("turtle")
color.speed(1)

def draw_heart():
    pen.color("black") # change this to read if you want to lol
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
pen.speed(1)

slow_draw()

turtle.done()
