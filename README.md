# 1Password Password Integration

This is going to be a simple program to generate complex passwords. The UI will allow the user to enter the length of the password the want and will generate a password comprised of random letters, numbers, and puncuation.

Once the password is generated the user will have the option to copy the password and enter it in their browser. The final step will be to allow the user to enter their username and the site it is for and create a new record in 1Password

## Generate Password

I first created a simple password generator using the `string` and `secrets` modules. I created a list of possible characters that includes

1. Uppercase Letters
2. Lowercase Letters
3. Punctuation
4. Space

The `password_gen` function takes in a password length and uses the `secrets` module to randomly select characters to make a string of the correct length.
