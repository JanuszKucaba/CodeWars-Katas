"""
Create a function that removes the first and last characters of a string.

You're given one parameter, the original string.
You don't have to worry with strings with less than two characters.
https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
"""


def remove_char(string):
    """
    input: string.

    output: string without first and last character
    """
    return string[1:-1]


def remove_char2(string):
    """
    input: string.

    output: string without first and last character
    """
    new_str = ''
    for idx, let in enumerate(string):
        if idx != 0 and idx != len(string) - 1:
            new_str += let
    return new_str


if __name__ == '__main__':
    print(remove_char('eloquent'))
    print(remove_char('country'))
    print(remove_char('person'))
    print(remove_char('place'))
    print(remove_char('ok'))
    print(remove_char('ooopsss'))
    print()
    print(remove_char2('eloquent'))
    print(remove_char2('country'))
    print(remove_char2('person'))
    print(remove_char2('place'))
    print(remove_char2('ok'))
