import turtle
#screen
wn=turtle.Screen()
wn.title("first game from jaabulateur")
wn.setup(width=600,height=800)
wn.bgcolor("green")
wn.tracer(0)

#paddle a
pd_a=turtle.Turtle()
pd_a.speed(0)
pd_a.shape("square")
pd_a.shapesize(stretch_len=6,stretch_wid=1)
pd_a.color("black")
pd_a.penup()
pd_a.goto(0,360)

#paddle b
pd_b=turtle.Turtle()
pd_b.speed(0)
pd_b.shape("square")
pd_b.shapesize(stretch_len=6,stretch_wid=1)
pd_b.color("black")
pd_b.penup()
pd_b.goto(0,-360)

#ball
b=turtle.Turtle()
b.shape("circle")
b.speed(0)
b.color("orange")
b.penup()
b.dx=2#ball moves
b.dy=2#ball moves

wn.listen()
#paddle a moves
def pd_a_left():
    x=pd_a.xcor()
    x-=20
    pd_a.setx(x)
def pd_a_right():
    x=pd_a.xcor()
    x+=20
    pd_a.setx(x)

    #paddle b moves
def pd_b_left():
    x=pd_b.xcor()
    x-=20
    pd_b.setx(x)
def pd_b_right():
    x=pd_b.xcor()
    x+=20
    pd_b.setx(x)

wn.onkeypress(pd_a_left,"4")
wn.onkeypress(pd_a_right,"6")
wn.onkeypress(pd_b_left,"q")
wn.onkeypress(pd_b_right,"d")
#main game loop
while True:
    wn.update()
    b.setx(b.xcor()+b.dx)
    b.sety(b.ycor()+b.dy)
    # border contole

