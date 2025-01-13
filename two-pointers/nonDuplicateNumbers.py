# given an array of sorted numbers (ascending)
# move in-place all numbers so that only one instance of each is in the array.
# return how many unique numbers are in the array

def moveElements(nums):
    
    # two pointer approach
    # track where the next non-duplicate element should be placed.
    
    next_unique = 1
    
    for i in range(1, len(nums)):
        
        if nums[i] != nums[next_unique - 1]:
            # unique
            nums[next_unique] = nums[i]
            next_unique += 1
            
    return next_unique

numbers = [2, 3, 3, 3, 6, 7, 7, 8, 9 ,9, 9, 9, 9, 10] # ans = [2, 3, 6, 9]
print(moveElements(numbers))
