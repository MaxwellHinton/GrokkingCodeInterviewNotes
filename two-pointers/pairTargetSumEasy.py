def targetSum(numbers, target):
    
    # returns indices of the pair that equal the target or [-1, -1]
    # 2 pointer approach
    
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        
        if numbers[left] + numbers[right] > target:
            # move right pointer
            right -= 1    
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            return [left, right]
    
    
    
    return [-1, -1]

numbers = [1, 2, 3, 4, 6]
target = 6

print(targetSum(numbers, target))