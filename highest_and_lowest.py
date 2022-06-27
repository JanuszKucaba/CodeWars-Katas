"""
You are given a string of space separated numbers.

Return the highest and lowest number.
https://www.codewars.com/kata/554b4ac871d6813a03000035
"""


def high_and_low(numbers):
    """
    input: string with numbers.

    output: min and max numbers in string
    """
    str_list = numbers.split(' ')
    num_list = []
    for num in str_list:
        num_list.append(int(num))
    num_min = min(num_list)
    num_max = max(num_list)
    res = str(num_max) + ' ' + str(num_min)
    return res


def high_and_low2(numbers):
    """
    input: string with numbers.

    output: min and max numbers in string
    """
    num_list = [int(let) for let in numbers.split(' ')]
    return f'{max(num_list)} {min(num_list)}'


if __name__ == '__main__':
    print(high_and_low('8 3 -5 42 -1 0 0 -9 4 7 4 -4'))
    print(high_and_low('1 2 3'))
    print()
    print(high_and_low2('8 3 -5 42 -1 0 0 -9 4 7 4 -4'))
    print(high_and_low2('1 2 3'))
