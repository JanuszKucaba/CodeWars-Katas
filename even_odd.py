"""
Create a function that takes an integer as an argument and
returns "Even" for even numbers or "Odd" for odd numbers.
https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
"""


def even_or_odd(number):
    """Takes a number and returns
    'Even' or 'Odd' information."""
    return 'Even' if number % 2 else 'Odd'


if __name__ == '__main__':
    print(even_or_odd(2))
    print(even_or_odd(1))
    print(even_or_odd(0))
    print(even_or_odd(1545452))
    print(even_or_odd(7))
    print(even_or_odd(78))
    print(even_or_odd(17))
