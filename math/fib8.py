"""Calculating fibonacci sequence's remainders mod 8, because I don't want to do it manually."""

def fibonacci(n):
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

print([fibonacci(n) % 8 for n in range(100)])
print(5**(187) % 18)