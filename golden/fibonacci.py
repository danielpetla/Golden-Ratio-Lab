import math


def loop_fib(n): # Using a standard loop for the fibonacci sequence
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b 
        # f(x) = a + b ---> f(x+1) = b + f(x)
        # a and b are always de last 2 numbers in de sequence. S = [..., a, b, f(x)]
        # a = f(n) and b = f(n+1)
    return a

def recursive_fib(n): # Using a recursive function fot the fibonacci sequence
    if n == 0: return 0
    if n == 1: return 1
    return recursive_fib(n-1) + recursive_fib(n-2 )

def binet_fib(n): # Binet's formula for the fibonacci sequence
    a = (1 + math.sqrt(5)) / 2
    b = (1 - math.sqrt(5)) / 2
    return round(((a**n) - (b**n)) // math.sqrt(5))

def main():
    n = int(input("n: "))
    print (f'r {recursive_fib(n)}')
    print (f'l {loop_fib(n)}')
    print (f'b {binet_fib(n)}')


if __name__ == "__main__":
    main()
