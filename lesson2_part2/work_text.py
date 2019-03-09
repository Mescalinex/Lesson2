with open('referat.txt', 'r', encoding = 'utf-8') as f:
    content = f.read()
    text_length = len(content)
    number_words = len(content.replace(' ', ',').split(','))
    text_exclamation_mark = content.replace('.', '!')
print(text_exclamation_mark)
with open('referat2.txt', 'w', encoding = 'utf-8') as f:
    f.write(text_exclamation_mark)
    