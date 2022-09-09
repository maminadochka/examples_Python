print("TASK1")
print("Same id and data:")
k = 10
a = 10
print(k, "-", id(k), " ", a, "-", id(a))

print("\nSame only data:")
list_k = [1, 3, 't']
list_a = [1, 3, 't']
print(list_k, "-", id(list_k), " ", list_a, "-", id(list_a))

print("\nNow same id and data:")
tuple_k = (1, 3, 't')
tuple_a = (1, 3, 't')
print(tuple_k, "-", id(tuple_k), " ", tuple_a, "-", id(tuple_a), "\n\n")


print("TASK2")
st = "abcdefgjshdfk"
st1 = ""
st2 = ""
print(st, "\n \n")
i = 0
for i in range(len(st)):
    if i % 2 == 0:
        st1 += st[i]
    else:
        st2 += st[i]
print(st1, "   ", st2)
j = 0
while j != 30:
    print("=", end='')
    j += 1


print("\n\nTASK3")
my_list = [1, 2, '6', 8]
print(my_list)
my_list.reverse()
print(my_list)


print("\n\nTASK4")
numb = "567890"
print("Numb =", numb)
sum = 0
for i in range(len(numb)):
    sum += int(numb[i])
print("Sum of all numbers =", sum)


print("\n\nTASK5")
string = "011777793123227166666788"
print(string)
count = 0

checked_numb = ""
for numb in string:
    if numb in checked_numb:
        continue
    else:
        checked_numb += numb

count_str = ""
for ch_numb in range(len(checked_numb)):
    for numb in range(len(string)):
        count = string.count(checked_numb[ch_numb])
    count_str += str(count)

checked_count = 0
dictionary = {}
for y in range(len(count_str)):
    index = y
    for ch_numb in range(len(checked_numb)):
        if index == ch_numb:
            dictionary[int(checked_numb[ch_numb])] = int(count_str[y])

print("\nThe number of occurrences of each number:")
print(dictionary)

print("\n3 maximum repeated digits:")
i = 0
while i < 3:
    my_key = max(dictionary, key=dictionary.get)
    print(my_key, ":", dictionary[my_key])
    del dictionary[my_key]
    i += 1
