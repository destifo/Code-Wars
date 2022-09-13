'''
https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
'''


def pig_it(text):
    return " ".join([ (word[1:] + word[0] + 'ay') if word.isalpha() else word for word in text.split() ])

print(pig_it('Hello world !'))