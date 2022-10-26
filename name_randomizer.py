from string import ascii_letters
from random import choice

def get_name():
    """
    Creates a string of 10 random letters in case the user doesn't specify a name for the file.
    """

    name = ""

    return name.join(choice(ascii_letters) for _ in range(10))
