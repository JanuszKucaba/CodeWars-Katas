"""
You are going to be given a word.

Your job is to return the middle character of the word.
If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.
#Input
A word (string) of length 0 < str < 1000.
You do not need to test for this.
This is only here to tell you that you do not need to worry about
your solution timing out.
#Output
The middle character(s) of the word represented as a string.
https://www.codewars.com/kata/56747fd5cb988479af000028
"""


# long version
def get_middle(word):
    """
    Input: word (string).

    Output: middle character(s) of the word
    """
    length = len(word)

    if length % 2 == 0:
        return word[int(length / 2) - 1: int(length / 2) + 1]
    return word[int(length / 2)]


# short version
def get_middle2(word):
    """
    Input: word (string).

    Output: middle character(s) of the word
    """
    return word[int((len(word) - 1) / 2): int(len(word) / 2) + 1]


if __name__ == '__main__':
    print(get_middle('test'))
    print(get_middle('testing'))
    print(get_middle('middle'))
    print(get_middle('A'))
    print(get_middle('of'))
    print()
    print(get_middle2('test'))
    print(get_middle2('testing'))
    print(get_middle2('middle'))
    print(get_middle2('A'))
    print(get_middle2('of'))
