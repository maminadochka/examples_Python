def recursive_factorial(n: int):
    if n == 1:
        return n
    elif n == 0:
        return 1
    else:
        return recursive_factorial(n-1)*n


def cycle_factorial(n: int):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


numb = input("Enter a number to calculate factorial: ")
print(f"Recursively calculated factorial of {numb} is {recursive_factorial(int(numb))}")
print(f"Calculated using cycle factorial of {numb} is {cycle_factorial(int(numb))}")
