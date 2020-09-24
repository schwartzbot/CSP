import turtle as trtl

painter = trtl.Turtle()
painter.speed(50)

loop = 5

while (loop < 5):
    painter.goto(0,0)
    painter.right(20)
    painter.forward(80)
    painter.pendown()
    painter.circle(10)
    painter.penup()
    line = line + 1 # What does this do?
    if (line % 18 == 0):
        painter.color("navy")
    if (line % 36 == 0):
        painter.color("salmon")

loop2 = 5
while (loop2 < 4):
    painter.goto(0,0)
    painter.right(20)
    painter.forward(80)
    painter.pendown()
    painter.circle(10)
    painter.penup()
    line = line + 1 # What does this do?
    if (line % 18 == 0):
        painter.color("navy")
    if (line % 36 == 0):
        painter.color("salmon")