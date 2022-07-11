"""
Multiples of 3 or 5.

If we list all the natural numbers below 10 that are multiples of 3 or 5
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5
below the number passed in. Additionally, if the number is negative, return 0
(for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.
https://www.codewars.com/kata/514b92a657cdc65150000006
"""


# long solution
def solution(number):
    """
    Input: number (integer).

    Output: the sum of the multiples of 3 or 5 (integer).
    If number is less than  or equal 0 returns 0.
    """
    res = []
    if number < 0:
        return 0

    for num in range(number):
        if num % 5 == 0:
            res.append(num)
        elif num % 3 == 0:
            res.append(num)

    return sum(res)


# short solution
def solution_2(number):
    """
    Input: number (integer).

    Output: the sum of the multiples of 3 or 5 (integer).
    If number is less than  or equal 0 returns 0.
    """
    if number < 0:
        return 0
    return sum([num for num in range(number) if num % 5 == 0 or num % 3 == 0])


if __name__ == '__main__':
    print(solution(4))      # 3
    print(solution(6))      # 8
    print(solution(16))     # 60
    print(solution(3))      # 0
    print(solution(5))      # 3
    print(solution(15))     # 45
    print(solution(0))      # 0
    print(solution(-1))     # 0
    print(solution(10))     # 23
    print(solution(20))     # 78
    print(solution(200))    # 9168
    print()
    print(solution_2(4))      # 3
    print(solution_2(6))      # 8
    print(solution_2(16))     # 60
    print(solution_2(3))      # 0
    print(solution_2(5))      # 3
    print(solution_2(15))     # 45
    print(solution_2(0))      # 0
    print(solution_2(-1))     # 0
    print(solution_2(10))     # 23
    print(solution_2(20))     # 78
    print(solution_2(200))    # 9168
