'''
https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
'''


def order(sentence):
    ans = ['' for i in range(len(sentence.split()))]
    
    for word in sentence.split():
        for ch in word:
            if ch.isdigit():
                ans[int(ch)-1] = word
                break
    
    return ' '.join(ans)