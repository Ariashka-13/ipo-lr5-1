s = input("Введите строку ")  # ввод строки

d = len(s)  # длина строки
print("Длина строки: ", d)  # вывод длины строки

gl = "аоуыэиеёюяАОУЫЭИЕЁЮЯ" #гласные
gl_count = 0  # счетчик количества гласных
sg_count = 0  # счетчик количества согласных
for i in s:  # использование цикла
    if i in gl: #если есть гласные
        gl_count += 1 #рпабота счетчика количества гласных
    elif i.isalpha() == True: #если есть согласные
        sg_count += 1  # работа счетчика количества согласных

print("Количество гласных: ", gl_count)  # вывод количества гласных
print("Количество согласных: ", sg_count)  # вывод количества согласных
