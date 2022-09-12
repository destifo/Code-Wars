'''
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python
'''


def solution(s):
    ans = [ s[i:i+2] for i in range(0, len(s), 2) ]
    if len(s) % 2 == 1:
        ans[-1] = ans[-1] + '_'
    
    return ans