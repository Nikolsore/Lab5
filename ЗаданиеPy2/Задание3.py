list1 = list(map(int, input("Введите первый список: ").split()))
list2 = list(map(int, input("Введите второй список: ").split()))

# Нахождение общих элементов 
common = set(list1).intersection(list2)

# Сохранение порядка первого списка
seen = set()
result = []
for num in list1:
    if num in common and num not in seen:
        result.append(str(num))
        seen.add(num)

# вывод
print("Общие элементы:", ' '.join(result))
