"""
The examples below show you how to write function accum.

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
"""


# long version
def accum(str_):
    """
    Input: string.

    Output: string with each letter duplicated idx times
    and uppercase first letter.
    """
    res = []
    for idx, let in enumerate(str_):
        res.append((let * (idx+1)).title())

    return '-'.join(res)


# short version
def accum2(str_):
    """
    Input: string.

    Output: string with each letter duplicated idx times
    and uppercase first letter.
    """
    return '-'.join((let * (idx + 1)).title() for idx, let in enumerate(str_))


if __name__ == '__main__':
    print(accum("ZpglnRxqenU"))
    print(accum("NyffsGeyylB"))
    print(accum("MjtkuBovqrU"))
    print(accum("EvidjUnokmM"))
    print(accum("HbideVbxncC"))
    print()
    print(accum2("ZpglnRxqenU"))
    print(accum2("NyffsGeyylB"))
    print(accum2("MjtkuBovqrU"))
    print(accum2("EvidjUnokmM"))
    print(accum2("HbideVbxncC"))
