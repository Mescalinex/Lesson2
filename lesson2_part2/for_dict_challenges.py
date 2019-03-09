from collections import Counter
import operator

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
def solution():
    names = []
    for n in students:
        x = n['first_name']
        names.append(x)
    b = Counter(names)    
    for i in b:
        print(f'{i}: {b.get(i)}') 
    
#solution()
    
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

def solution_one():
    names = []
    for n in students:
        x = n['first_name']
        names.append(x)

    b = Counter(names)   
    v = list(b.values())
    k = list(b.keys())    
    print('Самое частое имя среди учеников:', k[v.index(max(v))])
    
#solution_one()

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]


def solution_two():
    names_one = []
    for n in school_students[0]:
        x = n['first_name']
        names_one.append(x)
        b = Counter(names_one)
    print(f'Самое частое имя в классе 1: {max(zip(b.values(), b.keys()))[1]}')
    
    names_two = []
    for n in school_students[1]:
        x = n['first_name']
        names_two.append(x)
        b1 = Counter(names_two)
    print(f'Самое частое имя в классе 2: {max(zip(b1.values(), b1.keys()))[1]}')  
    
#solution_two()    


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

def solution_three():
  for n in school:
    names = []
    for i in n['students']:
      names.append(is_male[i['first_name']])
    b = Counter(names)   
    print(f"В классе {n['class']} - {b[False]} девочек и {b[True]} мальчиков")
    
solution_three()

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
def solution_man():
  for n in school:
    names = []
    for i in n['students']:
      names.append(is_male[i['first_name']])
    b = Counter(names)
    if max(zip(b.values(), b.keys()))[1] == True:
      print(f'Больше всего мальчиков в классе {(school.index(n)) + 1}')     
    else:
      print(f'Больше всего девочек в классе: {(school.index(n)) + 1}')

#solution_man()

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
