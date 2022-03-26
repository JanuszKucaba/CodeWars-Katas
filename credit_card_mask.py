'''
Write a function maskify, which changes all but the last four characters into '#'.
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""
https://www.codewars.com/kata/5412509bd436bd33920011bc
'''

# 1 solution
def maskify(credit_card):
    '''Takes a credit card number and returns it
    in encoded form except the last 4 characters'''
    for number in credit_card[:-4]:
        credit_card = credit_card.replace(number, '#', 1)
    return credit_card

# 2 solution
def maskify2(credit_card):
    '''Takes a credit card number and returns it
    in encoded form except the last 4 characters'''
    num_length = len(credit_card)
    if num_length <= 4:
        return credit_card
    return (num_length - 4) * '#' + credit_card[-4:]


if __name__ == '__main__':
    print(maskify("4556364607935616"))
    print(maskify(     "64607935616"))
    print(maskify(               "1"))
    print(maskify(                ""))
    print('-' * 30)
    print(maskify2("4556364607935616"))
    print(maskify2(     "64607935616"))
    print(maskify2(               "1"))
    print(maskify2(                ""))
