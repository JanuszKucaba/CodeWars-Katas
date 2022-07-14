"""
Playing with digits.

Given a positive integer n written as abcd... (a, b, c, d... being digits) and
a positive integer p we want to find a positive integer k, if it exists, such
that the sum of the digits of n taken to the successive powers of p is equal
to k * n.
In other words is there an integer k such as:
(a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
If it is the case we will return k, if not return -1.
Note: n and p will always be given as strictly positive integers.

https://www.codewars.com/kata/5552101f47fc5178b1000050
"""


# long version
def dig_pow(n, p):
    """
    Input: positive integers n and p.

    (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
    Output: if exist return integer k, if not return -1.
    """
    num = str(n)
    res = []
    for idx, item in enumerate(num):
        res.append((int(item) ** (p + idx)))

    res = sum(res)
    return int(res / n) if res % n == 0 else -1


# short version
def dig_pow_2(n, p):
    """
    Input: positive integers n and p.

    (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
    Output: if exist return integer k, if not return -1.
    """
    num = str(n)
    res = sum([int(item) ** (p + idx) for idx, item in enumerate(num)])
    return int(res / n) if res % n == 0 else -1


if __name__ == '__main__':
    print(dig_pow(89, 1))
    print(dig_pow(92, 1))
    print(dig_pow(46288, 3))
    print()
    print(dig_pow_2(89, 1))
    print(dig_pow_2(92, 1))
    print(dig_pow_2(46288, 3))
