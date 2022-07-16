"""
Simple Pig Latin.

Move the first letter of each word to the end of it,
then add "ay" to the end of the word.
Leave punctuation marks untouched.
Examples:
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
https://www.codewars.com/kata/520b9d2ad5c005041100000f
"""
import string


# long version
def pig_it(text):
    """
    Input: text (string).

    Output: text with changed words: first letter at the end with added 'ay'.
    """
    new_list = []
    for word in text.split(' '):
        if word in string.punctuation:
            text = word
        else:
            text = word[1:] + word[0] + 'ay'
        new_list.append(text)

    return ' '.join(new_list)


# short version
def pig_it_2(text):
    """
    Input: text (string).

    Output: text with changed words: first letter at the end with added 'ay'.
    """
    return ' '.join([word[1:] + word[0] + 'ay' if word.isalnum() else word for word in text.split(' ')])


if __name__ == '__main__':
    print(pig_it('Pig latin is cool'))
    print(pig_it('This is my string'))
    print()
    print(pig_it_2('Pig latin is cool'))
    print(pig_it_2('This is my string'))
