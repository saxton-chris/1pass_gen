import string   # Provides string constants (letters, digits, punctuation, etc.)
import secrets  # Used for generating secure random choices
from password_manager import config  # Custom module (assumed to contain DEFAULT_LENGTH configuration)

def password_gen(pass_len: int = config.DEFAULT_LENGTH,
                 upper: bool = True,
                 lower: bool = True,
                 numbers: bool = True,
                 specail: bool = True,
                 space: bool = False) -> str:
    """
    Generates a secure random password with the specified length.

    Parameters:
    pass_len (int): The length of the generated password. Defaults to config.DEFAULT_LENGTH.

    Returns:
    str: A randomly generated password containing letters, digits, punctuation, and spaces.
    """
    character = ''
    if upper:
        character += string.ascii_uppercase
    if lower:
        character += string.ascii_lowercase
    if numbers:
        character += string.digits
    if specail:
        character += string.punctuation
    if space:
        character += ' '

    # Generate a random password of the specified length using secrets.choice for better security
    password = ''.join(secrets.choice(character) for _ in range(pass_len))
    
    return password  # Return the generated password
