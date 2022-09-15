def high(x):
    words = x.split()
    max_val = max(words, key=lambda y:sum([ord(ch)-96 for ch in y]))
    max_score = sum([ord(ch)-96 for ch in max_val])
    for word in words:
        if sum([ord(ch)-96 for ch in word]) == max_score:
            return word
