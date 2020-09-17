import turtle as trtl

painter = trtl.Turtle()

painter.pensize(5)


#QUESTION 16
#painter.penup()
#painter.goto(200, 200)
#painter.pendown()
#painter.circle(100)

#painter.penup()
#painter.goto(-200, 200)
#painter.pendown()
#painter.circle(100, 30)

#painter.penup()
#painter.goto(-200, -200)
#painter.pendown()
#painter.circle(100, 360, 7)

#painter.penup()
#painter.goto(200, -200)
#painter.pendown()
#painter.circle(100, 270)

#QUESTOIN 18
painter.fillcolor("Blue")
painter.pencolor("Green")

painter.begin_fill()
painter.circle(20)
painter.end_fill()

painter.penup()
painter.goto(200, 200)
painter.pendown()
painter.begin_fill()
painter.circle(100, 360, 10)
painter.end_fill()

wn = trtl.Screen()
wn.mainloop()