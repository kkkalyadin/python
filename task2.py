time=int(input("Введите время в секундах:"))
hours = time // 3600
min = (time - hours * 3600) // 60
sec = time - (hours * 3600 + min * 60)
print (f"{hours}:{min}:{sec}")