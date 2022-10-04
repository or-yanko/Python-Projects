import turtle

win = turtle.getscreen()
turtle1 = turtle.Turtle()
win.setup(width=600, height=600)

body_color = 'red'
glass_color = '#9acedc'


# it can move forward backward left right
def body():
    """ draws the body """
    turtle1.pensize(20)
    # turtle1.speed(15)

    turtle1.fillcolor(body_color)
    turtle1.begin_fill()

    # right side
    turtle1.right(90)
    turtle1.forward(50)
    turtle1.right(180)
    turtle1.circle(40, -180)
    turtle1.right(180)
    turtle1.forward(200)

    # head curve
    turtle1.right(180)
    turtle1.circle(100, -180)

    # left side
    turtle1.backward(20)
    turtle1.left(15)
    turtle1.circle(500, -20)
    turtle1.backward(20)

    turtle1.circle(40, -180)
    turtle1.left(7)
    turtle1.backward(50)

    # hip
    turtle1.up()
    turtle1.left(90)
    turtle1.forward(10)
    turtle1.right(90)
    turtle1.down()
    turtle1.right(240)
    turtle1.circle(50, -70)

    turtle1.end_fill()


def glass():
    turtle1.up()
    turtle1.right(230)
    turtle1.forward(100)
    turtle1.left(90)
    turtle1.forward(20)
    turtle1.right(90)

    turtle1.down()
    turtle1.fillcolor(glass_color)
    turtle1.begin_fill()

    turtle1.right(150)
    turtle1.circle(90, -55)

    turtle1.right(180)
    turtle1.forward(1)
    turtle1.right(180)
    turtle1.circle(10, -65)
    turtle1.right(180)
    turtle1.forward(110)
    turtle1.right(180)

    turtle1.circle(50, -190)
    turtle1.right(170)
    turtle1.forward(80)

    turtle1.right(180)
    turtle1.circle(45, -30)

    turtle1.end_fill()


def backpack():
    turtle1.up()
    turtle1.right(60)
    turtle1.forward(100)
    turtle1.right(90)
    turtle1.forward(75)

    turtle1.fillcolor(body_color)
    turtle1.begin_fill()

    turtle1.down()
    turtle1.forward(30)
    turtle1.right(255)

    turtle1.circle(300, -30)
    turtle1.right(260)
    turtle1.forward(30)

    turtle1.end_fill()


body()
glass()
backpack()

turtle.done()
