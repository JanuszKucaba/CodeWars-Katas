"""
Sum of two lowest positive integers.

Create a function that returns the sum of the two lowest positive numbers
given an array of minimum 4 positive integers. No floats or non-positive
integers will be passed.
For example, when an array is passed like [19, 5, 42, 2, 77],
the output should be 7.
[10, 343445353, 3453445, 3453545353453] should return 3453455.
https://www.codewars.com/kata/558fc85d8fd1938afb000014
"""


# first solution
def sum_two_smallest_numbers(numbers):
    """
    Input: list of numbers.

    Output: sum of two lowest numbers
    """
    return sorted(numbers)[0] + sorted(numbers)[1]


# second solution
def sum_two_smallest_numbers_2(numbers):
    """
    Input: list of numbers.

    Output: sum of two lowest numbers
    """
    return sum(sorted(numbers)[:2])


if __name__ == '__main__':
    print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
    print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
    print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))
    print()
    print(sum_two_smallest_numbers_2([5, 8, 12, 18, 22]))
    print(sum_two_smallest_numbers_2([7, 15, 12, 18, 22]))
    print(sum_two_smallest_numbers_2([25, 42, 12, 18, 22]))
