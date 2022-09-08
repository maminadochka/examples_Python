def replace_func(a, b):
    a, b = b, a
    return a, b


dictionary = {'a': 2, 'b': 3, 'c': 4}
new_dictionary = {}

for i in dictionary:
    new_val, new_key = replace_func(i, dictionary[i])
    new_dictionary[new_val] = new_key

print(dictionary)
print(new_dictionary)
