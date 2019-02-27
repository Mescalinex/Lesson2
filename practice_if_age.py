# Условный оператор - Задание1(возраст)

age = int(input('Введите возраст: '))

if age <= 6:
    print("Детский сад")
elif age > 6 <= 17:
    print("Школа")
elif age > 17 <= 22:
    print("Вуз")
else:
    print("Работа")
