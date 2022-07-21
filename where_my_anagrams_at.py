"""
Where my anagrams at.

What is an anagram? Well, two words are anagrams of each other if they both
contain the same letters. For example:
'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words. You should return
an array of all the anagrams or an empty array if there are none. For example:
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
https://www.codewars.com/kata/523a86aa4230ebb5420001e1
"""


# long version
def anagrams(word, words):
    """
    Input: word to compare with words in list.

    Outut: list with anagrams.
    """
    res = []
    for item in words:
        if sorted(word) == sorted(item):
            res.append(item)
    return res


# short version
def anagrams_2(word, words):
    """
    Input: word to compare with words in list.

    Outut: list with anagrams.
    """
    return [item for item in words if sorted(word) == sorted(item)]


if __name__ == '__main__':
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
    print()
    print(anagrams_2('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
    print(anagrams_2('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
