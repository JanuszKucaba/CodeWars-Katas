"""
Unique In Order.

Implement the function unique_in_order which takes as argument a sequence and
returns a list of items without any elements with the same value next to each
other and preserving the original order of elements.

For example:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
"""


# long version
def unique_in_order(iterable):
    """
    Input: sequence with repeating items.

    Output: list of single items
    """
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)

    return res


# short version
def unique_in_order_2(iterable):
    """
    Input: sequence with repeating items.

    Output: list of single items
    """
    return [item for idx, item in enumerate(iterable) if not idx or iterable[idx-1] != item]


if __name__ == '__main__':
    print(unique_in_order('AAAABBBCCDAABBB'))
    print()
    print(unique_in_order_2('AAAABBBCCDAABBB'))
