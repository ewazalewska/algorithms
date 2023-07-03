""" 
"FizzBuzz"

For numbers in the range from 1 to n:

Print "Fizz" if the number is divisible by 3.
Print "Buzz" if the number is divisible by 5.
Print "FizzBuzz" if the number is divisible by both 3 and 5.
If none of the above cases apply, simply print the number. 
"""

def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizz_buzz(15)