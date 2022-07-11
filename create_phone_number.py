"""
Create Phone Number.

Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) #
=> returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
"""


# long version
def create_phone_number(number):
    """
    Input: list of numbers.

    Output: string with the form of a phone number.
    """
    res = ''
    for idx, num in enumerate(number):
        num = str(num)
        if idx == 0:
            res += f'({num}'
        elif idx == 2:
            res += f'{num}) '
        elif idx == 5:
            res += f'{num}-'
        else:
            res += num

    return res


# short version
def create_phone_number_2(number):
    """
    Input: list of numbers.

    Output: string with the form of a phone number.
    """
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*number)


if __name__ == '__main__':
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
    print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    print()
    print(create_phone_number_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    print(create_phone_number_2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(create_phone_number_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    print(create_phone_number_2([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
    print(create_phone_number_2([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
