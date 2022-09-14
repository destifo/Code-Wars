'''
https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
'''


def increment_string(strng):
    digits = []
    pas_zero = False
    
    for ch in strng:
        if ch.isdigit():
            if ch == '0' and not pas_zero:  continue
            if ch != '0':
                pas_zero = True
            digits.append(ch)
        else:
            pas_zero = False
            digits = []
    
    if not digits:
        if strng and strng[-1] == '0':
            strng = strng[:-1]
        strng +='1'
        return strng
    
    n = len(digits)
    m = len(strng)
    num = int(''.join(digits))
    inc_num = num + 1
    
    if strng[m-n-1] == '0' and len(str(num)) != len(str(inc_num)):
        strng = strng[:m-n-1]
        strng += str(inc_num)
        return strng
    
    new_strng = strng[:m-n] + str(inc_num)
    return new_strng