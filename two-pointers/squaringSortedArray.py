def squareArray(numbers):
    
    # 2 pointer approach to sort squares in place.
    
    n = len(numbers)
    squares = [-1 for x in range(n)]
    
    highestSquareIndex = n - 1
    
    left = 0
    right = n - 1
    
    while left <= right:
        
        leftSquare = numbers[left] * numbers[left]
        rightSquare = numbers[right] * numbers[right]
        
        if leftSquare > rightSquare:
            
            squares[highestSquareIndex] = leftSquare
            left += 1
        else:
            squares[highestSquareIndex] = rightSquare
            right -= 1
            
        highestSquareIndex -= 1
 
    return squares

nums = [-2, -1, 0, 2, 3]

squares = squareArray(nums)

print(squares)


            
            
            
    