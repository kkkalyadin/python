a = float(input("Начальный результат"))
b = float(input("Конечный результат"))
days = 1
if a <= 0 or b <= 0 or b <= a:
    print("Введите правильные значения")
else:
    while a < b:
        a = a * 1.1
        days += 1

        print(f"Спортсмен достигнет результата за {days} дней")
