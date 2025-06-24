words = input("Введите строку: ").lower().split()

# Создаем словарь для подсчета количества
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

seen = set()
result = []
for word in words:
    if word not in seen:
        result.append(f"{word}: {word_counts[word]}")
        seen.add(word)

# Вывод
print("\n".join(result))
