"""Retrieve a scale based on a given mode and starting note."""

import typing
import math


class MusicException(Exception):
    """Base exception for the musical_scales module."""

    pass


class Note:
    """A single note in a given octave, e.g. C#3.

    Measured as a number of semitones above Middle C;
        Note(0) # Middle C, i.e. C3
        Note(2) # D3
    """

    semitones_above_middle_c: int
    name: str
    octave: int

    def __init__(self, name: str = None, semitones_above_middle_c: int = None):
        """Create a note with a given name or degree.

        Examples:
            Note("C#")
            Note(semitones_above_middle_c = 1)
        """
        if name is not None:
            if name not in interval_from_names:
                raise MusicException(f"No note found with name {name}.")
            self._set_degree(interval_from_names[name])
        elif semitones_above_middle_c is not None:
            self._set_degree(semitones_above_middle_c)
        else:
            self._set_degree(0)

    def _set_degree(self, semitones_above_middle_c: int):
        """Set the note name and octave.

        Should only be used during initialisation.
        """
        self.semitones_above_middle_c = semitones_above_middle_c
        self.name = names_from_interval[semitones_above_middle_c % 12]
        self.octave = math.floor(semitones_above_middle_c / 12) + 3

    def __str__(self):
        """MIDI-style string representation e.g. C#3."""
        return self.midi

    def __repr__(self):
        """MIDI-style string representation e.g. C#3."""
        return self.midi

    @property
    def midi(self):
        """Note name and octave, e.g. C3."""
        return f"{self.name}{self.octave}"

    def __add__(self, shift: int):
        """Shifting this note's degree upwards."""
        return Note(semitones_above_middle_c=self.semitones_above_middle_c + shift)

    def __sub__(self, shift: int):
        """Shifting this note's degree downwards."""
        return self + (-shift)

    def __eq__(self, other):
        """Check equality via .midi."""
        if isinstance(other, Note):
            return self.midi == other.midi
        else:
            return self.midi == other or self.name == other


def scale(starting_note, mode="ionian", octaves=1):
    """Return a sequence of Notes starting on the given note in the given mode.

    Example:
        scale("C") # C major (ionian)
        scale(Note(4), "harmonic minor") # E harmonic minor
    """
    if mode not in scale_intervals:
        raise MusicException(f"The mode {mode} is not available.")
    if not isinstance(starting_note, Note):
        starting_note = Note(starting_note)
    notes = [starting_note]
    for octave in range(0,octaves):
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

names_from_interval = {
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
