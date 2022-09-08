n_list = [4, 4, 4, 4, 7, 9, 7, 9]
numb_set = set()

for i in range(len(n_list)):
    cn = n_list.count(n_list[i])
    if i not in numb_set:
        for j in range(1, cn+1):
            numb_set.add(str(n_list[i]) * j)

print(numb_set)
