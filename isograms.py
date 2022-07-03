"""
Isograms.

An isogram is a word that has no repeating letters, consecutive or
non-consecutive.
Implement a function that determines whether a string that contains only
letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.
https://www.codewars.com/kata/54ba84be607a92aa900000f1
"""


def is_isogram(string):
    """
    Input: string.

    Output: True/False depends string is isogram or not.
    """
    letters = {}

    for let in string.lower():
        if let in letters:
            letters[let] += 1
        else:
            letters[let] = 1

    for val in letters.values():
        if val > 1:
            return False
    return True


def is_isogram2(string):
    """
    Input: string.

    Output: True/False depends string is isogram or not.
    """
    return len(string) == len(set(string.lower()))


if __name__ == '__main__':
    print(is_isogram('Dermatoglyphics'))
    print(is_isogram('isogram'))
    print(is_isogram('aba'))
    print(is_isogram('moOse'))
    print(is_isogram('isIsogram'))
    print(is_isogram(''))
    print()
    print(is_isogram2('Dermatoglyphics'))
    print(is_isogram2('isogram'))
    print(is_isogram2('aba'))
    print(is_isogram2('moOse'))
    print(is_isogram2('isIsogram'))
    print(is_isogram2(''))
