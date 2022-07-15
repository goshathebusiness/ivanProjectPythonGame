import pyglet
from pyglet.window import key
import random
import math
import threading

from car import *
from sounds import *

window = pyglet.window.Window(width=1200, height=900, caption="Ivan: The Game", resizable=False)
window.set_location(0, 30)

### ТЕКСТУРЫ ###

testImage=pyglet.image.load('resources/test.png')

backgroundLevel1Image1=pyglet.image.load('resources/background1.png')
backgroundLevel1Image2=pyglet.image.load('resources/background2.png')
backgroundLevel1Image3=pyglet.image.load('resources/background3.png')

roadImage=pyglet.image.load('resources/road.png')

testRockImage=pyglet.image.load('resources/kamen.png')
rockImage1=pyglet.image.load('resources/rock.png')
treeImage1=pyglet.image.load('resources/tree.png')

### СПРАЙТЫ ### 

background1=pyglet.sprite.Sprite(backgroundLevel1Image1, x=0, y=900)
background2=pyglet.sprite.Sprite(backgroundLevel1Image1, x=1200/2-backgroundLevel1Image1.width/2, y=0)
road1=pyglet.sprite.Sprite(roadImage, x=1200/2-roadImage.width/2, y=900)
road2=pyglet.sprite.Sprite(roadImage, x=1200/2-roadImage.width/2, y=0)
testRock=pyglet.sprite.Sprite(rockImage1, x=650, y=500)

### ТЕКСТ ###

speed=pyglet.text.Label(str(0), x=0, y=50)
speed.color=(255,255,255,255)
speed.font_size=72
rpm=pyglet.text.Label(str(0), x=0, y=50+72)
rpm.color=(255,255,255,255)
rpm.font_size=72
gear=pyglet.text.Label(str(0), x=0, y=50+72+72)
gear.color=(255,255,255,255)
gear.font_size=72

### МАССИВЫ ###

sprites=[background1, background2, road1, road2, speed, rpm, gear, testRock , car.sprite] # порядок спрайтов в массиве = приоритет на экране7
backgroundLevel1Images=[backgroundLevel1Image1, backgroundLevel1Image2, backgroundLevel1Image3]
moveObj1=[background1,road1, testRock]
moveObj2=[background2, road2]
decor=[]
obstacles=[testRock]

for i in range(10):
    i=pyglet.sprite.Sprite(rockImage1, x=-200, y=1000)
    sprites.append(i)
    decor.append(i)
for i in range(10):
    i=pyglet.sprite.Sprite(treeImage1, x=-200, y=1000)
    sprites.append(i)
    decor.append(i)

for i in decor:
    i.anchor_x=i.width//2
    i.anchor_y=i.height//2
    i.rotation=random.randint(-5,5)

fps=pyglet.window.FPSDisplay(window=window)

# 300 735
@window.event
def on_draw():
    window.clear()
    for i in sprites:
        i.draw()
    fps.draw()

threadOnDraw=threading.Thread(target=on_draw())
threadOnDraw.start()

right=False
left=False
up=False
down=False
frameCount=0

@window.event
def on_key_press(symbol, modifiers):
    global  right, left, up, down
    if symbol==key.RIGHT:
        right=True
    if symbol==key.LEFT:
        left=True
    if symbol==key.SPACE:
        car.restart()
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
    global frameCount
    if right==True and car.sprite.x < 900: #700
        car.sprite.x+=frame*car.turnSpeed
        if car.sprite.rotation<10:
            car.sprite.rotation+=2
        
    if left==True and car.sprite.x > 300: #500
        car.sprite.x-=frame*car.turnSpeed
        if car.sprite.rotation>-10:
            car.sprite.rotation-=2
    
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
    
    if left==False and right==False:
        if car.sprite.rotation>0:
            car.sprite.rotation-=1
        elif car.sprite.rotation<0:
            car.sprite.rotation+=1
        elif car.sprite.rotation==0 and car.speed>600:    
            if frameCount>=59:
                randomInteger=random.randint(0,4)
                if randomInteger==0:
                    car.sprite.rotation-=5
                    car.sprite.x+=0.016*car.turnSpeed*2
                elif randomInteger==1:
                    car.sprite.rotation+=5 
                    car.sprite.x-=0.016*car.turnSpeed*2
            
def decorRandomizer(i): #300 735 границы дороги для спрайта шириной 150px
    xArr=[50, 100, 150, 200, 250, 300, 750, 800, 850, 900, 950, 1000, 1050]
    i.x=random.choice(xArr)
    i.y=random.randint(0,900)+1800
    i.rotation=random.randint(-5,5)

def groundMove(frame):
    for i in moveObj1:
        i.y-=frame*car.speed*10
        if i.y<=0:
            i.y=900
            background1.image=backgroundLevel1Images[random.randint(0,len(backgroundLevel1Images)-1)]
            
    for i in moveObj2:
        i.y-=frame*car.speed*10
        if i.y<=-900:
            i.y=0
            background2.image=backgroundLevel1Images[random.randint(0,len(backgroundLevel1Images)-1)]

    for i in decor:
        i.y-=frame*car.speed*12
        if i.y<=-900:
            i.y=1500
            decorRandomizer(i)
        
frametime=0
skinNow=0

def changeSkin(frame):
    global skinNow
    
    if frameCount==10 or frameCount==20 or frameCount==30 or frameCount==40 or frameCount==50:
        car.sprite.image=carImages[skinNow]
        if skinNow<len(carImages)-1:
            skinNow+=1
        else:
            skinNow=0
        
def collision():
    for obstacle in obstacles:      
        if obstacle.x>car.sprite.x+car.sprite.width//2 or obstacle.x+obstacle.width<car.sprite.x-car.sprite.width//2: #если самая левая точка препятствия меньше чем самая правая точка машины то пасс и т.д.
            pass
        elif obstacle.y>car.sprite.y+car.sprite.height//2 or obstacle.y+obstacle.height<car.sprite.y-car.sprite.height//2:
            pass
        else:
            print('collision')
            car.crash()
    



def update(frame):
    global frameCount
    threadGroundMove=threading.Thread(target=groundMove(frame))
    
    threadPlayerMove=threading.Thread(target=playerMove(car, frame))
    threadChangeSkin=threading.Thread(target=changeSkin(frame))
    collision()
    threadGroundMove.start()
    threadPlayerMove.start()
    threadChangeSkin.start()
    
    car.turnSpeedUpdate()
    
    speed.text=str(int(car.speed))
    rpm.text=str(int(car.rpm))
    gear.text=str(car.gear)
    
    frameCount+=1
    if frameCount>=60:
        frameCount=0
    
if __name__ == "__main__":
    threading.Thread(target=pyglet.clock.schedule_interval(update, 1/60))
    musicPlayer()
    pyglet.app.run()