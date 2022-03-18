sheeps = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

# 1 solution
def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i is True:
            count += 1
    return count

# 2 solution
def count_sheeps2(sheep):
    return sum([i for i in sheep if i is True])

# 3 solution
def count_sheeps3(sheep):
    return sheep.count(True)


if __name__ == '__main__':

    print(count_sheeps(sheeps))
    print(count_sheeps2(sheeps))
    print(count_sheeps3(sheeps))
