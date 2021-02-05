import turtle

list_colors = ['#8AE252', '#E2AA52', '#E252D0', '#6752E2', '#52E2A0', '#94E252']
t = turtle.Pen()
turtle.bgcolor('black')

text = turtle.textinput('Подсказка 1', 'Подсказка 2')

for i in range(10000):
	t.pencolor(list_colors[i%6])
	t.penup()
	t.forward(i * 25)
	t.pendown()
	t.write(text, font=('Minecraft Title Cyrillic Regular', int((i + 4) / 4), 'bold'))
	t.left(120)
