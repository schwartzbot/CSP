import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

user1 = input("Enter a number")
user2 = input("Enter another number")

loop = 5
#zero iteration
while (loop < 5):
    painter.goto(0,0)
    painter.right(20)
    painter.forward(80)
    painter.pendown()
    painter.circle(10)
    painter.penup()
    line = line + 1
    if (loop % 18 == 0):
        painter.color("navy")
    if (loop % 36 == 0):
        painter.color("salmon")

loop2 = 5
#infinite interation
while (loop2 > 4):
    painter.goto(0,0)
    painter.right(20)
    painter.forward(80)
    painter.pendown()
    painter.circle(10)
    painter.penup()
    loop2 = loop2 + 1
    if (loop2 % 18 == 0):
        painter.color("navy")
    if (loop2 % 36 == 0):
        painter.color("salmon")

wn = trtl.Screen()
wn.mainloop()