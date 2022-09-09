def calc_count(numb: int, my_list: list):
    counter = 0
    while numb in my_list:
        counter += 1
        my_list.remove(numb)
    return counter


init_list = [4, 4, 7, 4, 7, 2, 3, 3]
init1_list = [4, 4, 7, 4, 7, 2, 3, 3]
dictionary = {}
dictionary1 = {}

new_list = set(init_list)
for i in new_list:
    dictionary[i] = calc_count(i, init_list)

print(f"The number of occurrences of each number in the list is {dictionary}")

#через лямбду функцию
for numb in init1_list:
    if numb not in dictionary1:
        dictionary1[numb] = (lambda n, ln: sum([1 for j in ln if n == j]))(numb, init1_list)
print(dictionary1)
