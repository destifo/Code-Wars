'''
https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
'''


def dig_pow(n, p):
    return sum(int(str(n)[i])**(p+i) for i in range(len(str(n)))) // n if sum(int(str(n)[i])**(p+i) for i in range(len(str(n)))) % n == 0 else -1