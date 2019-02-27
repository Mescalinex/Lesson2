# Цикл for - Задание 

students = [
{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '4b', 'scores': [4,3,3,4,5]},
{'school_class': '4c', 'scores': [2,5,4,4,3]}
]

a_mean = sum(students[0]['scores'])/len(students[0]['scores'])
b_mean = sum(students[1]['scores'])/len(students[1]['scores'])
c_mean = sum(students[2]['scores'])/len(students[2]['scores'])
school_mean = (a_mean + b_mean + c_mean)/3

print(f'Средняя по школе: {school_mean}')
print(f'Средняя по классу 4a: {a_mean}')
print(f'Средняя по классу 4b: {b_mean}')
print(f'Средняя по классу 4c: {c_mean}')
