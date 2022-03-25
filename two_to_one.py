'''
Take 2 strings s1 and s2 including only letters from a to z.
Return a new sorted string, the longest possible, containing distinct letters
- each taken only once - coming from s1 or s2.
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"
https://www.codewars.com/kata/5656b6906de340bd1b0000ac
'''

def longest(string1, string2):
    '''takes two strings
    returns sorted list with distinct letters'''
    return ''.join(sorted(set(string1) | set(string2)))

def longest2(string1, string2):
    '''takes two strings
    returns sorted list with distinct letters'''
    return "".join(sorted(set(string1 + string2)))


if __name__ == '__main__':
    letters_1 = "xyaabbbccccdefww"
    letters_2 = "xxxxyyyyabklmopq"

    print(longest(letters_1, letters_2))
    print(longest2(letters_1, letters_2))
