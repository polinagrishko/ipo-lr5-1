s = str(input("Введите строку (на русском языке): ")) # Ввод строки 
count = 0
count2 = 0
s_low = s.lower()
glasnie = set("ауоиэыяюеё") # множество гласных
soglasnie = set("бвгджзйклмнпрмтфхцчшщ") # множество согласных
for letter in s_low:
    if letter in glasnie:
        count += 1
    elif letter in soglasnie:
        count2 += 1
print(f"Длина строки:{len(s)}, количество гласных букв: {count}, количество согласных букв:{count2}") # вывод 