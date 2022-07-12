import pyglet
from pyglet.window import key
import random

window = pyglet.window.Window(width=1200, height=900, caption="Ivan: The Game", resizable=False)
window.set_location(400, 100)

testImage=pyglet.image.load('resources/test.png')
backgroundImage=pyglet.image.load('resources/background.png')
roadImage=pyglet.image.load('resources/road.png')
carImage1=pyglet.image.load('resources/car1.png')
carImage2=pyglet.image.load('resources/car2.png')
carImage3=pyglet.image.load('resources/car3.png')
backlightsImage=pyglet.image.load('resources/backlights.png')

carImages=[carImage1, carImage2, carImage3] # текстурки используемые для машины, чтобы потом их удобно менять

background1=pyglet.sprite.Sprite(backgroundImage, x=0, y=900)
background2=pyglet.sprite.Sprite(backgroundImage, x=0, y=0)
road1=pyglet.sprite.Sprite(roadImage, x=0, y=0)
road2=pyglet.sprite.Sprite(roadImage, x=0, y=-900)
car=pyglet.sprite.Sprite(carImage1, x=0, y=150)
backlights=pyglet.sprite.Sprite(backlightsImage, x=car.x, y=car.y)

sprites=[background1, background2, road1, road2,backlights, car ] # порядок спрайтов в этом списке = приоритет на экране.
moveObj1=[background1, road1]
moveObj2=[background2, road2]

for i in sprites:
    i.x=window.width/2-i.width/2

@window.event
def on_draw():
    window.clear()
    for i in sprites:
        i.draw()

right=False
left=False

@window.event
def on_key_press(symbol, modifiers):
    global  right, left, fire, game
    if symbol == key.RIGHT:
        right = True
    if symbol == key.LEFT:
        left = True
    if symbol == key.SPACE:
        pass

@window.event
def on_key_release(symbol, modifiers):
    global right, left, fire
    if symbol == key.RIGHT:
        right = False
    if symbol == key.LEFT:
        left = False

def playerMove(car, frame):
    if right==True and car.x < window.width/2+backgroundImage.width/2:
        car.x+=frame*100
        backlights.x=car.x
        print(window.width/2+backgroundImage.width/2)
        
    if left==True and car.x > window.width/2-backgroundImage.width/2:
        car.x-=frame*100
        backlights.x=car.x
        print(window.width/2-backgroundImage.width/2)

def groundMove(frame):
    for i in moveObj1:
        i.y-=frame*1000
        if i.y<=0:
            i.y=900
    for i in moveObj2:
        i.y-=frame*1000
        if i.y<=-900:
            i.y=0
        
def update(frame):
    groundMove(frame)
    playerMove(car, frame)
    if str(frame)[-1]=='2':
        car.image=carImages[random.randint(0,len(carImages)-1)]

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()