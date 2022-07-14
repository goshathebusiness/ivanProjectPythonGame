import pyglet
from pyglet.window import key

pyglet.options['audio']=('openal', 'pulse', 'directsound', 'silent')

masterVolume=0.5
musicVolume=0.5
effectVolume=1

soundTest=pyglet.media.load('resources/sounds/sf2gt.mp3', streaming=False)
soundTest.volume=(masterVolume*musicVolume)

window = pyglet.window.Window(width=1200, height=900, caption="Sound test", resizable=False)
window.set_location(0, 30)

player=pyglet.media.Player()
player.volume=masterVolume*musicVolume

@window.event
def on_key_press(symbol, modifiers):
    if symbol==key.RIGHT:
        pass
    if symbol==key.LEFT:
        pass
    if symbol==key.SPACE:
        player.queue(soundTest)
        player.play()
    if symbol==key.UP:
        pass
    if symbol==key.DOWN:
        pass

@window.event
def on_key_release(symbol, modifiers):
    if symbol==key.RIGHT:
        pass
    if symbol==key.LEFT:
        pass
    if symbol==key.SPACE:
        player.pause()
        player.next_source()
    if symbol==key.UP:
        pass
    if symbol==key.DOWN:
        pass

def update(frame):
    pass
    

if __name__ == '__main__':
    
    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()