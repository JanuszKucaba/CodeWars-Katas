'''
Complete the solution so that it reverses the string passed into it.
'world'  =>  'dlrow'
'word'   =>  'drow'
https://www.codewars.com/kata/5168bb5dfe9a00b126000018
'''

def reverse_strings(string):
    '''reverse the string'''
    return string[::-1]


if __name__ == '__main__':
    print(reverse_strings('world'))
    print(reverse_strings('word'))
