#!/usr/bin/env python

# Classic Fibonacci function

def fibonacci(num):
    print(0)
    print(1)
    fib = [0,1]
    for i in range(num - 1):
        sum = fib[len(fib) - 1] + fib[len(fib) - 2]
        fib.append(sum)
        print(fib[len(fib) - 1])

fibonacci(10)