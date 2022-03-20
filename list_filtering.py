'''
In this kata you will create a function that takes a list of non-negative integers
and strings and returns a new list with the strings filtered out.
https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
'''

# 1 solution
def filter_list(list_in):
    '''Function take a list with ints and strings
    returns new list without strings'''
    new_list = []
    for item in range(len(list_in)):
        if type(list_in[item]) == int:
            new_list.append(list_in[item])
    return new_list

# 2 solution
def filter_list2(list_in):
    '''Function take a list with ints and strings
    returns new list without strings'''
    new_list = []
    for i, item in enumerate(list_in):
        if isinstance(item, int):
            new_list.append(list_in[i])
    return new_list

# 3 solution
def filter_list3(list_in):
    '''Function take a list with ints and strings
    returns new list without strings'''
    return [item for item in list_in if not isinstance(item, str)]


if __name__ == '__main__':
    t1 = [1, 2, 'a', 'b']
    t2 = [1, 'a', 'b', 0, 15]
    t3 = [1, 2, 'aasf', '1', '123', 123]

    print(filter_list(t1))
    print(filter_list(t2))
    print(filter_list(t3))

    print(filter_list2(t1))
    print(filter_list2(t2))
    print(filter_list2(t3))

    print(filter_list3(t1))
    print(filter_list3(t2))
    print(filter_list3(t3))
