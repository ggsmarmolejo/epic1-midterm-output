from turtle import *

speed(0)
bgcolor("black")

red , green , blue = 255 , 0 , 0

for q in range(255 * 2):
    colormode(255)
    if q < 255 // 3:
        green += 3
    elif q < 255 * 2 // 3:
        red -= 3
    elif q < 255:
        blue += 3
    elif q < 255 * 4 // 3:
        green -=3
    elif q < 255 * 5 // 3:
        red += 3
    else:
        blue -= 3
    forward(50 + q)
    right(230)
    pencolor(red , green , blue)
    circle(100)
    left(10)
    width(q / 350 + 1)
hideturtle()
    