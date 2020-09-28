import turtle as trtl

painter = trtl.Turtle()

painter.shape("circle")
painter.hideturtle()
painter.penup()

y = 200
x = -200
while (y > 0):
    y = y - 50
    painter.goto(x, y)
    painter.color("blue")
    painter.stamp()

wn = trtl.Screen()
wn.mainloop()