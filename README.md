# MIDIML
#### [MIDIML](https://mattrmcg.github.io/midiml/) (MIDI Markup Language) is an xml-like DSL that provides an easier way to define MIDI files.

##### Define a `.midiml` file
`program.midiml`
```
<MIDIProgram>
    <Track tempo="100">
        <Notes duration="1" interval="1" vol="100" >
        50, 52, 54, 55, 57, 59, 61, 62, 64, 66, 64, 62, 61, 62, 61, 59
        </Notes>
    </Track>
    <Track tempo="100">
        <Notes duration="2" interval="4" vol="80">
        [50, 54, 57], [50, 54, 57], [52, 55, 59], [52, 55, 59], [50, 54, 61]
        </Notes>
    </Track>
</MIDIProgram>
```

##### Aim `midiml.py` at it
`midiml.py`
``midiml_mm = metamodel_from_file(join(this_folder, "midiml.tx"), debug=False)``

##### Generate a MIDI file
``python3 midiml.py``

You now have a multi-track `.mid` file that can be read by any midi synthesizer of your choice. I tested this using pygame's midi player:
``player.py``
```
import pygame

  

def play_music(midi_filename):

clock = pygame.time.Clock()

pygame.mixer.music.load(midi_filename)

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():

clock.tick(30)

  

def play(midi_filename):

# mixer config

freq = 44100 # audio CD quality

bitsize = -16 # unsigned 16 bit

channels = 2 # 1 is mono, 2 is stereo

buffer = 1024 # number of samples

pygame.mixer.init(freq, bitsize, channels, buffer)

  

# optional volume 0 to 1.0

pygame.mixer.music.set_volume(0.8)

  

# listen for interruptions

try:

# use the midi file you just saved

play_music(midi_filename)

except KeyboardInterrupt:

# if user hits Ctrl/C then exit

# (works only in console mode)

pygame.mixer.music.fadeout(1000)

pygame.mixer.music.stop()

raise SystemExit

  

play("./test.mid")
```

The interpreter makes use of the ``midiutil`` library to generate the MIDI file.

As for the midiml language itself, the ``<MIDIProgram>`` denotes the beginning and end of the program. 

``<Track>`` defines a MIDI track, in which you can specify the tempo
```
<Track tempo="100">
	...
</Tempo>
```

``<Notes>`` defines a note sequence, in which you can specify the duration, interval of time between, and volume of each note. These can either be comma separated single-note sequences (``50, 51, 52, 54, 56``) or comma separated chord sequences (``[50, 54, 57], [52, 56, 59]``)
