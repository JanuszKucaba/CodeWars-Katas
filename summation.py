"""
Program that finds the summation of every number from 1 to num.
The number will always be a positive integer greater than 0
"""

def summation(num):
    res = 0
    for i in range(num+1):
        res += i
    return res

def summation2(num):
    res = 0
    while num:
        res += num
        num -= 1
    return res



# better solution
def summation3(num):
    return sum(range(num + 1))


print(summation(1))     # 1
print(summation(8))     # 36
print(summation(22))    # 253
print(summation(100))   # 5050
print(summation(213))   # 22791

print(summation2(1))     # 1
print(summation2(8))     # 36
print(summation2(22))    # 253
print(summation2(100))   # 5050
print(summation2(213))   # 22791


print(summation3(1))     # 1
print(summation3(8))     # 36
print(summation3(22))    # 253
print(summation3(100))   # 5050
print(summation3(213))   # 22791