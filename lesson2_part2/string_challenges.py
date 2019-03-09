import re
from collections import Counter

# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[len(word)-1])
# k

# Вывести количество букв а в слове
word = 'Архангельск'
print(word.lower().count('а'))
# 2

# Вывести количество гласных букв в слове
word = 'Архангельск'
print(len(re.findall('[а, у, о, ы, и, э, я, ю, ё, е]', word.lower())))
# 3

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))
# 4

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence = sentence.split(" ") #['мы]
for string_line in sentence:
    print(string_line[0])



# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
print(int(len(sentence)) / int(len(sentence.split())))


import datetime
from datetime import datetime
date_string = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)