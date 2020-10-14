#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  newColor = turtle_colors.pop()
  t = trtl.Turtle(shape=s) 
  t.color(newColor)
  my_turtles.append(t)
  t.penup()
  

#The x and y coordinates where the shapes will be drawn from
startx = 0
starty = 0

#for each loop that goes through the my_turtles list
for t in my_turtles:
  t.goto(startx, starty)
  t.right(45)     
  t.forward(50)
  t.pendown()

#change in coordinates after each iteration
  startx = t.xcor() + 50
  starty = t.ycor()  + 50

wn = trtl.Screen()
wn.mainloop()