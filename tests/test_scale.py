"""Test the creation of scales."""

import musical_scales
import pytest


def test_ionian():
    """Check that D major is correct."""
    scale_notes = musical_scales.scale("D")
    names = list(map(lambda note: note.midi, scale_notes))
    assert names == ["D3", "E3", "F#3", "G3", "A3", "B3", "C#4", "D4"]

def test_blues():
    """Check that blues scale on C is correct."""
    scale_notes = musical_scales.scale("C","blues")
    names = list(map(lambda note: note.name, scale_notes))
    assert names == ["C", "D#", "F", "F#", "G", "A#", "C"]

def test_major():
    """'major' is a shorthand for ionian in our code."""
    assert musical_scales.scale("D") == musical_scales.scale("D","major")
