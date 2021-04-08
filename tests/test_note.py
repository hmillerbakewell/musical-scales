"""Test the creation of notes."""

import musical_scales
import pytest

def test_middle_c():
    """Test creation of C3."""
    c_3 = musical_scales.Note("C")
    assert c_3.name == "C"
    d_3 = c_3+2
    assert d_3.name == "D"
    b_2 = c_3 -1
    assert b_2.name == "B"

def test_equality():
    """Notes should compare permissively."""
    assert musical_scales.Note("C") == musical_scales.Note("C")
    assert musical_scales.Note("C") == "C3"
    assert musical_scales.Note("C") == "C"