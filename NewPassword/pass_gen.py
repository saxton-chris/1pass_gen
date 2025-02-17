import string
import secrets

def gen_pass(pwd_length: int,
             allow_cap = True,
             allow_lower = True,
             allow_space = True,
             banned_punc = '',
             allowed_punc = string.punctuation) -> str:
    characters = string.digits + string.punctuation + string.ascii_letters + ' '
    password = ''.join(secrets.choice(characters) for _ in range(pwd_length))
    print(password)
