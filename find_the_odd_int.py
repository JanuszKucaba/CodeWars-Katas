"""
Find the odd int.

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time.
https://www.codewars.com/kata/54da5a58ea159efa38000836
"""


def find_it(seq):
    """
    Input: list of integers.

    Output: integer that appear an odd numbers of times.
    """
    for num in seq:
        if seq.count(num) % 2 == 1:
            return num


def find_it_2(seq):
    """
    Input: list of integers.

    Output: integer that appear an odd numbers of times.
    """
    return [num for num in seq if seq.count(num) % 2 == 1][0]


if __name__ == '__main__':
    print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
    print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
    print()
    print(find_it_2([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
    print(find_it_2([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
