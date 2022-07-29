import pgzrun

height=200
widht=200
box=Rect(50,50,200,100)
box2=Rect(200,200,200,100)

def draw():
    screen.fill('white')
    screen.draw.rect(box,color='red')
    screen.draw.filled_rect(box2,color='green')


pgzrun.go()    