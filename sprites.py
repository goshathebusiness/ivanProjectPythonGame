import pyglet
from numba import prange
from car import *

### ТЕКСТУРЫ ###

testImage=pyglet.image.load('resources/test.png')

backgroundLevel1Image1=pyglet.image.load('resources/background1.png')
backgroundLevel1Image2=pyglet.image.load('resources/background2.png')
backgroundLevel1Image3=pyglet.image.load('resources/background3.png')

backgroundLevel1Images=[backgroundLevel1Image1, backgroundLevel1Image2, backgroundLevel1Image3]

roadImage=pyglet.image.load('resources/road.png')


backlightsImage=pyglet.image.load('resources/backlights.png')



testRockImage=pyglet.image.load('resources/kamen.png')

rockImage1=pyglet.image.load('resources/rock.png')
treeImage1=pyglet.image.load('resources/tree.png')

### СПРАЙТЫ ### порядок спрайтов сверху вниз = приоритет на экране

background1=pyglet.sprite.Sprite(backgroundLevel1Image1, x=0, y=900)
background2=pyglet.sprite.Sprite(backgroundLevel1Image1, x=1200/2-backgroundLevel1Image1.width/2, y=0)
road1=pyglet.sprite.Sprite(roadImage, x=1200/2-roadImage.width/2, y=900)
road2=pyglet.sprite.Sprite(roadImage, x=1200/2-roadImage.width/2, y=0)

### ТЕКСТ ###

speed=pyglet.text.Label(str(0), x=0, y=50)
speed.color=(255,255,255,255)
speed.font_size=72

### МАССИВЫ ###

sprites=[background1, background2, road1, road2, speed, car.sprite]

moveObj1=[background1,road1]
moveObj2=[background2, road2]
decor=[]

for i in prange(10):
    i=pyglet.sprite.Sprite(rockImage1, x=-200, y=1000)
    sprites.append(i)
    decor.append(i)
for i in prange(10):
    i=pyglet.sprite.Sprite(treeImage1, x=-200, y=1000)
    sprites.append(i)
    decor.append(i)

if __name__=='__main__':
    print(sprites)