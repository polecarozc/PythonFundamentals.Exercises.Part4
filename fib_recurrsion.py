def Fibonacci(n):

    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def fibonacci_no_recurrsion(n):
    a = 0
    b = 1
    for i in range(1, n):
        c = a + b
        a = b
        b = c

    return c

print(fibonacci_no_recurrsion(5))

