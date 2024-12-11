from textx import metamodel_from_file
from textx.export import metamodel_export, model_export
from os.path import dirname, join
from midiutil import MIDIFile
from typing import List

class Program:
    def __init__(self):
        self.trackCount = 0
    
    def __str__(self):
        return f"track count is {self.trackCount}"
    
    def interpret(self, model):

        print("interpreting...")

        self.trackCount = len(model.tracks)

        MyMIDI = MIDIFile(self.trackCount)

        
        for i, t in enumerate(model.tracks):
            time = 0
            if t.tempoArg != 0:
                MyMIDI.addTempo(i, 0, int(t.tempoArg.strArg))
            else:
                MyMIDI.addTempo(i, 0, 100)

            for j, nl in enumerate(t.notes):

                for ch in nl.chords:
                    for n in ch.chord:
                        MyMIDI.addNote(i, 0, n, time, int(nl.durationArg.strArg), int(nl.volArg.strArg))
                    time += int(nl.noteIntervalArg.strArg)

                for n in nl.nums:
                    # MyMIDI.addNote(track,channel,pitch,time,duration,volume)
                    MyMIDI.addNote(i, 0, n, time, int(nl.durationArg.strArg), int(nl.volArg.strArg))
                    time += int(nl.noteIntervalArg.strArg)
            
        
        with open("test.mid", "wb") as output_file:
            MyMIDI.writeFile(output_file)



def main():
    this_folder = dirname(__file__)

    midiml_mm = metamodel_from_file(join(this_folder, "midiml.tx"), debug=False)
    # metamodel_export(midiml_mm, join(this_folder, 'mml_meta.dot'))

    midiml_model = midiml_mm.model_from_file(join(this_folder, 'program.midiml'))
    # model_export(midiml_model, join(this_folder), 'program1.dot')

    prgm = Program()
    prgm.interpret(midiml_model)


if __name__ == "__main__":
    main()