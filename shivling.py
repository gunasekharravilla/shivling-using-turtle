import turtle

turtle.speed(0)


turtle.title('SHIVALINGA Design BY-Gunasekhar Ravilla')
turtle.speed(0)
turtle.up()


def my_goto(x, y):
    turtle.pencolor("red")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def round_rectangle(center_x, center_y, width, height, cornersize):
    turtle.up()
    turtle.goto(center_x-width/2+cornersize, center_y-height/2)
    turtle.down()
    for _ in range(2):
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.fd(width-2*cornersize)
        turtle.circle(cornersize, 90)
        turtle.fd(height-2*cornersize)
        turtle.circle(cornersize, 90)
        turtle.end_fill()


def round_rectangle(center_x, center_y, width, height, cornersize):
    turtle.up()
    turtle.goto(center_x-width/2+cornersize, center_y-height/2)
    turtle.down()
    for _ in range(2):
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.fd(width-2*cornersize)
        turtle.circle(cornersize, 90)
        turtle.fd(height-2*cornersize)
        turtle.circle(cornersize, 90)
        turtle.end_fill()


round_rectangle(0, 0, 200, 300, 80)

turtle.fillcolor('black')
turtle.begin_fill()


turtle.goto(-35, 40)
turtle.penup()

turtle.begin_fill()
turtle.fillcolor('white')
turtle.forward(80)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.pendown()
turtle.end_fill()


turtle.goto(-35, 80)
turtle.penup()

turtle.begin_fill()
turtle.fillcolor('white')

turtle.forward(80)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.pendown()
turtle.end_fill()

turtle.goto(-35, 60)
turtle.penup()

turtle.begin_fill()
turtle.fillcolor('white')

turtle.forward(80)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(10)
turtle.left(90)

turtle.pendown()
turtle.end_fill()


turtle.fillcolor('red')
turtle.begin_fill()

turtle.goto(5, 50)
turtle.penup()
r = 15
turtle.circle(r)
turtle.pendown()
turtle.end_fill()


turtle.goto(-150, -175)
turtle.penup()
turtle.pencolor("black")
turtle.fillcolor("black")
turtle.begin_fill()
# double Base
round_rectangle(90, -111, 600, 70, 37)
round_rectangle(90, -170, 600, 70, 37)
round_rectangle(90, -230, 600, 70, 37)

turtle.pendown()


my_goto(-220, -350)
turtle.write('Om Nama Shivaya', font=("Bradley Hand ITC", 50, "bold"))


my_goto(-200, 150)
turtle.write('Hara Mahadeva', font=("Bradley Hand ITC", 50, "bold"))
turtle.done()
