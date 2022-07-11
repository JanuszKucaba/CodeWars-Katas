"""
Stop gninnipS My sdroW.

Write a function that takes in a string of one or more words, and returns
the same string, but with all five or more letter words reversed.
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
https://www.codewars.com/kata/5264d2b162488dc400000001
"""


# long version
def spin_words(sentence):
    """
    Input: sentence (string).

    Output: the same string with all five or more letter words reversed.
    """
    res = []
    words = sentence.split(' ')

    for word in words:
        if len(word) >= 5:
            res.append(word[::-1])
        else:
            res.append(word)

    return ' '.join(res)


# long version
def spin_words_2(sentence):
    """
    Input: sentence (string).

    Output: the same string with all five or more letter words reversed.
    """
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split(' ')])


if __name__ == '__main__':
    print(spin_words('Welcome'))
    print(spin_words('to'))
    print(spin_words('CodeWars'))
    print(spin_words('Hey fellow warriors'))
    print(spin_words('This sentence is a sentence'))
    print()
    print(spin_words_2('Welcome'))
    print(spin_words_2('to'))
    print(spin_words_2('CodeWars'))
    print(spin_words('Hey fellow warriors'))
    print(spin_words('This sentence is a sentence'))
