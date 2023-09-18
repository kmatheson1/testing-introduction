# File: tests/test_counter.py
from lib.counter import *

def test_counter_adds_one():
    counter = Counter()
    counter.add(1)

    result = counter.report()
    assert result == "Counted to 1 so far."

def test_counter_adds_five():
    counter = Counter()
    counter.add(5)

    result = counter.report()
    assert result == "Counted to 5 so far."