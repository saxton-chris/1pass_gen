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

# if __name__ == "__main__":
#     pytest.main()
