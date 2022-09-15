
# O(rows*cols) time,
# O(1) space,
# Approach: dp, tabulation
def longest_slide_down(pyramid):
    rows = len(pyramid)
    cols = len(pyramid[-1])
    
#     dp = [[0 for col in range(row+1)] for row in range(rows)]
    
#     for col in range(cols):
#         dp[rows-1][col] = pyramid[rows-1][col]
        
    for row in range(rows-2, -1, -1):
        cols = len(pyramid[row])
        for col in range(cols):
            pyramid[row][col] = pyramid[row][col] + max(pyramid[row+1][col], pyramid[row+1][col+1])
    
    return pyramid[0][0]