# setup
import turtle

chibi = "giphy.gif"
chibiflip = "giphyflip.gif"
bg = "turtlebgpic1.gif"
ruby = turtle.Turtle()
wn = turtle.Screen()
wn.setup(700, 700)
wn.bgpic(bg)
wn.title("Chibi Keys")
wn.register_shape(chibi)
wn.register_shape(chibiflip)
ruby.shape(chibi)
ruby.penup()

# flipping ruby when she changes direction, and setting the directions and movements


def direction(img1, img2):
    if ruby.heading() == 0:
        ruby.shape(img2)
    elif ruby.heading() == 180:
        ruby.shape(img1)


def up():
    ruby.sety(ruby.ycor() + 50)


def down():
    ruby.sety(ruby.ycor() - 50)


def left():
    ruby.setheading(180)
    direction(chibi, chibiflip)
    ruby.forward(50)


def right():
    ruby.setheading(0)
    direction(chibi, chibiflip)
    ruby.forward(50)


# using key input (arrow keys) to call the functions
wn.onkey(up, "Up")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(down, "Down")

# listening to key input indefinitely
wn.listen()
wn.mainloop()
