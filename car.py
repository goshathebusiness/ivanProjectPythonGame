import pyglet
import math
from sounds import *

carImage1=pyglet.image.load('resources/car1.png')
carImage2=pyglet.image.load('resources/car2.png')
carImage3=pyglet.image.load('resources/car3.png')
carImage4=pyglet.image.load('resources/car4.png')
carImage5=pyglet.image.load('resources/car5.png')
carImages=[carImage1, carImage2, carImage3, carImage4, carImage5] # текстурки используемые для машины, чтобы потом их удобно менять

for i in carImages:
    i.anchor_x=i.width//2
    i.anchor_y=i.height//2

class Car():
    sprite=pyglet.sprite.Sprite(carImage1, x=1200/2-carImage1.width/2, y=150)
    
    speed=0
    turnSpeed=(40-math.sqrt(math.ceil(speed)))
    rpm=0
    gear=1
    def __init__(self) -> None:
        pass
    def acceleration(self):
        if self.speed<self.maxSpeed:
            self.speed+=0.25
        self.rpmUpdate()
    def brake(self):
        if self.speed<0:
            self.speed=0
            return
        self.speed-=2
        self.rpmUpdate()
    def idle(self):
        if self.speed<0:
            self.speed=0
            return
        self.speed-=self.speed/2500
        self.rpmUpdate()
    def turnSpeedUpdate(self):
        self.turnSpeed=(math.sqrt(abs(self.speed))*20)
    def restart(self):
        self.sprite.x=1200/2-carImage1.width/2
        self.sprite.y=150
    def crash(self):
        self.gear=1
        self.speed=0
    def rpmUpdate(self):
        self.rpm=8000*(self.speed-(self.gear-1)*40)/40
        if self.speed>=self.gear*40 and self.gear<6:
            print(self.rpm)
            self.gear+=1
            gearPlayer.queue(gearSound)
            gearPlayer.play()
        elif self.speed<=(self.gear-1)*40 and self.gear>1:
            print(self.rpm)
            self.gear-=1
            gearPlayer.queue(gearSound)
            gearPlayer.play()
        elif self.rpm<0:
            self.rpm=1
        self.maxSpeed=self.gear*40
        enginePlayer.pitch=abs((self.rpm/8000)+1)
    def rpmRotation(self):
        if self.rpm>4000:
            rpmTemp=self.rpm-4000
        else:
            rpmTemp=self.rpm
        degrees=(rpmTemp*115)/4000
        if self.rpm<4000:
            return degrees-115
        else:
            return degrees

car=Car()