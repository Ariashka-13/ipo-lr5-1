s = str(input("Введите строку "))  # ввод строки

d = len(s)  # длина строки
print("Длина строки: ", d)  # вывод длины строки

gl_count = 0  # счетчик количества гласных
sg_count = 0  # счетчик количества согласных
for i in s:  # использование цикла
    if i == "а" or i == "о" or i == "у" or i == "ы" or i == "и" or i == "е" or i == "ё" or i == "ю" or i == "я" or i == "э": # если есть гласные в строке
        gl_count += 1# работа счетчика количества гласныхi == "а" or 
    elif i != " ": #если есть пробел
        pass #пропускаем
    else: #если есть согласные
        sg_count += 1  # работа счетчика количества согласных

print("Количество гласных: ", gl_count)  # вывод количества гласных
print("Количество согласных: ", sg_count)  # вывод количества согласных
