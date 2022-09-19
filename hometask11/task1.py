b1 = int(input("Enter b1: "))
q = int(input("Enter q: "))
n = int(input("Enter n: "))


def generator(x):
    yield q**x


for i in range(n):
    n_i = next(generator(i))
    b = b1 * n_i
    print(b)
