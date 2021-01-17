# setup
import turtle
chibi = "giphy.gif"
bg = "turtlebgpic1.gif"
ruby = turtle.Turtle()
wn = turtle.Screen()
wn.setup(700, 700)
wn.bgpic(bg)
wn.title("Chibi Keys")
wn.register_shape(chibi)
ruby.shape(chibi)
ruby.penup()

# defining functions for possible movements


def up():
    ruby.sety(ruby.ycor() + 50)


def down():
    ruby.sety(ruby.ycor() - 50)


def left():
    ruby.backward(50)


def right():
    ruby.forward(50)

# using key input (arrow keys) to call the functions
wn.onkey(up, "Up")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(down, "Down")

# listening to key input indefinitely
wn.listen()
wn.mainloop()
