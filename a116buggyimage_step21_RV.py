import turtle as trtl

x = trtl.Turtle()
x.pensize(40)
x.circle(20)
w = 6
y = 70
z = 380 / w
x.pensize(5)
n = 0
while (n < w):
  x.goto(0,0)
  x.setheading(z*n)
  x.forward(y)
  n = n + 1
x.hideturtle()
wn = trtl.Screen()
wn.mainloop()