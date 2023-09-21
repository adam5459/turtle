import turtle as Tk

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

def even(x):
    if x == 0:
        return True
    else:
        return x % 2 == 0


win = Tk.Screen()
win.title('turtle')
win.bgcolor('grey')

square = Tk.Turtle()
square.penup()
square.goto(200 , 100)
square.pendown()
for _ in range(4):
    square.pendown()
    square.forward(100)
    square.left(90)
square.hideturtle()

diamond = Tk.Turtle()
diamond.penup()
diamond.goto(-200, 100)
diamond.pendown()
diamond.setheading(45)
diamond.forward(100)
diamond.setheading(-45)
diamond.forward(100)
diamond.setheading(225)
diamond.forward(100)
diamond.setheading(135)
diamond.forward(100)
diamond.hideturtle()

staris = Tk.Turtle()
staris.penup()
staris.goto(-200,-100)
staris.pendown()
for _ in range(4):
    staris.forward(30)
    staris.setheading(0)
    staris.forward(30)
    staris.setheading(90)
staris.hideturtle()


home = Tk.Turtle()
home.penup()
home.goto(200 , -100)
home.pendown()
for _ in range(4):
    home.pendown()
    home.forward(100)
    home.left(90)
home.penup()
home.goto(180, -15)
home.pendown()
home.setheading(45)
home.forward(100)
home.setheading(-45)
home.forward(100)

color = Tk.Turtle()
color.penup()
color.goto(-200,-250)
color.pendown()
for x in range(4):
    color.penup()
    color.pendown()
    if even(x) :
        color.color('red')
    else:
        color.color('black')
    color.forward(100)
    color.left(90)
color.hideturtle()


line = Tk.Turtle()
line.goto(0,0)
for color in colors:
    line.color(color)
    line.forward(15)
line.hideturtle()

hexx = Tk.Turtle()
hexx.penup()
hexx.goto(50, 150)
hexx.pendown()
hexx.color('red')
hexx.setheading(45)
hexx.forward(30)
hexx.setheading(0)
hexx.color('orange')
hexx.forward(30)
hexx.setheading(-45)
hexx.color('yellow')
hexx.forward(30)
hexx.setheading(225)
hexx.color('green')
hexx.forward(30)
hexx.setheading(180)
hexx.color('blue')
hexx.forward(30)
hexx.setheading(130)
hexx.color('violet')
hexx.forward(30)

hexx.hideturtle()

home2 = Tk.Turtle()
home2.penup()
home2.goto(50,-150)
home2.pendown()
home2.begin_fill()
home2.color('blue')
for _ in range(4):
    home2.forward(30) 
    home2.right(90)

home2.end_fill()
home2.penup()
home2.goto(44,-150)
home2.pendown()
home2.setheading(45)
home2.color('red')
home2.begin_fill()
home2.forward(30)
home2.setheading(-45)
home2.forward(30)
home2.setheading(180)
home2.forward(30)
home2.end_fill()

home2.color('white')
home2.penup()

home2.goto(60, -180)
home2.setheading(90)
home2.pendown()
home2.begin_fill()
home2.forward(15)
home2.setheading(0)
home2.fd(10)
home2.setheading(-90)
home2.fd(15)
home2.setheading(180)
home2.fd(10)
home2.end_fill()
home2.hideturtle()


win.mainloop()