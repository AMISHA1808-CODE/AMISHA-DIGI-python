import pgzrun


height=300 
width=400

p=Rect(20,40,40,30)
def draw():
    screen.fill('green')
    screen.draw.filled_rect(p,'yellow')

def update():
    if keyboard.Right:
        p.x+=2
    if keyboard.left:
        p.x+=2
    if keyboard.up:
        p.y+=2
    if keyboard.down:
        p.y+=2



pgzrun.go()    