'''
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).
https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/
'''

# 1 solution
def solution(string, ending):
    '''takes 2 strings and check that
    second sting is or not in first string '''
    if string.endswith(ending):
        return True
    return False

# 2 solution
def solution2(string, ending):
    '''takes 2 strings and check that
    second sting is or not in first string '''
    return True if string.endswith(ending) else False

if __name__ == '__main__':
    print(solution('abcde', 'cde'))
    print(solution('abcde', 'abc'))
    print(solution('abcde', ''))
    print('-' * 30)
    print(solution2('abcde', 'cde'))
    print(solution2('abcde', 'abc'))
    print(solution2('abcde', ''))
