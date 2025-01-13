# Given an array of numbers find the triplet where the sum is as close as possible to the given target.
# if there are multiple, return the sum of the smaller triplets sum.

# [0 0 1 1 2 6] target = 5
# output = 3

def closeToTarget(nums, target):
    
    triplets = []
    
    left = 0
    right = len(nums) - 1
    
    for i in range(len(nums)): # fix X
        
        while left < right:
            
            