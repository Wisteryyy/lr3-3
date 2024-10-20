d=int(input("Введите день: ")) # вводим день
m=int(input("Введите месяц: ")) # вводим месяц

def season(d, m): # при помощи def создаем функцию которая при помощи if, elif, else определяет к какому времени года относится дата
    if (m == 3 and d >= 1) or (m == 4) or (m == 5) or (m == 6 and d < 1):
        return "Весна"
    elif (m == 6 and d >= 1) or (m == 7) or (m == 8) or (m == 9 and d < 1):
        return "Лето"
    elif (m == 9 and d >= 1) or (m == 10) or (m == 11) or (m == 12 and d < 1):
        return "Осень"
    else:
        return "Зима"

vremya_goda=season(d,m) # присваиваем переменной значение функции season
print("Эта дата относится к сезону", vremya_goda) # выводи переменную
