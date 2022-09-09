print(list(map(lambda x: "Even" if x % 2 == 0 else "Odd", [1, 2, 3, 4, 6, 8])))

print(list(map(lambda x: str(x), [1, 2, 3, 4, 6, 8])))

my_tuple = ("kek", "lol", "loop")
print(list(filter(lambda x: str(''.join(reversed(x))) == x, my_tuple)))
