# All pitches to be calculated (in Hz).
pitches = [240, 140]

# Calculate
import math
import os

os.system("cls")
for pitch in pitches:
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "B#"]

    midiNote = round(12 * math.log2(pitch / 440) + 69)
    octave = int(midiNote / 12) 
    note = int(midiNote % 12)

    print(str(pitch) + " Hz: " + notes[note] + str(octave))