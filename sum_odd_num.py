'''
Given the triangle of consecutive odd numbers:
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle
(starting at index 1) e.g.: (Input --> Output)
1 -->  1
2 --> 3 + 5 = 8
https://www.codewars.com/kata/55fd2d567d94ac3bc9000064
'''

# 1 solution
def row_sum_odd_numbers(num_triangle):
    '''Takes the triangle of consecutive odd numbers
    and returns the sum of the numbers in the nth row of this triangle'''
    return sum([num for num in range(num_triangle*(num_triangle-1),
                num_triangle*(num_triangle+1)) if num % 2 == 1])

# 2 solution
def row_sum_odd_numbers2(num_triangle):
    '''Takes the triangle of consecutive odd numbers
    and returns the sum of the numbers in the nth row of this triangle'''
    return num_triangle ** 3


if __name__ == '__main__':
    print(row_sum_odd_numbers(5))
    print(row_sum_odd_numbers(10))
    print('-' * 30)
    print(row_sum_odd_numbers(5))
    print(row_sum_odd_numbers(10))
