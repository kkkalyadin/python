
a=float(input("Введите выручку фирмы"))
b=float(input("Введите издержки фирмы"))
if a > b:
    print(f"Фирма работает в плюс. Рентабельность фирмы =" ,   {a / b})
    workers=float(input("Введите количество работников"))
    print(f"Прибыль фирмы в расчете на одного сотрудника =" , {a / workers})
elif a==b:
    print("Фирма работает в ноль")
else:
     print("Фирма работает в минус")