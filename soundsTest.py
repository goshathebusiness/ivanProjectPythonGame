import pyglet
from pyglet.window import key

pyglet.options['audio']=('openal', 'pulse', 'directsound', 'silent')

masterVolume=0.5
musicVolume=0.5
effectVolume=1

soundTest=pyglet.media.load('resources/sounds/sf2gt.mp3', streaming=False)
engineSound=pyglet.media.load('resources/sounds/engine.wav', streaming=False)
soundTest.volume=(masterVolume*musicVolume)

window = pyglet.window.Window(width=1200, height=900, caption="Sound test", resizable=False)
window.set_location(0, 30)

player=pyglet.media.Player()
player.volume=masterVolume*musicVolume

up=False
down=False

@window.event
def on_key_press(symbol, modifiers):
    global up, down
    
    if symbol==key.RIGHT:
        player.queue(engineSound)
        player.play()
        player.loop=True
    if symbol==key.LEFT:
        pass
    if symbol==key.SPACE:
        player.queue(soundTest)
        player.play()
    if symbol==key.UP:
        up=True
    if symbol==key.DOWN:
        down=True

@window.event
def on_key_release(symbol, modifiers):
    global up, down
    
    if symbol==key.RIGHT:
        pass
    if symbol==key.LEFT:
        pass
    if symbol==key.SPACE:
        player.pause()
        player.next_source()
    if symbol==key.UP:
        up=False
    if symbol==key.DOWN:
        down=False

def pitch():
    global up
    if up==True and player.pitch<2:
        player.pitch+=0.02
    elif down==True and player.pitch>1:
        player.pitch-=0.04
    if player.pitch<0:
        player.pitch+=0.01

def update(frame):
    pitch()
    

if __name__ == '__main__':
    
    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()