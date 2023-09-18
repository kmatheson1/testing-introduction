# File: tests/test_password_checker.py
import pytest
from lib.password_checker import *

"""
if the password used is equal to 8 characters
"""
def test_password_len_at_least_8():
    password_checker = PasswordChecker()
    assert password_checker.check("password") == True

"""
if the password used is greather than 8 characters
"""
def test_password_len_greater_than_8():
    password_checker = PasswordChecker()
    assert password_checker.check("password1") == True

"""
If password used is less than 8 characters
"""
def test_password_len_less_than_8_throws_error():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("passwor")
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."

