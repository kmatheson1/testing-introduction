# File: tests/test_string_builder.py
from lib.string_builder import *

def test_string_builder_empty_string():
    string_builder = StringBuilder()
    string_builder.add("")
    result = string_builder.output()
    assert result == ""

def test_string_builder_create_string():
    string_builder = StringBuilder()
    string_builder.add("Hello ")
    string_builder.add("World")

    result = string_builder.output()
    assert result == "Hello World"

def test_string_builder_size():
    string_builder = StringBuilder()
    string_builder.add("Hello ")
    string_builder.add("World")

    result = string_builder.size()
    assert result == 11

def test_adding_multiple_strings_has_total_size():
    string_builder = StringBuilder()
    string_builder.add("Hello ")
    string_builder.add("World")

    result = string_builder.size()
    assert result == 11