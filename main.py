import pyglet
from pyglet.window import key

window = pyglet.window.Window(width=600, height=900, caption="Ivan: The Game", resizable=False)
window.set_location(400, 100)

backgroundImage=pyglet.image.load('resources/background.png')
roadImage=pyglet.image.load('resources/road.png')
background1=pyglet.sprite.Sprite(backgroundImage, x=0, y=0)
background2=pyglet.sprite.Sprite(backgroundImage, x=0, y=-900)
road1=pyglet.sprite.Sprite(roadImage, x=175, y=0)
road2=pyglet.sprite.Sprite(roadImage, x=175, y=-900)

sprites=[background1, background2, road1, road2]
moveObj1=[background1, road1]
moveObj2=[background2, road2]

@window.event
def on_draw():
    window.clear()
    for i in sprites:
        i.draw()


def groundMove(dt):
    for i in moveObj1:
        i.y+=dt*1000
        if i.y>=900:
            i.y=0
    for i in moveObj2:
        i.y+=dt*1000
        if i.y>=0:
            i.y=-900
        
def update(dt):
    groundMove(dt)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()