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
 - `.name` e.g. `"C"`
 - `.octave` e.g. `3`

You can retrieve both together MIDI style with:
 - `.midi` e.g. "F#4"

You can add an integer to a note to raise it by that many semitones:
 - `Note("C") + 12` the first C above middle C

## Examples
````python
import musical_scales

# Notes

# Middle C. If no octave name is provided then defaults to octave 3.
C3 = musical_scales.Note("C")
musical_scales.Note("C3")

# Or specify by interval above/below Middle C
C3 = musical_scales.Note(0)
C4 = musical_scales.Note(12)

D_sharp = musical_scales.Note(3)

# You can add / subtract integers from notes to shift them
assert C3 = D_sharp - 3

# Scales

# Defaults to a major scale
musical_scales.scale("D")
# [D3, E3, F#3, G3, A3, B3, C#4, D4]

# Or specify a name from musical_scales.scale_intervals.keys()
musical_scales.scale("F#", "blues")
# [F#3, A3, B3, C4, C#4, E4, F#4]

# Specify a starting octave for the note (defaults to 3)
musical_scales.scale("D5")
# [D5, E5, F#5, G5, A5, B5, C#6, D6]

# Specify how many octaves to output (keyword required)
musical_scales.scale("F#", "blues", octaves=2)
# [F#3, A3, B3, C4, C#4, E4, F#4, A4, B4, C5, C#5, E5, F#5]
````


## Documentation

Detailed documentation can be found at [readthedocs.io](https://musical-scales.readthedocs.io/en/latest/) as well as
in the docstrings of the python files themselves.

## Licensing

The source code is available under the MIT licence and can be found
on [Hector Miller-Bakewell's github](https://github.com/hmillerbakewell/musical-scales).

## Acknowledgements

This package was created as part of the [QuTune Project](https://iccmr-quantum.github.io/).

