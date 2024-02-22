import turtle
import datetime as dt
import time
s=turtle.Turtle()
t=turtle.Turtle()
sec=dt.datetime.now().second
min=dt.datetime.now().minute
hr=dt.datetime.now().hour
turtle.bgcolor("#5FA052")
s.hideturtle()
t.hideturtle()
s.speed(0)
t.speed(0)
s.fillcolor("#FFFDD0")
s.pensize(4)
s.begin_fill()
s.forward(200)
s.left(180)
s.forward(200)
s.forward(200)
s.right(90)
s.forward(100)
s.right(90)
s.forward(400)
s.right(90)
s.forward(100)
s.right(90)
s.forward(200)
s.end_fill()
s.penup()
s.left(90)
s.forward(200)
s.left(90)
s.pendown()
s.circle(250)
s.circle(240)
t.backward(120)
while True:
    t.clear()
    t.write(str(hr).zfill(2)
            + ":"+str(min).zfill(2)+":"
            + str(sec).zfill(2),
            font=("Arial Narrow",60,"bold"))
    time.sleep(1)
    sec+=1
    if sec==60:
        sec=0
        min+=1
    if min==60:
        min=0
        hr+=1
    if hr==13:
        hr=1

turtle.mainloop()