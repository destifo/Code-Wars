'''
https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
'''


import heapq


def queue_time(customers, n):
    m = len(customers)
    if n == 1:
        return sum(customers)
    
    if n >= m:
        return max(customers)
    
    min_heap = []
    for i in range(n):
        heapq.heappush(min_heap, customers[i])

    i +=1 
    while i < m:
        till = heapq.heappop(min_heap)
        
        till += customers[i]
        i+=1
        
        heapq.heappush(min_heap, till)
        
    while len(min_heap) > 1:
        heapq.heappop(min_heap)
        
    return heapq.heappop(min_heap)
        

print(queue_time([2,2,3,3,4,4], 2))