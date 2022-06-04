"""
Your task is to create a function that does four basic mathematical operations.
The function should take three arguments - operation(string/char), 
value1(number), value2(number). The function should return result of numbers
after applying the chosen operation.
https://www.codewars.com/kata/57356c55867b9b7a60000bd7
"""


# 1 solution
def basic_op(operator, value1, value2):
    """Takes operator, number1 and number2
    returns results of operation"""
    if operator == '+':
        res = value1 + value2
    elif operator == '-':
        res = value1 - value2
    elif operator == '*':
        res = value1 * value2
    elif operator == '/':
        res = value1 / value2
    return res


# 2 solution
def basic_op2(operator, value1, value2):
    return eval('{}{}{}'.format(value1, operator, value2))


if __name__ == '__main__':
    print(basic_op('+', 4, 7))
    print(basic_op('-', 15, 18))
    print(basic_op('*', 5, 5))
    print(basic_op('/', 49, 7))
    print()
    print(basic_op2('+', 4, 7))
    print(basic_op2('-', 15, 18))
    print(basic_op2('*', 5, 5))
    print(basic_op2('/', 49, 7))
