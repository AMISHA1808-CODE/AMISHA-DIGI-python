from turtle import*
colors=["red" ,"grey", "blue" ,"yellow","black" ,"green"]
 
s=len(colors)
for i in range(100):
    c=colors[i % s]
    pencolor(c)
    forward(i+5)
    left(360/s)
    for j in range(s):
        forward(100)
        left(60)


mainloop()
