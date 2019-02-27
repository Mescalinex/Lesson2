#  Условный оператор - Задание2(строки) -

str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
word = "learn"
if( str1.isdigit() or str2.isdigit()):
    print("0")
if str1 == str2:
    print("1")
if len(str1) > len(str2):
    print("2")
if str1 != str2 and word in str2:
    print("3")
    