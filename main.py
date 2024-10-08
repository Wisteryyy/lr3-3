# Время года
def season(day, month):
    if (month == 3 and day >= 1) or (month == 4) or (month == 5) or (month == 6 and day < 1):
        return "Весна"
    elif (month == 6 and day >= 1) or (month == 7) or (month == 8) or (month == 9 and day < 1):
        return "Лето"
    elif (month == 9 and day >= 1) or (month == 10) or (month == 11) or (month == 12 and day < 1):
        return "Осень"
    else:
        return "Зима"

# Ввод данных
day = int(input("Введите день (1-31): "))
month = int(input("Введите месяц (1-12): "))


if (1 <= day <= 31) and (1 <= month <= 12):
    season = season(day, month)
    print(f"Эта дата относится к сезону: {season}")
else:
    print("Некорректный ввод даты.")