"""
Decode the Morse code.

In this kata you have to write a simple Morse code decoder. While the Morse
code is now mostly superseded by voice and digital data communication
channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes".
For example, the letter A is coded as ·−, letter Q is coded as −−·−,
and digit 1 is coded as ·−−−−. The Morse code is case-insensitive,
traditionally capital letters are used. When the message is written in Morse
code, a single space is used to separate the character codes and 3 spaces are
used to separate words. For example, the message HEY JUDE in Morse code is
···· · −·−−   ·−−− ··− −·· ·.

Your task is to implement a function that would take the morse code as input
and return a decoded human-readable string.

For example:

decode_morse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"
NOTE: For coding purposes you have to use ASCII characters . and -, not
Unicode characters.

https://www.codewars.com/kata/54b724efac3d5402db00065e
"""

MORSE_CODE = {
                    '.-': 'A',
                    '-...': 'B',
                    '-.-.': 'C',
                    '-..': 'D',
                    '.': 'E',
                    '..-.': 'F',
                    '--.': 'G',
                    '....': 'H',
                    '..': 'I',
                    '.---': 'J',
                    '-.-': 'K',
                    '.-..': 'L',
                    '--': 'M',
                    '-.': 'N',
                    '---': 'O',
                    '.--.': 'P',
                    '--.-': 'Q',
                    '.-.': 'R',
                    '...': 'S',
                    '-': 'T',
                    '..-': 'U',
                    '...-': 'V',
                    '.--': 'W',
                    '-..-': 'X',
                    '-.--': 'Y',
                    '--..': 'Z',
                    '-----': 0,
                    '.----': 1,
                    '..---': 2,
                    '...--': 3,
                    '....-': 4,
                    '.....': 5,
                    '-....': 6,
                    '--...': 7,
                    '---..': 8,
                    '----.': 9,
                    '.-.-.-': '.',
                    '--..--': ',',
                    '..--..': '?',
                    '.----.': '`',
                    '-.-.--': '!',
                    '-..-.': '/',
                    '-.--.': '(',
                    '-.--.-': ')',
                    '.-...': '&',
                    '---...': ':',
                    '-.-.-.': ';',
                    '-...-': '=',
                    '.-.-.': '+',
                    '-....-': '-',
                    '..--.-': '_',
                    '.-..-.': '"',
                    '...-..-': '$',
                    '.--.-.': '@',
                    '...-.-': 'End of work',
                    '........': 'Error',
                    '-.-.-': 'Starting Signal',
                    '...-.': 'Understood',
                    '...---...': 'SOS',
                    '': ' ',
                }


# long version
def decode_morse(morse_code):
    """
    Input: code morse message.

    Output: decode morse message.
    """
    morse_decode_list = []
    for item in morse_code.split(' '):
        if item in MORSE_CODE:
            morse_decode_list.append(MORSE_CODE[item])
        else:
            morse_decode_list.append(' ')
    morse_decode = ''.join(morse_decode_list)
    return morse_decode.replace('  ', ' ').strip()


# short version:
def decode_morse_2(morse_code):
    """
    Input: code morse message.

    Output: decode morse message.
    """
    morse_decode = ''.join([MORSE_CODE[item] if item in MORSE_CODE else ' ' for item in morse_code.split(' ')])
    return morse_decode.replace('  ', ' ').strip()


if __name__ == '__main__':
    print(decode_morse('.... . -.--  .--- ..- -.. .'))
    print(decode_morse('... --- ...'))
    print()
    print(decode_morse_2('.... . -.--  .--- ..- -.. .'))
    print(decode_morse_2('... --- ...'))
