def find_sec_numb(where_find):
    number = ""
    for c in range(len(where_find)):
        if where_find[c].isdigit():
            number += where_find[c]
        else:
            break
    return number


def find_first_numb(where_find):
    n = where_find[::-1]
    number = ""
    for y in range(len(n)):
        if n[y].isdigit():
            number += n[y]
        else:
            break
    return number[::-1]


def exponent(pos, input_expression):
    find_first = input_expression[:pos]
    first_num = find_first_numb(find_first)

    find_second = input_expression[pos+1:]
    second_num = find_sec_numb(find_second)

    res = int(first_num) ** int(second_num)
    print("exp", first_num ,"and", second_num,"=", res)

    tochange = first_num + "*" + second_num
    return input_expression.replace(str(tochange), str(res))


def multi(pos, input_expression):
    find_first = input_expression[:pos]
    first_num = find_first_numb(find_first)

    find_second = input_expression[pos+1:]
    second_num = find_sec_numb(find_second)

    res = int(first_num)*int(second_num)
    print("multi", first_num ,"and", second_num,"=", res)

    tochange = first_num + "*" + second_num
    return input_expression.replace(str(tochange), str(res))


def modulo(pos, input_expression):
    find_first = input_expression[:pos]
    first_num = find_first_numb(find_first)

    find_second = input_expression[pos+1:]
    second_num = find_sec_numb(find_second)

    res = int(first_num) % int(second_num)
    print("modulo", first_num ,"and", second_num,"=", res)

    tochange = first_num + "%" + second_num
    return input_expression.replace(str(tochange), str(res))


def div(pos, input_expression):
    find_first = input_expression[:pos]
    first_num = find_first_numb(find_first)

    find_second = input_expression[pos+1:]
    second_num = find_sec_numb(find_second)

    res = int(int(first_num)/int(second_num))
    print("division", first_num ,"and", second_num,"=", res)

    tochange = first_num + "/" + second_num
    return input_expression.replace(str(tochange), str(res))


def sum(pos, input_expression):
    find_first = input_expression[:pos]
    first_num = find_first_numb(find_first)

    find_second = input_expression[pos+1:]
    second_num = find_sec_numb(find_second)

    res = int(first_num)+int(second_num)
    print("sum", first_num ,"and", second_num,"=", res)

    tochange = first_num + "+" + second_num
    return input_expression.replace(str(tochange), str(res))


def sub(pos, input_expression):
    find_first = input_expression[:pos]
    first_num = find_first_numb(find_first)

    find_second = input_expression[pos+1:]
    second_num = find_sec_numb(find_second)

    res = int(first_num)-int(second_num)
    print("sub", first_num ,"and", second_num,"=", res)

    tochange = first_num + "-" + second_num
    return input_expression.replace(str(tochange), str(res))


def mul_div_mod(input_expression):
    dictionary_ord = {}

    if "*" in input_expression:
        position_multi = input_expression.find("*")
        dictionary_ord[position_multi] = "*"
    if "/" in input_expression:
        position_div = input_expression.find("/")
        dictionary_ord[position_div] = "/"
    if "%" in input_expression:
        position_mod = input_expression.find("%")
        dictionary_ord[position_mod] = "%"

    dictionary_order = sorted(dictionary_ord.keys())
    pos = dictionary_order[0]
    sign = dictionary_ord.__getitem__(pos)

    if sign == "*":
        input_expression = multi(pos, input_expression)
    if sign == "/":
        input_expression = div(pos, input_expression)
    if sign == "%":
        input_expression = modulo(pos, input_expression)
    print(input_expression)
    return input_expression


def plus_min(input_expression):
    dictionary_ord = {}

    if "+" in input_expression:
        position_plus = input_expression.find("+")
        dictionary_ord[position_plus] = "+"
    if "-" in input_expression:
        position_min = input_expression.find("-")
        dictionary_ord[position_min] = "-"

    dictionary_order = sorted(dictionary_ord.keys())
    pos = dictionary_order[0]
    sign = dictionary_ord.__getitem__(pos)

    if sign == "+":
        input_expression = sum(pos, input_expression)
    if sign == "-":
        input_expression = sub(pos, input_expression)
    print(input_expression)
    return input_expression


try:
    operands = ["+", "-", "*", "/", "%", "**"]
    input_expression = input("Enter an expression without spaces with signs +, - , / , % , *, **: ")
    
    for i in range(len(input_expression)):
        if not (input_expression[i].isdigit() or input_expression[i] in operands):
            print("Wrong input!")
            exit()

    if "**" in input_expression:
        count_exp = input_expression.count("**")
        for i in range(count_exp):
            position_exp = input_expression.find("**")
            input_expression = input_expression[:position_exp] + input_expression[position_exp+1:]
            input_expression = exponent(position_exp, input_expression)
            print(input_expression)

    if "*" in input_expression or "/" in input_expression or "%" in input_expression:
        count = input_expression.count("*") + input_expression.count("/") + input_expression.count("%")
        for i in range(count):
            input_expression = mul_div_mod(input_expression)

    if "+" in input_expression or "-" in input_expression:
        count = input_expression.count("+") + input_expression.count("-")
        for i in range(count):
            input_expression = plus_min(input_expression)

except ValueError as err:
    print(f"Something goes wrong! Try again")
