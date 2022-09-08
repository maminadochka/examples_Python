import time


def my_decorator(strange_function):
    def nice_wrapper(*args):
        time1 = time.perf_counter_ns()
        strange_function(*args)
        print('Execution time =', time.perf_counter_ns() - time1, 'ns')
    return nice_wrapper


@my_decorator
def my_cool_function(members_list):
    print("This is my first cool function!")
    for i in members_list:
        print(f"Hello, {i}")
    pass


@my_decorator
def my_second_cool_function(numbs):
    print("\n\nThis is my second cool function!")
    res = 0
    for i in numbs:
        if i > 7:
            res += i
        else:
            res -= i
    print(res)
    pass


init_list = ["Edward", "Bella", "Jacob", "Alice"]
my_cool_function(init_list)

numbers = [1, 2, 3, 7, 90]
my_second_cool_function(numbers)
