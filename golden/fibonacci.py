import math


def loop_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b 
        # f(x) = a + b ---> f(x+1) = b + f(x)
        # a and b are always de last 2 numbers in de sequence. S = [..., a, b, f(x)]
        # a = f(n) and b = f(n+1)
    return a

def recursive_fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return recursive_fib(n-1) + recursive_fib(n-2 )

def main():
    n = int(input("n: "))
    result = (recursive_fib(n))
    print(result)


if __name__ == "__main__":
    main()
