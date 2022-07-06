"""
Array.diff.

Your goal in this kata is to implement a difference function, which subtracts
one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping
their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences
must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""


# long version
def array_diff(a, b):
    """
    Input: list a and list b.

    Output: list a without elements from list b.
    """
    res = []
    for el in a:
        if el not in b:
            res.append(el)

    return res


# short version
def array_diff_2(a, b):
    """
    Input: list a and list b.

    Output: list a without elements from list b.
    """
    return [el for el in a if el not in b]


if __name__ == '__main__':
    print(array_diff([1, 2], [1]))
    print(array_diff([1, 2, 2], [1]))
    print(array_diff([1, 2, 2], [2]))
    print(array_diff([1, 2, 2], []))
    print(array_diff([], [1, 2]))
    print(array_diff([1, 2, 3], [1, 2]))
    print()
    print(array_diff_2([1, 2], [1]))
    print(array_diff_2([1, 2, 2], [1]))
    print(array_diff_2([1, 2, 2], [2]))
    print(array_diff_2([1, 2, 2], []))
    print(array_diff_2([], [1, 2]))
    print(array_diff_2([1, 2, 3], [1, 2]))
