'''
https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
'''


def sort_array(source_array):
    odd_num_indices = []
    odd_nums = []
    
    for index,num in enumerate(source_array):
        if num % 2 != 0:
            odd_num_indices.append(index)
            odd_nums.append(num)
            
    odd_nums.sort()
    
    for i in range(len(odd_nums)):
        index = odd_num_indices[i]
        source_array[index] = odd_nums[i]
        
    return source_array