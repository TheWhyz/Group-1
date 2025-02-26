import turtle
import random

# Constants
BRANCH_LENGTH = 100
ANGLE = 30
DEPTH = 7

def draw_branch(pen, length, angle, depth):
    if depth == 0:
        return
    
    pen.width(depth)
    pen.forward(length)
    new_length = length * random.uniform(0.6, 0.8)
    
    for turn in (angle, -2 * angle, angle):  # Left, Right, Back to Center
        pen.left(turn)
        draw_branch(pen, new_length, angle, depth - 1)

    pen.backward(length)  # Return to previous position

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    
    pen = turtle.Turtle()
    pen.color("green")
    pen.speed(0)
    pen.left(90)
    pen.up()
    pen.goto(0, -250)
    pen.down()
    
    draw_branch(pen, BRANCH_LENGTH, ANGLE, DEPTH)
    screen.mainloop()

if __name__ == "__main__":
    main()
