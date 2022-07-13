import pyglet
from pyglet.window import key
import random
import math

window = pyglet.window.Window(width=1200, height=900, caption="Ivan: The Game", resizable=False)
window.set_location(400, 100)

testImage=pyglet.image.load('resources/test.png')
backgroundImage1=pyglet.image.load('resources/background1.png')
backgroundImage2=pyglet.image.load('resources/background2.png')
backgroundImage3=pyglet.image.load('resources/background3.png')

backgroundImages=[backgroundImage1, backgroundImage2, backgroundImage3]

roadImage=pyglet.image.load('resources/road.png')
carImage1=pyglet.image.load('resources/car1.png')
carImage2=pyglet.image.load('resources/car2.png')
carImage3=pyglet.image.load('resources/car3.png')
backlightsImage=pyglet.image.load('resources/backlights.png')

rockImage1=pyglet.image.load('resources/rock.png')
treeImage1=pyglet.image.load('resources/tree.png')

carImages=[carImage1, carImage2, carImage3] # текстурки используемые для машины, чтобы потом их удобно менять

class Car():
    sprite=pyglet.sprite.Sprite(carImage1, x=0, y=150)
    
    speed=250
    turnSpeed=speed/5
    def __init__(self) -> None:
        pass
    def acceleration(self):
        self.speed+=(40-math.sqrt(car.speed))
    def brake(self):
        if self.speed<0:
            self.speed=0
            return
        self.speed-=(1000+self.speed)/100
    def idle(self):
        if self.speed<0:
            self.speed=0
            return
        self.speed-=self.speed/2500


car=Car()

background1=pyglet.sprite.Sprite(backgroundImage1, x=0, y=1350)
background2=pyglet.sprite.Sprite(backgroundImage1, x=0, y=450)
background3=pyglet.sprite.Sprite(backgroundImage1, x=0, y=-450)
road1=pyglet.sprite.Sprite(roadImage, x=0, y=1800)
road2=pyglet.sprite.Sprite(roadImage, x=0, y=900)
road3=pyglet.sprite.Sprite(roadImage, x=0, y=0)

backlights=pyglet.sprite.Sprite(backlightsImage, x=car.sprite.x, y=car.sprite.y)

rock1=pyglet.sprite.Sprite(rockImage1, x=0, y=0)
tree1=pyglet.sprite.Sprite(treeImage1, x=0, y=0)
rock2=pyglet.sprite.Sprite(rockImage1, x=0, y=0)
tree2=pyglet.sprite.Sprite(treeImage1, x=0, y=0)

speed=pyglet.text.Label(str(0), x=0, y=0)
speed.color=(255,255,255,255)
speed.font_size=72

sprites=[background1, background2, background3, road1, road2, road3, rock1, rock2, tree1, tree2, backlights, car.sprite, speed] # порядок спрайтов в этом списке = приоритет на экране.
moveObjB=[background1, background2, background3]
moveObjR=[road1, road2, road3]
decor=[rock1, rock2, tree1, tree2]



for i in sprites:
    try:
        i.x=window.width/2-i.width/2
    except TypeError:
        pass

@window.event
def on_draw():
    window.clear()
    for i in sprites:
        i.draw()

right=False
left=False
up=False
down=False

@window.event
def on_key_press(symbol, modifiers):
    global  right, left, up, down
    if symbol==key.RIGHT:
        right=True
    if symbol==key.LEFT:
        left=True
    if symbol==key.SPACE:
        pass
    if symbol==key.UP:
        up=True
    if symbol==key.DOWN:
        down=True

@window.event
def on_key_release(symbol, modifiers):
    global right, left, up, down
    if symbol==key.RIGHT:
        right=False
    if symbol==key.LEFT:
        left=False
    if symbol==key.UP:
        up=False
    if symbol==key.DOWN:
        down=False
        if car.speed<0:
            car.speed=0

def playerMove(car, frame):
    if right==True and car.sprite.x < 600:
        car.sprite.x+=frame*car.turnSpeed
        backlights.x=car.sprite.x
        
    if left==True and car.sprite.x > 440:
        car.sprite.x-=frame*car.turnSpeed
        backlights.x=car.sprite.x
    
    if up==True:
        car.acceleration()
        if car.sprite.y < 400:
            car.sprite.y+=frame*(50-math.sqrt(car.speed))
            backlights.y=car.sprite.y

    if down==True:
        car.brake()
        if car.sprite.y > 50:
            car.sprite.y-=frame*car.speed/2
            backlights.y=car.sprite.y
    
    if up==False and down==False:
        car.idle()
        if car.sprite.y>50:
            car.sprite.y-=frame*car.speed/5
            backlights.y=car.sprite.y
    print(car.speed)
def decorRandomizer(i):
    def decorXRandomizer(decor):
        decor.x=random.randint(50,backgroundImage1.width-50)
    def decorYRandomizer(decor):
        decor.y=random.randint(0,backgroundImage1.height)+900
    for j in decor:
        decorXRandomizer(i)
        decorYRandomizer(i)
        while j.x in range(350,700):
            decorXRandomizer(j)

def groundMove(frame):
    for i in moveObjB:
        i.y-=frame*car.speed*2
        if i.y<=-900:
            i.y=1600
            i.image=random.choice(backgroundImages)
    for i in moveObjR:
        i.y-=frame*car.speed*2
        if i.y<=-900:
            i.y=1800
    for i in decor:
        i.y-=frame*car.speed*2
        if i.y<=-900:
            i.y=1500
            decorRandomizer(i)
        
frametime=0
skinNow=0

def changeSkin(frame):
    global frametime, skinNow
    frametime+=frame
    if frametime>=0.5:
        car.sprite.image=carImages[skinNow]
        if skinNow<len(carImages)-1:
            skinNow+=1
        else:
            skinNow=0
        frametime=0

def update(frame):
    groundMove(frame)
    playerMove(car, frame)
    changeSkin(frame)
    
    speed.text=str(int(car.speed))
    car.turnSpeed=car.speed/5

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()
    