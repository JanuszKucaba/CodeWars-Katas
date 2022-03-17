'''
There is an array of strings. All strings contains similar letters except one. Try to find it!
Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.
It’s guaranteed that array contains more than 3 strings
https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3
'''


# 1 solution
# def find_uniq(arr):
#     temp = []
#     for i, item in enumerate(arr):
#         temp.append((''.join(sorted(item.lower().strip())), arr[i]))
#     temp.sort()
#     if temp.count(temp[0][0]) == 1:
#         return arr[0][1]
#     else:
#         return temp[-1][1]

# 2 solution
def find_uniq(arr):
    # lista
    temp = []
    for item in arr:
        temp.append((item.lower(), item))
    temp.sort()
    if temp[0][0].count == 1 and temp[0][0] != '':
        return temp[0][1]
    else:
        return temp[-1][1]

# 3 solution
# def find_uniq(arr):
#     arr.sort(key=lambda x: x.lower())
#     arr1 = [set(i.lower()) for i in arr]    
#     return arr[0] if arr1.count(arr1[0]) == 1 and str(arr1[0]) != 'set()' else arr[-1]

# 4 solution
# def find_uniq(arr):
#    if set(arr[0].lower()) == set(arr[1].lower()):
#         majority_set = set(arr[0].lower())
#     elif set(arr[0].lower()) == set(arr[2].lower()):
#         majority_set = set(arr[0].lower())
#     else:
#         majority_set = set(arr[1].lower())
#     for string in arr:
#         if set(string.lower()) != majority_set:
#             return string


if __name__ == '__main__':
    l1 = [ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]    # BbBb
    l2 = [ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]        # foo
    l3 = [ '    ', 'a', '  ' ]                                      # a

    print(find_uniq(l1))
    print(find_uniq(l2))
    print(find_uniq(l3))