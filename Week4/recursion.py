def factorial(n):
    if n == 0 or n == 1:  # Base Case
        return 1
    else:  # Recursive Case
        return n * factorial(n - 1)
    
print(factorial(5))  # Output: 120

# 5! = 5x4x3x2x1
