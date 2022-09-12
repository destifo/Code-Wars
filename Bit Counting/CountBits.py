'''
https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
'''


def count_bits(n):
    return bin(n).count(1)

def count_bits2(n):
    ones = 0

    while n > 0:
        if n % 2 == 1:
            ones +=1
        n //=2
    
    return ones