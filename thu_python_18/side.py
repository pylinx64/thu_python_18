import turtle
import time

palitra_1 = ['red', 'yellow', 'blue']
t=turtle.Pen()
turtle.bgcolor('black')


def side():
	t.pencolor(palitra_1[0])
	t.forward(10)
	t.left(5)


i = 72
while i > 0:
	side()
	i = i - 1

time.sleep(100)
