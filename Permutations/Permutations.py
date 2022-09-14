'''
https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
'''


from typing import List
from collections import Counter


# O() time,
# O() space,
# Approach: backtracking
def permutations(s):
    permutations = []
    count = Counter(s)

    def findPermute(curr_str: List[str]) -> None:
        if len(curr_str) == len(s):
            permutations.append("".join(curr_str))
            return
        
        used_letters = set()
        
        for ch in s:
            if ch in used_letters or count[ch] < 1:  continue
            count[ch] -=1
            used_letters.add(ch)
            curr_str.append(ch)
            findPermute(curr_str)
            count[ch] +=1
            curr_str.pop()
            
    findPermute([])
    return permutations