import turtle as trtl

painter = trtl.Turtle()
painter.speed(50)
painter.pensize(5)

loop = 0
spiral = 3
objectList = ["Background", "Mountains", "grass", "building", "roof", "windows", "door", "person", "turtle"]

for thing in objectList:
    if thing == "Background":
        painter.color("cyan")
        painter.fillcolor("cyan")
        painter.circle(200)
    while (loop < 10):
        painter.goto(0,0)
        painter.right(200 / (spiral))
        spiral = spiral + .5
        painter.forward(50 + loop * 4)
        painter.pendown()
        painter.circle(15)
        painter.penup()
        loop = loop + 1
        if (loop % 2 == 0):
            painter.color("Yellow")
        if (loop % 2 == 1):
            painter.color("Orange")

wn = trtl.Screen()
wn.mainloop()