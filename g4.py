import pgzrun


height=300 
width=400

p=Rect(20,40,40,30)
def draw():
    screen.fill('green')
    screen.draw.filled_rect(p,'yellow')

def update():
    control_player()
    if p.x>width:
        p.x=0
    if p.x<0:
        p.x=width    

def control_player():   

    if keyboard.Right:
        p.x+=2
    if keyboard.left:
        p.x+=2
    if keyboard.up:
        p.y+=2
    if keyboard.down:
        p.y+=2



pgzrun.go()    