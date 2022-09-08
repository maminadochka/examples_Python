#GYGYfunctools import reduce
from datetime import datetime

#filter:
def is_even(value):
    return value % 2 == 0

ln = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Even numbers by my function: {list(filter(is_even, ln))}")
print(f"Even numbers by lambda function: {list(filter(lambda x: x%2 ==0 , ln))}")


#reduce:
n = 10
ln = list(range(1, 11))
#rx - предыдущее, x - текущее
print(f"Factorial 10 is {reduce(lambda rx, x: rx*x, ln)}")


#Decorator:
def stringarator(ugly_function):
    def wrapper(*args): #обертка
        time = datetime.now()
        if args[0] == 10:
            res = 3628800
        else:
            res = str(ugly_function(*args))
        time2 = datetime.now()
        print(time2 - time)
        return res
    return wrapper


@stringarator
def factorial(number):
    fact = 1
    for i in range(2, number+1):
        fact *= i
    return fact


numb = 11
print(type(factorial(numb)))
print(factorial(numb))
#GYGY#GYGY#GYGY#GYGY
#print("hello, world!")
#print("hello, world!")