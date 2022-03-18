'''
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
https://www.codewars.com/kata/52597aa56021e91c93000cb0/
'''

# 1 solution
def move_zeros(array):
    '''moving zeros to the end'''
    new_array = []
    zero_array = []
    for i in array:
        if i == 0:
            zero_array.append(i)
        else:
            new_array.append(i)

    array = new_array + zero_array

    return array

# solution
def move_zeros2(array):
    '''moving zeros to the end'''
    return sorted(array, key=lambda x: x==0 and not isinstance(x, bool))


if __name__ == '__main__':

    print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
    print(move_zeros2([1, 0, 1, 2, 0, 1, 3]))

    print(move_zeros([0, 5, 0, 3, 2, 0, 3]))
    print(move_zeros2([0, 5, 0, 3, 2, 0, 3]))
