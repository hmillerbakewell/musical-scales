"""Test the creation of notes."""

import sys
sys.path.append('./src')

import musical_scales

def test_regex():
    parse = musical_scales.parse_compound_note_name
    assert parse("C") == ("C", 3)
    assert parse("C3") == ("C", 3)
    assert parse("C4") == ("C", 4)
    assert parse("C#") == ("C#", 3)
    assert parse("C#0") == ("C#", 0)
    assert parse("Eb-1") == ("Eb", -1)

def test_middle_c():
    """Test creation of middle C."""
    by_name_no_octave = musical_scales.Note("C")
    by_name_with_octave = musical_scales.Note("C3")
    by_integer = musical_scales.Note(0)
    for note in (by_name_no_octave, by_name_with_octave, by_integer):
        print(note)
        assert note.octave == 3
        assert note.name == "C"
        assert note.semitones_above_middle_c == 0
        assert str(note) == "C3"
        assert repr(note) == "C3"
        assert note.midi == "C3"

def test_interval_shifts():
    """Test creation of C3 and above."""
    c_3 = musical_scales.Note("C")
    assert c_3.octave == 3
    assert c_3.name == "C"
    d_3 = c_3+2
    assert d_3.name == "D"
    b_2 = c_3 -1
    assert b_2.name == "B"

def test_enharmonic():
    """Test enharmonic names."""
    a_sharp = musical_scales.Note("A#3")
    b_flat = musical_scales.Note("Bb3")
    assert a_sharp == b_flat
    assert a_sharp.name == "A#"
    assert b_flat.name == "A#"
    assert a_sharp.enharmonic == "Bb"
    assert b_flat.enharmonic == "Bb"

def note_from_compound_name():
    """Create notes from compound names."""
    assert musical_scales.Note("C") == musical_scales.Note("C3")
    assert musical_scales.Note("C4").semitones_above_middle_c == 12
    assert musical_scales.Note("D5").semitones_above_middle_c == 26
    assert musical_scales.Note("A#3").semitones_above_middle_c == 10
    assert musical_scales.Note("Bb1").semitones_above_middle_c == -14


def test_equality():
    """Notes should compare permissively."""
    assert musical_scales.Note("C") == musical_scales.Note("C")
    assert musical_scales.Note("C") == "C3"

def test_emojify():
    """Test conversion of # and b to emoji equivalents."""
    assert musical_scales.emojify_accidentals("C#") == "C♯"
    assert musical_scales.emojify_accidentals("Db") == "D♭"
    assert musical_scales.emojify_accidentals("E") == "E"