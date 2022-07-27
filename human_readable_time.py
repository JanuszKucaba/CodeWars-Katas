"""
Human Readable Time.

Write a function, which takes a non-negative integer (seconds) as input
and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
https://www.codewars.com/kata/52685f7382004e774f0001f7
"""


def make_readable(seconds):
    """
    Input: seconds (integer).

    Output: time in format (HH:MM:SS)
    """
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    secs = seconds - (hours * 3600) - (minutes * 60)
    return f'{hours:0>2d}:{minutes:0>2d}:{secs:0>2d}'


if __name__ == '__main__':
    print(make_readable(0))
    print(make_readable(5))
    print(make_readable(60))
    print(make_readable(86399))
    print(make_readable(359999))
