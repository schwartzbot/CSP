import turtle as trtl 

painter = trtl.Turtle()
painter.speed(1000)

painter.right(90)
painter.penup()
painter.goto(0, -150)
painter.pendown()
painter.color("green")
painter.pensize(10)
painter.forward(200)
painter.penup()
painter.goto(0,0)
painter.right(270)
painter.color("black")
painter.pensize(1)

row1 = 0
painter.goto(0,0)
while (row1 < 18):
    painter.penup()
    painter.forward(20)
    painter.right(20)
    painter.pendown()
    painter.begin_fill()
    painter.circle(20)
    row1 = row1 + 1
    if (row1 % 2 == 0):
        painter.fillcolor("magenta")
        painter.end_fill()
    else:
        painter.fillcolor("green")
        painter.end_fill()
painter.goto(0, -20)
row2 = 0
while (row2 < 10):
    painter.penup()
    painter.forward(20)
    painter.right(35)
    painter.pendown()
    painter.begin_fill()
    painter.circle(20)
    row2 = s + 1
    if (row2 % 2 == 0):
        painter.fillcolor("cyan")
        painter.end_fill()
    else:
        painter.fillcolor("yellow")
        painter.end_fill()
painter.goto(0, -45)
row2 = 0
while (row3 < 7):
    painter.penup()
    painter.forward(15)
    painter.right(60)
    painter.pendown()
    painter.begin_fill()
    painter.circle(20)
    row3 = row3 + 1
    if (row3 % 2 == 0):
        painter.fillcolor("red")
        painter.end_fill()
    else:
        painter.fillcolor("pink")
        painter.end_fill()

painter.penup()
painter.goto(0, -250)
painter.pensize(20)
painter.pencolor("green")
painter.pendown()
painter.circle(60, 40)

wn = trtl.Screen()
wn.mainloop()
