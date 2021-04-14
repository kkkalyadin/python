a=int(input("Введите число:"))
max=a%10
while a>0:
    a=a//10
    if a%10> max:
        max=a%10

    else:
            print(f"Наибольшая цифра числа: = {max}")
            break