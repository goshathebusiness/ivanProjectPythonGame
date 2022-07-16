import pyglet

pyglet.options['audio']=('openal', 'pulse', 'directsound', 'silent')

masterVolume=1
musicVolume=0.05
effectVolume=0.05

soundTest=pyglet.media.load('resources/sounds/sf2gt.mp3', streaming=False)
outoftouchSound=pyglet.media.load('resources/sounds/outoftouch.mp3', streaming=False)
engineSound=pyglet.media.load('resources/sounds/enginetruck.wav', streaming=False)
gearSound=pyglet.media.load('resources/sounds/gear.wav', streaming=False)

music=[soundTest, outoftouchSound]
effects=[engineSound, gearSound]

musicPlayer=pyglet.media.Player()
musicPlayer.volume=masterVolume*musicVolume

enginePlayer=pyglet.media.Player()
enginePlayer.volume=masterVolume*effectVolume
enginePlayer.loop=True

gearPlayer=pyglet.media.Player()
gearPlayer.volume=masterVolume*effectVolume

def musicStart():
    musicPlayer.queue(outoftouchSound)
    musicPlayer.play()

def engineStart():
    enginePlayer.queue(engineSound)
    enginePlayer.play()

if __name__ == '__main__':
    pass