''''
https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
'''


def open_or_senior(data):
    ans = []
    
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            ans.append("Senior")
        else:
            ans.append("Open")
            
    return ans

def open_or_senior2(data):
    return ["Senior" if (age >= 55 and handicap > 7) else "Open" for (age, handicap) in data]