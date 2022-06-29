"""
Trolls are attacking your comment section.

A common way to deal with this situation is to remove all of the vowels
from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new
string with all vowels removed.
For example, the string "This website is for losers LOL!" would become
"Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.
https://www.codewars.com/kata/52fba66badcd10859f00097e
"""


# long version
def disemvowel(string_):
    """
    Input: sentence.

    Output: sentence without vowels
    """
    vowels = 'aeiou'
    res = ''
    for let in string_:
        if let.lower() not in vowels:
            res += let
    return res


# short version
def disemvowel2(string_):
    """
    Input: sentence.

    Output: sentence without vowels
    """
    return ''.join(let for let in string_ if let.lower() not in 'aeiou')


if __name__ == '__main__':
    print(disemvowel("This website is for losers LOL!"))
    print()
    print(disemvowel2("This website is for losers LOL!"))
