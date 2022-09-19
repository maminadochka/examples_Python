b1 = int(input("Enter b1: "))
q = int(input("Enter q: "))
n = int(input("Enter n: "))


def generator(x):
    for y in range(x):
        yield b1*q**y


res_gen = generator(n)
for i in res_gen:
    print(i)
