"""
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b))
that checks whether the two arrays have the "same" elements,
with the same multiplicities (the multiplicity of a member is the number of times it appears).
"Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
https://www.codewars.com/kata/550498447451fbbd7600041c
"""

def comp(array1, array2):
    """Takes two arrays and compare them,
    returns True if array1 to square is equal array 2,
    if not returns False"""
    if array1 is None and array2 is None:
        return False
    elif array1 == [] or array2 == []:
        return True
    elif len(array1) == len(array2):
        return True if sorted([a * a for a in array1]) == sorted(array2) else False
    else:
        return False


if __name__ == '__main__':
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    print(comp(a1, a2))

    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    print(comp(a1, a2))

    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    print(comp(a1, a2))

    a1 = []
    a2 = []
    print(comp(a1, a2))

    a1 = None
    a2 = None
    print(comp(a1, a2))
