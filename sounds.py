import pyglet
from pyglet.window import key

pyglet.options['audio']=('openal', 'pulse', 'directsound', 'silent')

masterVolume=0.5
musicVolume=0.1
effectVolume=0.5

soundTest=pyglet.media.load('resources/sounds/sf2gt.mp3', streaming=False)
outoftouchSound=pyglet.media.load('resources/sounds/outoftouch.mp3', streaming=False)
engineSound=pyglet.media.load('resources/sounds/engine.wav', streaming=False)

music=[soundTest, outoftouchSound]
effects=[engineSound]

def volumeCorrection():
    for i in music:
        i.volume=(masterVolume*musicVolume)
    for i in effects:
        i.volume=(masterVolume*effectVolume)

#volumeCorrection()
player=pyglet.media.Player()
player.volume=masterVolume*musicVolume

def musicPlayer():
    player.queue(outoftouchSound)
    player.play()

if __name__ == '__main__':
    pass