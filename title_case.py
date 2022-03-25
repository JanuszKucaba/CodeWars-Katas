'''
Write a function that will convert a string into title case,
given an optional list of exceptions (minor words).
The list of minor words will be given as a string with each word separated by a space.
Your function should ignore the case of the minor words string
-- it should behave in the same way even if the case of the minor word string is changed.
title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
https://www.codewars.com/kata/5202ef17a402dd033c000009
'''

# 1 solution
def title_case(title, minor_words=''):
    '''Convert a string into title case,
    and could takes list of excpetions'''
    title_list = title.lower().split(' ')
    minor_list = minor_words.lower().split(' ')

    for i, words in enumerate(title_list):
        if len(minor_words) == 0:
            title_list[i] = title_list[i].capitalize()
        elif title_list[i] not in minor_list:
            title_list[i] = title_list[i].capitalize()
        elif i == 0:
            title_list[0] = title_list[0].capitalize()

    return ' '.join(title_list)

# 2 solution
def title_case2(title, minor_words=''):
    '''Convert a string into title case,
    and could takes list of excpetions'''
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])


if __name__ == '__main__':
    print(title_case('a clash of KINGS', 'a an the of'))
    print(title_case('THE WIND IN THE WILLOWS', 'The In'))
    print(title_case('the quick brown fox'))

    print(title_case2('a clash of KINGS', 'a an the of'))
    print(title_case2('THE WIND IN THE WILLOWS', 'The In'))
    print(title_case2('the quick brown fox'))
