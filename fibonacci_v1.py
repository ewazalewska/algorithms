'''
Implementation of Fibonacci sequence
(a sequence in which each number is the sum of the two preceding ones)

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(0))     # Output: 0
print(fibonacci(3))     # Output: 2
print(fibonacci(10))    # Output: 55