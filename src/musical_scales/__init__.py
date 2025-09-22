"""Retrieve a scale based on a given mode and starting note."""

import math
import re


class MusicException(Exception):
    """Base exception for the musical_scales module."""

    pass


PATTERN = re.compile(r"^([A-Ga-g])([#b]?)(-?\d*)$")


def parse_compound_note_name(name: str):
    """Parse a compound note name e.g. C#4 into its components.

    Returns:
        (str, int): The note name and octave.
    """

    name = name.strip()
    name = name[0].upper() + name[1:]
    name = name.replace("♯", "#").replace("♭", "b")
    match = PATTERN.match(name)
    if not match:
        raise MusicException(f"The note name {name} is not valid. Expected forms are like 'C#' or 'C#4'.")
    name = match.group(1) + match.group(2)
    octave = match.group(3)
    if name not in interval_from_names:
        raise MusicException(f"No note found with name {name}. Expected A-G with optional # or b.")
    if octave == "":
        octave = 3
    else:
        octave = int(octave)
    return name, octave


class Note:
    """A single note in a given octave, e.g. C#3.

    Measured as a number of semitones above Middle C:
        * Note(0) # Middle C, i.e. C3
        * Note(2) # D3

    semitones_above_middle_c is the single source of truth.
    """

    semitones_above_middle_c: int

    def __init__(self, name_or_interval: str | int):
        """Create a note with a given name or degree.

        Examples:
            * Note("C#")
            * Note(semitones_above_middle_c = 1)
        """
        if isinstance(name_or_interval, str):
            name, octave = parse_compound_note_name(name_or_interval)
            self.semitones_above_middle_c = interval_from_names[name] + (
                (octave - 3) * 12)
        elif isinstance(name_or_interval, int):
            self.semitones_above_middle_c = name_or_interval
        else:
            self.semitones_above_middle_c = 0

    def __str__(self):
        """MIDI-style string representation e.g. C#3."""
        return self.midi

    def __repr__(self):
        """MIDI-style string representation e.g. C#3."""
        return self.midi

    @property
    def name(self):
        """Name of the note, e.g. C#. Favours sharps.

        Favours sharps for consistenct, see `enharmonic` for flats."""
        return names_from_interval_favour_sharps[self.semitones_above_middle_c % 12]

    @property
    def octave(self):
        """Get the octave of the note."""
        return self.semitones_above_middle_c // 12 + 3

    @property
    def midi(self) -> str:
        """Note name and octave, sutiable for MIDI software, e.g. C3.

        Favours sharps.
        """
        return f"{self.name}{self.octave}"

    @property
    def enharmonic(self) -> str:
        """Note name and octave, but favouring flats e.g. Bb."""
        return names_from_interval_favour_flats[self.semitones_above_middle_c % 12]

    def __add__(self, shift: int):
        """Shifting this note's degree upwards."""
        return Note(name_or_interval=self.semitones_above_middle_c + shift)

    def __sub__(self, shift: int):
        """Shifting this note's degree downwards."""
        return self + (-shift)

    def __eq__(self, other):
        """Check equality via interval, or by midi representation."""
        if isinstance(other, Note):
            return self.semitones_above_middle_c == other.semitones_above_middle_c
        else:
            return str(self) == str(other)

def scale(starting_note: Note | str | int, mode="ionian", *, octaves=1):
    """Return a sequence of Notes starting on the given note in the given mode.

    Example:
        * scale("C3") # C major (ionian) starting on middle C
        * scale(Note(4), "harmonic minor") # E harmonic minor
    """
    if mode not in scale_intervals:
        raise MusicException(f"The mode {mode} is not available.")
    if not isinstance(starting_note, Note):
        starting_note = Note(starting_note)
    notes = [starting_note]
    for _ in range(0, octaves):
        for interval in scale_intervals[mode]:
            notes.append(notes[-1] + interval)
    return notes


# Found at https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes
# Only scales that include a representation given
# by semi-tone intervals are included.
# One alteration is that this repository will use the term "Romani"
scale_intervals = {
    "acoustic": [2, 2, 2, 1, 2, 1, 2],
    "aeolian": [2, 1, 2, 2, 1, 2, 2],
    "algerian": [2, 1, 3, 1, 1, 3, 1, 2, 1, 2],
    "super locrian": [1, 2, 1, 2, 2, 2, 2],
    "augmented": [3, 1, 3, 1, 3, 1],
    "bebop dominant": [2, 2, 1, 2, 2, 1, 1, 1],
    "blues": [3, 2, 1, 1, 3, 2],
    "chromatic": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "dorian": [2, 1, 2, 2, 2, 1, 2],
    "double harmonic": [1, 3, 1, 2, 1, 3, 1],
    "enigmatic": [1, 3, 2, 2, 2, 1, 1],
    "flamenco": [1, 3, 1, 2, 1, 3, 1],
    "romani": [2, 1, 3, 1, 1, 2, 2],
    "half-diminished": [2, 1, 2, 1, 2, 2, 2],
    "harmonic major": [2, 2, 1, 2, 1, 3, 1],
    "harmonic minor": [2, 1, 2, 2, 1, 3, 1],
    "hijaroshi": [4, 2, 1, 4, 1],
    "hungarian minor": [2, 1, 3, 1, 1, 3, 1],
    "hungarian major": [3, 1, 2, 1, 2, 1, 2],
    "in": [1, 4, 2, 1, 4],
    "insen": [1, 4, 2, 3, 2],
    "ionian": [2, 2, 1, 2, 2, 2, 1],
    "iwato": [1, 4, 1, 4, 2],
    "locrian": [1, 2, 2, 1, 2, 2, 2],
    "lydian augmented": [2, 2, 2, 2, 1, 2, 1],
    "lydian": [2, 2, 2, 1, 2, 2, 1],
    "locrian major": [2, 2, 1, 1, 2, 2, 2],
    "pentatonic major": [2, 2, 3, 2, 3],
    "melodic minor ascending": [2, 1, 2, 2, 2, 2, 1],
    "melodic minor descending": [2, 1, 2, 2, 2, 2, 1],
    "pentatonic minor": [3, 2, 2, 3, 2],
    "mixolydian": [2, 2, 1, 2, 2, 1, 2],
    "neapolitan major": [1, 2, 2, 2, 2, 2, 1],
    "neapolitan minor": [1, 2, 2, 2, 1, 3, 1],
    "octatonic c-d": [2, 1, 2, 1, 2, 1, 2, 1],
    "octatonic c-c#": [1, 2, 1, 2, 1, 2, 1],
    "persian": [1, 3, 1, 1, 2, 3, 1],
    "phrygian dominant": [1, 3, 1, 2, 1, 2, 2],
    "phrygian": [1, 2, 2, 2, 1, 2, 2],
    "prometheus": [2, 2, 2, 3, 1, 2],
    "harmonics": [3, 1, 1, 2, 2, 3],
    "tritone": [1, 3, 2, 1, 3, 2],
    "two-semitone tritone": [1, 1, 4, 1, 1, 4],
    "ukranian dorian": [2, 1, 3, 1, 2, 1, 2],
    "whole-tone scale": [2, 2, 2, 2, 2, 2],
    "yo": [3, 2, 2, 3, 2]
}

scale_intervals["major"] = scale_intervals["ionian"]

names_from_interval_favour_sharps = {
    0: "C",
    1: "C#",
    2: "D",
    3: "D#",
    4: "E",
    5: "F",
    6: "F#",
    7: "G",
    8: "G#",
    9: "A",
    10: "A#",
    11: "B"
}
"""From an interval give the note name, favouring sharps over flats."""


names_from_interval_favour_flats = {
    0: "C",
    1: "Db",
    2: "D",
    3: "Eb",
    4: "E",
    5: "F",
    6: "Gb",
    7: "G",
    8: "Ab",
    9: "A",
    10: "Bb",
    11: "B"
}
"""From an interval give the note name, favouring sharps over flats."""


interval_from_names = {
    "C": 0,
    "C#": 1,
    "Db": 1,
    "D": 2,
    "D#": 3,
    "Eb": 3,
    "E": 4,
    "Fb": 4,
    "E#": 5,
    "F": 5,
    "F#": 6,
    "Gb": 6,
    "G": 7,
    "G#": 8,
    "Ab": 8,
    "A": 9,
    "A#": 10,
    "Bb": 10,
    "B": 11,
    "Cb": 11,
    "B#": 0
}
"""Dictionary from note names to number of semitones above C."""

# MIT License

"""
The MIT License (MIT)

Copyright (c) 2021 Hector Miller-Bakewell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
