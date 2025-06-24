numbers_str = input("Введите числа через пробел: ").split()

processed = []
for s in numbers_str:
    try:
        num = int(s)
    except ValueError:
        try:
            num = float(s)
        except ValueError:
            num = s
    processed.append(num)

degree = int(input("Введите степень: "))


result = []
for elem in processed:
    if isinstance(elem, (int, float)):
        powered = elem ** degree
        if isinstance(powered, float) and powered.is_integer():
            powered = int(powered)
        result.append(str(powered))
    else:
        result.append(elem * degree)

print("Вывод:", ' '.join(result))
