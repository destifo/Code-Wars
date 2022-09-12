'''
https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python
'''


def maskify(cc):
    n = len(cc)
    if n < 5:   return cc

    non_masked = 4
    masked_str = '#' * (n-non_masked)
    masked_str += cc[n-non_masked:]
    
    return masked_str