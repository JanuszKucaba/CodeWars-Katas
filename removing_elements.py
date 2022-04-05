'''
Take an array and remove every second element from the array.
Always keep the first element and start removing with the next element.
https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python
'''

# 1 solution
def remove_every_other(my_list):
    '''takes list and
    returns items with even index'''
    new_list = []
    for index, element in enumerate(my_list):
        if index % 2 == 0:
            new_list.append(element)

    return new_list

# 2 solution
def remove_every_other2(my_list):
    '''takes list and
    returns items with even index'''
    return [element for index, element in enumerate(my_list) if index % 2 == 0]


if __name__ == '__main__':
    print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
    print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(remove_every_other([[1, 2]]))
    print(remove_every_other([['Goodbye'], {'Great': 'Job'}]))
    print('-' * 30)
    print(remove_every_other2(['Hello', 'Goodbye', 'Hello Again']))
    print(remove_every_other2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(remove_every_other2([[1, 2]]))
    print(remove_every_other2([['Goodbye'], {'Great': 'Job'}]))
