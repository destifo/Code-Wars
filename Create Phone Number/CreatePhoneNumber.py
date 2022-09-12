'''
https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
'''


def create_phone_number(n):
    return f'({"".join(list(map(str, n[:3])))}) {"".join(list(map(str, n[3:6])))}-{"".join(list(map(str, n[6:])))}'

def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])