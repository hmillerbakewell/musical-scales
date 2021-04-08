# Musical Scales

Retrieve a scale based on a given mode and starting note.
Information about these scales can be found [on Wikipedia](https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes).

Currently supported scales:
 - acoustic
 - aeolian
 - algerian
 - super locrian
 - augmented
 - bebop dominant
 - blues
 - chromatic
 - dorian
 - double harmonic
 - enigmatic
 - flamenco
 - romani
 - half-diminished
 - harmonic major
 - harmonic minor
 - hijaroshi
 - hungarian minor
 - hungarian major
 - in
 - insen
 - ionian
 - iwato
 - locrian
 - lydian augmented
 - lydian
 - locrian major
 - pentatonic major
 - melodic minor ascending
 - melodic minor descending
 - pentatonic minor
 - mixolydian
 - neapolitan major
 - neapolitan minor
 - octatonic c-d
 - octatonic c-c#
 - persian
 - phrygian dominant
 - phrygian
 - prometheus
 - harmonics
 - tritone
 - two-semitone tritone
 - ukranian dorian
 - whole-tone scale
 - yo

## The Note class

Notes can be specified with either a name or a given number of semitones above middle C (C3).
Octaves are done MIDI-style, so B2 is immediately followed by C3.
Example notes:
 - `Note("D")` the first D above middle C
 - `Note(2)` two semitones above middle C, which is the same as `Note("D")`.

Notes have two fundamental properties:
 - `.name` e.g. "C"
 - `.octave` e.g. 3

You can retrieve both together MIDI style with:
 - `.midi` e.g. "F#4"

You can add an integer to a note to raise it by that many semitones:
 - `Note("C") + 12` the first C above middle C

## Examples
````py
musical_scales.scale("D")
# [D3, E3, F#3, G3, A3, B3, C#4, D4]
musical_scales.scale("F#", "blues")
# [F#3, A3, B3, C4, C#4, E4, F#4]
````
