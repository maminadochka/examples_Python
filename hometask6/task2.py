str1 = input("Enter 1 string: ")
str2 = input("Enter 2 string: ")
str3 = input("Enter 3 string: ")
str4 = input("Enter 4 string: ")

my_cool_file = open("task_2_file", "a")

my_cool_file.write(str1 + '\n')
my_cool_file.write(str2 + '\n')

my_cool_file.close()

my_cool_file = open("task_2_file", "r+")
lines = my_cool_file.readlines()

my_cool_file.seek(0)

my_cool_file.write(str3 + '\n')
my_cool_file.write(str4 + '\n')

for line in lines:
    my_cool_file.write(line)

my_cool_file.close()
