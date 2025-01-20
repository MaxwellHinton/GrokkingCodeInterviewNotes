# brute force approach

def ceilingBruteForce(nums, key):
    
    ceiling = float('inf')
    
    for i in range(len(nums)):
        
        if nums[i] >= key:
            ceiling = min(ceiling, nums[i])
    
    return ceiling
    
nums = [4, 6, 10]
key = 1

# print(ceilingBruteForce(nums, key))


# the problem is to use binary-search to turn the time compelxity to O(log N)

def binaryCeiling(nums, key):
    
    n = len(nums)
    
    ceiling = -1
    
    start = 0
    end = n - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if nums[mid] >= key:
            ceiling = nums[mid]
            end = mid - 1
        else:
            start = mid + 1
    
    return ceiling
    
nums2 = [4, 6, 10, 12, 14]
key2 = 15

print(binaryCeiling(nums2, key2))
    

    