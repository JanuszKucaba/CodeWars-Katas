'''
Write a program that finds the summation of every number from 1 to num.
The number will always be a positive integer greater than 0.
summation(2) -> 3 <- 1 + 2
summation(8) -> 36 <- 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
https://www.codewars.com/kata/55d24f55d7dd296eb9000030
'''

# 1 solution
def summation(num):
    '''finds the summation of every number from 1 to num'''
    res = 0
    while num:
        res += num
        num -= 1
    return res

# solution
def summation2(num):
    '''finds the summation of every number from 1 to num'''
    return sum(range(num + 1))


if __name__ == '__main__':
    print(summation(2))
    print(summation2(2))

    print(summation(8))
    print(summation2(8))
