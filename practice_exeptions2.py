def get_summ(num_one, num_two):
    try:
        result = int(num_one) + int(num_two)
        print(result)
    except ValueError:
        print('Введите числа!')

num_one = input('Введите первое число ')
num_two = input('Введите второе число ')

get_summ(num_one, num_two)
