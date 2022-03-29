'''
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing
second character of the final pair with an underscore ('_').
Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
'''

# 1 solution
def solution(letters):
    '''takes a string and divides it by 2 letters
    returns a list of these strings'''
    res = []
    if len(letters) % 2:
        letters += '_'

    for index, value in enumerate(letters):
        let = ''
        if not index % 2:
            let = value + letters[index+1]
            res.append(let)
        elif index == len(letters)-1:
            break

    return res

# 2 solution
def solution2(letters):
    '''takes a string and divides it by 2 letters
    returns a list of these strings'''
    result = []
    if len(letters) % 2:
        letters += '_'
    for i in range(0, len(letters), 2):
        result.append(letters[i:i+2])
    return result


if __name__ == '__main__':
    print(solution("asdfadsf"))
    print(solution("asdfads"))
    print(solution(""))
    print(solution("x"))
    print('-' * 30)
    print(solution2("asdfadsf"))
    print(solution2("asdfads"))
    print(solution2(""))
    print(solution2("x"))
