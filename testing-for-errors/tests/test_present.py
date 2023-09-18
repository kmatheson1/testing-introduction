# File: tests/test_present.py
import pytest
from lib.present import *

"""
When we wrap an item
We get it back when unwrapping
"""
def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(3)
    assert present.unwrap() == 3

"""
If we unwrap before wrapping
We get an error message
"""
def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."

"""
If we try to wrap an already-wrapped present
we get an error message
"""
def test_wrapping_already_wrapped_throws_error():
    present = Present()
    present.wrap(4)
    with pytest.raises(Exception) as e:
        present.wrap(4)
    message = str(e.value)
    assert message == "A contents has already been wrapped."

"""
If we try to wrap an already wrapped present
The first wrapped value is unchanged
"""
def test_wrapping_already_wrapped_preserves_value():
    present = Present()
    present.wrap(4)
    with pytest.raises(Exception) as e:
        present.wrap(6)
    assert present.unwrap() == 4