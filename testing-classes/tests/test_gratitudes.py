# File: tests/test_gratitudes.py
from lib.gratitudes import *

def test_empty_string():
    gratitudes = Gratitudes()
    gratitudes.add("")

    assert gratitudes.format() == "Be grateful for: "

def test_one_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("Family")

    assert gratitudes.format() == "Be grateful for: Family"

def test_multiple_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("Family")
    gratitudes.add("Health")
    gratitudes.add("Fortune")

    assert gratitudes.format() == "Be grateful for: Family, Health, Fortune"