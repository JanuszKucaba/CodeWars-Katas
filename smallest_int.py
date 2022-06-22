"""
Given an array of integers your solution should find the smallest integer.

You can assume, for the purpose of this kata,
that the supplied array will not be empty.
https://www.codewars.com/kata/55a2d7ebe362935a210000b2
"""


def find_smallest_int(arr):
    """
    input: arr, a list of integers.

    output: smallest integer in arr.
    """
    return min(arr)


def find_smallest_int2(arr):
    """
    input: arr, a list of integers.

    output: smallest integer in arr.
    """
    return sorted(arr)[0]


def find_smallest_int3(arr):
    """
    input: arr, a list of integers.

    output: smallest integer in arr.
    """
    min = arr[0]
    for item in arr:
        if min > item:
            min = item
    return min


if __name__ == '__main__':
    print(find_smallest_int([78, 56, 232, 12, 11, 43]))
    print(find_smallest_int([78, 56, -2, 12, 8, -33]))
    print()
    print(find_smallest_int2([78, 56, 232, 12, 11, 43]))
    print(find_smallest_int2([78, 56, -2, 12, 8, -33]))
    print()
    print(find_smallest_int3([78, 56, 232, 12, 11, 43]))
    print(find_smallest_int3([78, 56, -2, 12, 8, -33]))
