"""
Jaden Casing Strings.

Your task is to convert strings to how they would be written by Jaden Smith.
The strings are actual quotes from Jaden Smith, but they are not capitalized
in the same way he originally typed them.
https://www.codewars.com/kata/5390bac347d09b7da40006f6
"""


# long version
def to_jaden_case(string):
    """
    Input: sentence.

    Output: every word in sentence with capital first letter.
    """
    words = string.split(' ')
    words_list = []
    for word in words:
        words_list.append(word.capitalize())

    return ' '.join(words_list)


# short version
def to_jaden_case2(string):
    """
    Input: sentence.

    Output: every word in sentence with capital first letter.
    """
    return ' '.join([word.capitalize() for word in string.split(' ')])


if __name__ == '__main__':
    print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
    print()
    print(to_jaden_case2("How can mirrors be real if our eyes aren't real"))
