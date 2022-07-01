"""
Given an integral number, determine if it's a square number.

https://www.codewars.com/kata/54c27a33fb7da0db0100040e
"""


def is_square(number: int) -> bool:
    """
    Input: number (int).

    Output: True / False depends if it's a square number
    """
    if number >= 0 and (number ** (1/2)).is_integer():
        return True
    return False


if __name__ == '__main__':
    print(is_square(-1))
    print(is_square(0))
    print(is_square(3))
    print(is_square(4))
    print(is_square(25))
    print(is_square(26))
