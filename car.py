import pyglet
import math

carImage1=pyglet.image.load('resources/car1.png')
carImage2=pyglet.image.load('resources/car2.png')
carImage3=pyglet.image.load('resources/car3.png')
carImages=[carImage1, carImage2, carImage3] # текстурки используемые для машины, чтобы потом их удобно менять

for i in carImages:
    i.anchor_x=i.width//2
    i.anchor_y=i.height//2

class Car():
    sprite=pyglet.sprite.Sprite(carImage1, x=1200/2-carImage1.width/2, y=150)
    
    speed=250
    turnSpeed=(40-math.sqrt(math.ceil(speed)))
    def __init__(self) -> None:
        pass
    def acceleration(self):
        self.speed+=30-math.sqrt(abs(self.speed))
    def brake(self):
        if self.speed<0:
            self.speed=0
            return
        self.speed-=(1000+math.ceil(abs(self.speed)))/100
    def idle(self):
        if self.speed<0:
            self.speed=0
            return
        self.speed-=self.speed/2500
    def turnSpeedUpdate(self):
        self.turnSpeed=(40+math.sqrt(abs(self.speed)))


car=Car()