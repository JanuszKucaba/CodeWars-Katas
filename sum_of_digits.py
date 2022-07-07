"""
Sum of Digits / Digital Root.

Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than one
digit, continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

https://www.codewars.com/kata/541c8630095125aba6000c00
"""


# long version
def digital_root(n):
    """
    Input: number (integer).

    Output: sum of the digits(integer).
    """
    res = sum([int(el) for el in str(n)])
    if res < 10:
        return res
    return digital_root(res)


# short version
def digital_root_2(n):
    """
    Input: number (integer).

    Output: sum of the digits(integer).
    """
    return n if n < 10 else digital_root_2(sum([int(el) for el in str(n)]))


if __name__ == '__main__':
    print(digital_root(16))
    print(digital_root(942))
    print(digital_root(132189))
    print(digital_root(493193))
    print()
    print(digital_root_2(16))
    print(digital_root_2(942))
    print(digital_root_2(132189))
    print(digital_root_2(493193))
