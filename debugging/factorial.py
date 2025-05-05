#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid infinite loop
    return result

if __name__ == "__main__":
    try:
        num = int(sys.argv[1])
        print(factorial(num))
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)