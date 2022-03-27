'''
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
'''

# 1 solution
def find_short(sentence):
    '''Takes a sentence and returns
    the length of the shortest word(s)'''
    words = sentence.split(" ")
    shortest = len(words[0])
    for word in words:
        if shortest > len(word):
            shortest = len(word)
    return shortest

# 2 solution
def find_short2(sentence):
    '''Takes a sentence and returns
    the length of the shortest word(s)'''
    return min(len(word) for word in sentence.split())


if __name__ == '__main__':
    print(find_short("It turns out you don't need all that stuff you insisted you did."))
    print(find_short('The team members were hard to tell apart since they all wore their hair in a ponytail.'))
    print('-' * 30)
    print(find_short2("It turns out you don't need all that stuff you insisted you did."))
    print(find_short2('The team members were hard to tell apart since they all wore their hair in a ponytail.'))
