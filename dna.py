"""
Complementary DNA.

Deoxyribonucleic acid is a chemical found in the nucleus of cells and carries
the "instructions" for the development and functioning of living organisms.

In DNA strings, "A" and "T" are complements of each other, as "C" and "G".
Your function receives one side of the DNA (string, except for Haskell);
you need to return the other complementary side.
DNA strand is never empty or there is no DNA at all (except for Haskell).

Example: (input --> output)
"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
https://www.codewars.com/kata/554e4a2f232cdd87d9000038
"""


# long version
def dna_strand(dna):
    """
    Input: one side of the DNA (string).

    Output: complementary side of the DNA (string).
    """
    dna_list = ''
    for let in dna:
        if let == 'A':
            dna_list += 'T'
        elif let == 'T':
            dna_list += 'A'
        elif let == 'C':
            dna_list += 'G'
        elif let == 'G':
            dna_list += 'C'

    return dna_list


# short version
def dna_strand2(dna):
    """
    Input: one side of the DNA (string).

    Output: complementary side of the DNA (string).
    """
    return dna.translate(dna.maketrans("ATCG", "TAGC"))


if __name__ == '__main__':
    print(dna_strand('AAAA'))
    print(dna_strand('ATTGC'))
    print(dna_strand('GTAT'))
    print()
    print(dna_strand2('AAAA'))
    print(dna_strand2('ATTGC'))
    print(dna_strand2('GTAT'))
