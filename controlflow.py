from turtle import*

speed('fast')
bgcolor('yellow')
pencolor('black')
penup()
setpos(-100,100)
pendown()

for i in range(100,0,-3):
    forward(i)
    left(90)
    pencolor('black')

penup()
setpos(-100,-100)
pendown()
for i in range(100,0,-3):
    forward(i)
    left(90)
    pencolor('black')

penup()
setpos(100,100)
pendown()
for i in range(100,0,-3):
    forward(i)
    left(90)
    pencolor('black')
    
penup()
setpos(100,-100)
pendown()
for i in range(100,0,-3):
    forward(i)
    left(90)
    pencolor('black')


mainloop()

