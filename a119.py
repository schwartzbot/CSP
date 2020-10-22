import turtle as trtl

painter = trtl.Turtle()
painter.speed(50)
painter.pensize(5)

loop = 0
spiral = 3
objectList = ["Background", "Mountains", "grass", "sun", "building", "roof", "windows", "door", "person", "turtle"]

for thing in objectList:
    if thing == "Background":
        painter.goto(0, -500)
        painter.color("cyan")
        painter.fillcolor("cyan")
        painter.begin_fill()
        painter.circle(1000)
        painter.end_fill()
    elif thing == "Mountains":
        painter.penup()
        xcord = -500
        ycord = 0
        painter.goto(xcord, ycord)
        painter.pensize(100)
        painter.color("brown")
        painter.fillcolor("brown")
        painter.pendown()
        painter.begin_fill()
        while xcord < 400:
            painter.goto(xcord, ycord)
            painter.goto(xcord + 100, ycord + 100)
            painter.goto(xcord + 200, ycord)
            xcord += 200
        
        painter.goto(-500, 0)
        painter.end_fill
    elif thing == "sun":
        painter.penup()
        painter.goto(-100, 300)
        painter.pendown()
        painter.pensize(40)
        painter.color("yellow")
        painter.circle(20)#create painter body
        loop = 10
        angle = 360 / loop
        i = 0
        painter.pensize(10)
        while (i < loop):
            painter.goto(-100, 315)
            if(i % 4 == 0):
                painter.setheading(angle * i)
            painter.pendown()
            painter.circle(50, 90)#Draw legs
            painter.penup()
            i = i + 1

wn = trtl.Screen()
wn.mainloop()