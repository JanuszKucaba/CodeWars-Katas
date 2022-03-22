'''
You need to write regex that will validate a password to make sure it meets the following criteria:
- at least six characters long
- contains a lowercase letter
- contains an uppercase letter
- contains a number
Valid passwords will only be alphanumeric characters.
https://www.codewars.com/kata/52e1476c8147a7547a000811
'''

regex = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[a-zA-Z0-9]{6,}$'

# Description of the solution:
# ^                     - starting character of the string
# (?=.*[A-Z])           - upper case letter that must occur at least once
# (?=.*[a-z])           - lower case letter must occur at least once
# (?=.*[0-9])           - digit must occur at least once
# [a-zA-Z0-9]           - contains only lower- , uppercase and numbers
# {6,}                  - at least 6 characters
# $                     - the end of the string
