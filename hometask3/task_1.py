first_try_flag: bool = True

while True:
    name = input("Enter your name: ")
    if not name.isalpha():
        first_try_flag = False
        continue
    else:
        break


while True:
    age = input("Enter your age: ")
    if not age.isdigit():
        if age[0] == '-':
            print(name, ", так не бывает!")
        first_try_flag = False
        continue
    elif 0 <= int(age) <= 3:
        print(name, ", ты слишком молодо выглядишь)")
        first_try_flag = False
        continue
    elif int(age) > 100:
        print(name, ", у нас столько не живут)")
        first_try_flag = False
        continue
    else:
        age = int(age)
        break

if age <= 10:
    print("Привет, шкет", name)
elif age <= 18:
    print("Как жизнь,", name, "?")
else:
    print("Чего желаете,", name, "?")

if first_try_flag:
    print("*ишь какой правильный попался) с первого раза все сделал*")
else:
    print("*вот сразу бы так, чего томил?*")
