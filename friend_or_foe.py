'''
Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
https://www.codewars.com/kata/55b42574ff091733d900002f
'''

# 1 solution
def friend(list_of_friends):
    '''Filter list of strings
    return name with 4 letters'''
    return [name for name in list_of_friends if len(name) == 4]

# 2 solution
def friend2(list_of_friends):
    '''Filter list of strings
    return name with 4 letters'''
    names = []
    for name in list_of_friends:
        if len(name) == 4:
            names.append(name)
    return names


if __name__ == '__main__':
    print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
    print(friend(["Ryan", "Kieran", "Mark"]))
    print(friend2(["Ryan", "Kieran", "Jason", "Yous"]))
    print(friend2(["Ryan", "Kieran", "Mark"]))
