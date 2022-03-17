"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""

# 1 solution
# def find_uniq(arr):
#     arr.sort()
#     print(arr)
#     if arr[0] != arr[1]:
#         return arr[0]
#     else:
#         return arr[-1]

# 2 solution
# def find_uniq(arr):
#     arr.sort()
#     return arr[0] if arr[0] != arr[1] else arr[-1]

# 3 solution
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


if __name__ == '__main__':
    l1 = [1, 1, 1, 2, 1, 1]     # 2
    l2 = [ 0, 0, 0.55, 0, 0 ]   # 0,55
    l3 = [ 3, 10, 3, 3, 3 ]     # 10

    print(find_uniq(l1))
    print(find_uniq(l2))
    print(find_uniq(l3))