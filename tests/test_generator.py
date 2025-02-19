import pytest
import string
from password_manager import config
from password_manager import generator as gen

def test_password_length():
    """Test if the generated password has the correct length."""
    length = 24
    password = gen.password_gen(length)
    assert len(password) == length

def test_password_default_length():
    """Test if the function uses the default length from config."""
    password = gen.password_gen()
    assert len(password) == config.DEFAULT_LENGTH

def test_password_character_set():
    """Ensure all characters in the password are from the allowed set."""
    allowed_chars = string.ascii_letters + string.punctuation + string.digits + ' '
    password = gen.password_gen(20)
    assert all(char in allowed_chars for char in password)

def test_password_uniqueness():
    """Generate multiple passwords and check if they are unique."""
    passwords = {gen.password_gen(20) for _ in range(10)}
    assert len(passwords) == 10  # If all are unique, length should match

def test_no_uppercase():
    no_upper_pass = gen.password_gen(upper=False, space=True)  # Generate password without uppercase letters
    assert all(char not in string.ascii_uppercase for char in no_upper_pass)

def test_no_lowercase():
    no_lower_pass = gen.password_gen(lower=False, space=True)  # Generate password without lower letters
    assert all(char not in string.ascii_lowercase for char in no_lower_pass)

def test_no_number():
    no_number = gen.password_gen(numbers=False, space=True)  # Generate password without number
    assert all(char not in string.digits for char in no_number)

def test_no_punctuation():
    no_punc_pass = gen.password_gen(specail=False, space=True)  # Generate password without punctuation
    assert all(char not in string.punctuation for char in no_punc_pass)

def test_no_space():
    passwords = {gen.password_gen(50, space=False) for _ in range(20)}  # Generate multiple passwords with space=False
    assert all(' ' not in password for password in passwords)
