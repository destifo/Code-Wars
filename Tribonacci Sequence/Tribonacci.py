'''
https://www.codewars.com/kata/556deca17c58da83c00002db/train/python
'''


def tribonacci(signature, n):
    for i in range(3, n):
        signature.append((signature[i-1]+signature[i-2]+signature[i-3]))
        
    return signature[:n]