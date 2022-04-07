'''
Capitalise the first letter of the first word.
Add a period (.) to the end of the sentence.
Join the words into a complete string, with spaces.
Do no other manipulation on the words.
https://www.codewars.com/kata/59ad7d2e07157af687000070
'''

# 1 solution
def sentencify(words):
    '''takes words as list and return sentence
    with first capitalize letter and dot at the end'''
    for index in range(len(words)):
        if index == 0:
            words[0] = words[index][0].upper() + words[index][1:]
        if index == len(words) - 1:
            words[index] += '.'

    return ' '.join(words)

# 1 solution
def sentencify2(words):
    '''takes words as list and return sentence
    with first capitalize letter and dot at the end'''
    res = ' '.join(words) + '.'
    return res[0].upper() + res[1:]


if __name__ == '__main__':
    print(sentencify(["i", "am", "an", "AI"]))
    print(sentencify(["yes"]))
    print(sentencify(["FIELDS","of","CORN","are","to","be","sown"]))
    print(sentencify(["i'm","afraid","I","can't","let","you","do","that"]))
    print('-' * 30)
    print(sentencify2(["i", "am", "an", "AI"]))
    print(sentencify2(["yes"]))
    print(sentencify2(["FIELDS","of","CORN","are","to","be","sown"]))
    print(sentencify2(["i'm","afraid","I","can't","let","you","do","that"]))
