def numb_recognizer(string: str):
    incorrect = ""
    if string[0] == "-":
        pos_or_neg = "отрицательное "
    else:
        pos_or_neg = "положительное "
    if string.isdigit() or string.lstrip('-').isdigit():
        fract = "целое "
    elif string.lstrip('-').replace('.', '', 1).isdigit():
            fract = "дробное "
            if pos_or_neg and string[0] == "-" and string[1] == ".":
                string = string[:1] + "0" + string[1:]
    else:
        pos_or_neg = ""
        fract = ""
        incorrect = "некорретное "
    print(f"Вы ввели {pos_or_neg}{fract}{incorrect}число: {string}")
    return


init_str = input("Введите строку для проверки: ")
numb_recognizer(init_str)
