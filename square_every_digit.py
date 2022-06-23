"""
Square every digit of a number and concatenate them.

Note: The function accepts an integer and returns an integer
https://www.codewars.com/kata/546e2562b03326a88e000020
"""


def square_digits(num):
    """
    input: integer number.

    output: every digit square.
    """
    res = ''
    for dig in str(num):
        res += str(int(dig)**2)
    return int(res)


def square_digits2(num):
    """
    input: integer number.

    output: every digit square.
    """
    return int(''.join(str(int(dig)**2) for dig in str(num)))


if __name__ == '__main__':
    print(square_digits(9119))
    print(square_digits(0))
    print()
    print(square_digits2(9119))
    print(square_digits2(0))
