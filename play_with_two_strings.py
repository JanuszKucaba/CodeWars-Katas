'''
Your task is to Combine two Strings
Input Strings a and b: For every character in string a swap the casing of every occurrence
of the same character in string b. Then do the same casing swap with the inputs reversed.
Return a single string consisting of the changed version of a followed by the changed version of b.
A char of a is in b regardless if it's in upper or lower case - see the testcases too.
https://www.codewars.com/kata/56c30ad8585d9ab99b000c54/train/python
'''
# 1 solution
def work_on_strings(string_1, string_2):
    '''Takes two strings and change every occurance of the same character
    Returns single string'''
    res = []
    for let_1 in string_1:
        if let_1.islower() and string_2.lower().count(let_1) % 2:
            res.append(let_1.upper())
        elif let_1.isupper() and string_2.upper().count(let_1) % 2:
            res.append(let_1.lower())
        else:
            res.append(let_1)
    for let_2 in string_2:
        if let_2.islower() and string_1.lower().count(let_2) % 2:
            res.append(let_2.upper())
        elif let_2.isupper() and string_1.upper().count(let_2) % 2:
            res.append(let_2.lower())
        else:
            res.append(let_2)

    return ''.join(res)

# 2 solution
def work_on_strings2(string_1, string_2):
    '''Takes two strings and change every occurance of the same character
    Returns single string'''
    new_s1 = [letter if string_2.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in string_1]
    new_s2 = [letter if string_1.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in string_2]
    return ''.join(new_s1) + ''.join(new_s2)


if __name__ == '__main__':
    print(work_on_strings("abc","cde"))
    print(work_on_strings("abcdeFgtrzw", "defgGgfhjkwqe"))
    print(work_on_strings("abcdeFg", "defgG"))
    print(work_on_strings("abab", "bababa"))
    print('-' * 30)
    print(work_on_strings2("abc","cde"))
    print(work_on_strings2("abcdeFgtrzw", "defgGgfhjkwqe"))
    print(work_on_strings2("abcdeFg", "defgG"))
    print(work_on_strings2("abab", "bababa"))
