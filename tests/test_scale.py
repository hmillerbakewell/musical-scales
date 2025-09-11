"""Test the creation of scales."""

# import sys
# sys.path.append('./src')
# import musical_scales.musical_scales
import musical_scales
import pytest


def test_ionian():
    """Check that D major is correct."""
    scale_notes = musical_scales.scale("D")
    names = list(map(lambda note: note.midi, scale_notes))
    assert names == ["D3", "E3", "F#3", "G3", "A3", "B3", "C#4", "D4"]

def test_starting_octave():
    """Check that C major with given octave is correct."""
    scale_notes = musical_scales.scale("D", starting_octave=5)
    names = list(map(lambda note: note.midi, scale_notes))
    assert names == ["C5", "D5", "E5", "F5", "G5", "A5", "B5", "C6"]

def test_octaves():
    """Check that D major is correct with 2 octaves."""
    scale_notes = musical_scales.scale("D", octaves=2)
    names = list(map(lambda note: note.midi, scale_notes))
    assert names == ["D3", "E3", "F#3", "G3", "A3", "B3", "C#4", "D4", "E4", "F#4", "G4", "A4", "B4", "C#5", "D5"]

def test_blues():
    """Check that blues scale on C is correct."""
    scale_notes = musical_scales.scale("C","blues")
    names = list(map(lambda note: note.name, scale_notes))
    assert names == ["C", "D#", "F", "F#", "G", "A#", "C"]

def test_major():
    """'major' is a shorthand for ionian in our code."""
    assert musical_scales.scale("D") == musical_scales.scale("D","major")
