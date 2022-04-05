'''
Find Multiple of a Number
Build a program that takes a value, integer , and returns a list of its multiples up to
another value, limit. If limit is a multiple of integer, it should be included as well.
There will only ever be positive integers passed into the function, not consisting of 0.
The limit will always be higher than the base.
https://www.codewars.com/kata/58ca658cc0d6401f2700045f
'''

# 1 solution
def find_multiples(integer, limit):
    '''takes integer and its limit,
    returns list with integer mutiples up to limit'''
    result_list = []
    for i in range(1, (int(limit/integer)+1)):
        result_list.append(integer * i)
    return result_list

# 2 solution
def find_multiples2(integer, limit):
    '''takes integer and its limit,
    returns list with integer mutiples up to limit'''
    return [integer * i for i in range(1, int(limit/integer) + 1)]

if __name__ == '__main__':
    print(find_multiples(5, 25))
    print(find_multiples(1, 2))

    print(find_multiples2(5, 25))
    print(find_multiples2(1, 2))
