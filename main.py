import pyglet
from pyglet.window import key
import random
import math
from numba import njit, prange

from sprites import *
from car import *

window = pyglet.window.Window(width=1200, height=900, caption="Ivan: The Game", resizable=False)
window.set_location(0, 30)



for i in decor:
    i.x=-200

fps=pyglet.window.FPSDisplay(window=window)

# 300 735
@window.event
def on_draw():
    window.clear()
    for i in sprites:
        print(i)
        i.draw()
    fps.draw()

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
    if right==True and car.x < 600:
        car.sprite.x+=frame*car.turnSpeed
        
    if left==True and car.sprite.x > 440:
        car.sprite.x-=frame*car.turnSpeed
    
    if up==True:
        car.acceleration()
        if car.sprite.y < 400:
            car.sprite.y+=frame*(50-math.sqrt(car.speed))

    if down==True:
        car.brake()
        if car.sprite.y > 50:
            car.sprite.y-=frame*(50+math.sqrt(abs(car.speed)))
    
    if up==False and down==False:
        car.idle()
        if car.sprite.y>50:
            car.sprite.y-=frame*(50-math.sqrt(abs(car.speed)))
   
def decorRandomizer(i): #300 735 границы дороги для спрайта шириной 150px
    xArr=[50, 100, 150, 200, 250, 300, 750, 800, 850, 900, 950, 1000, 1050]
    def decorXRandomizer(decor):
        decor.x=random.choice(xArr)
    def decorYRandomizer(decor):
        decor.y=random.randint(0,900)+1800    
    for j in decor:
        decorXRandomizer(i)
        decorYRandomizer(i)

def groundMove(frame):
    for i in moveObj1:
        i.y-=frame*car.speed*3
        if i.y<=0:
            i.y=900
            background1.image=backgroundLevel1Images[random.randint(0,len(backgroundLevel1Images)-1)]
            
    for i in moveObj2:
        i.y-=frame*car.speed*3
        if i.y<=-900:
            i.y=0
            background2.image=backgroundLevel1Images[random.randint(0,len(backgroundLevel1Images)-1)]

    for i in decor:
        i.y-=frame*car.speed*3
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
    car.turnSpeedUpdate()
    
    speed.text=str(int(car.speed))

    
if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/60)
    
    pyglet.app.run()