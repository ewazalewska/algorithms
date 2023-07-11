'''
Implementation of Fibonacci sequence
(a sequence in which each number is the sum of the two preceding ones)
using range() function

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
'''

def fibonacci(n):
    # f - first; s - second
    f, s = 0, 1
    for _ in range(n):
        f, s = s, f + s
    return f
    
print(fibonacci(0))     # Output: 0
print(fibonacci(3))     # Output: 2
print(fibonacci(10))    # Output: 55