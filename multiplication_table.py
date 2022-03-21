'''
Your task, is to create NxN multiplication table, of size provided in parameter.
for example, when given size is 3:
1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08
'''

# 1 solution
def multiplication_table(size):
    '''create multiplication table of given size'''
    size = int(size)
    matrix = []
    for i in range(size):
        num = []
        for j in range(size):               # big-O notation
            num.append((i+1)*(j+1))
        matrix.append(num)
    return matrix

def multiplication_table2(size):
    '''create multiplication table of given size'''
    return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]


if __name__ == '__main__':
    print(multiplication_table(3))
    print(multiplication_table2(3))

    print(multiplication_table(6))
    print(multiplication_table2(6))
