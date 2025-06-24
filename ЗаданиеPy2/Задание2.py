dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

# Получаем множество ключей
keys_set = set(dct.keys())

# Получаем множество значений
values_set = set(dct.values())

# Объединение множеств
combined_set = keys_set | values_set

# результаты
print(f"Множество ключей: {keys_set}")
print(f"Множество значений: {values_set}")
print(f"Объединение множеств: {combined_set}")
