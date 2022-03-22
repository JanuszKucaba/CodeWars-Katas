'''
Write a function that takes an array of numbers (integers for the tests) and a target number.
It should find two different items in the array that, when added together, give the target value.
The indices of these items should then be returned in a tuple / list like so: (index1, index2).
twoSum [1, 2, 3] 4 === (0, 2)
https://www.codewars.com/kata/52c31f8e6605bcc646000082
'''

def two_sum(numbers, target):
    '''takes a list and a target
    returns a list with indices'''
    for i in range(len(numbers)):
        for j in range(len(numbers)):   # big-O
            if i != j and numbers[i] + numbers[j] == target:
                return i, j


if __name__ == '__main__':
    print(two_sum([1, 2, 3], 4))
    print(two_sum([5, 6, 7], 12))
