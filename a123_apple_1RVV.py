#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def applFall(active_apple):
  xcor = active_apple.xcor()
  ycor = active_apple.ycor()
  active_apple.penup()
  active_apple.goto(xcor, -150)
  active_apple.clear()
  active_apple.hideturtle()

def userI (active_apple):
  
  active_apple.color("blue")
  active_apple.write("Press 'A'", font=("Arial", 20, "bold"))
  
def dropAppl():
  applFall(apple)

#-----function calls-----
draw_apple(apple)

wn.tracer(False)
userI(apple)
wn.tracer(True)

wn.onkeypress(dropAppl, "a")



wn.listen()

wn.update() 

wn.mainloop()