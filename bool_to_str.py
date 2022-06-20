"""
Complete the method that takes a boolean value.
Return a "Yes" string for true,or a "No" string for false.
https://www.codewars.com/kata/53369039d7ab3ac506000467
"""


def bool_to_word(boolean):
    """Take boolean variable.
    Return text Yes or No.
    """
    return "Yes" if boolean else "No"


if __name__ == '__main__':
    print(bool_to_word(True))
    print(bool_to_word(False))
