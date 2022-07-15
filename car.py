import pyglet
import math

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
    
    speed=250
    turnSpeed=(40-math.sqrt(math.ceil(speed)))
    rpm=2000
    gear=1
    def __init__(self) -> None:
        pass
    def acceleration(self):
        self.speed+=30-math.sqrt(abs(self.speed))
        self.rpmUpdate(50)
    def brake(self):
        if self.speed<0:
            self.speed=0
            return
        self.speed-=(1000+math.ceil(abs(self.speed)))/100
        self.rpmUpdate(-200)
    def idle(self):
        if self.speed<0:
            self.speed=0
            return
        self.speed-=self.speed/2500
        self.rpmUpdate(-25)
    def turnSpeedUpdate(self):
        self.turnSpeed=(math.sqrt(abs(self.speed))*10)
    def restart(self):
        self.sprite.x=1200/2-carImage1.width/2
        self.sprite.y=150
    def crash(self):
        self.speed=0
    def rpmUpdate(self, change):
        self.rpm+=change
        if self.rpm>8000 and self.gear<6:
            self.gear+=1
            self.rpm=2500
        elif self.rpm<2000 and self.gear>1:
            self.gear-=1
            self.rpm=7500
        elif self.rpm<0:
            self.rpm=0


car=Car()