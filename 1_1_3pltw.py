import turtle as trtl 

painter = trtl.Turtle()

loopOne = range(0, 19)
for i in loopOne:
    painter.forward(20)
    painter.right(20)


wn = trtl.Screen()
wn.mainloop()