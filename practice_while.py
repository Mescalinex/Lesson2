questions_answers = {
    'как дела?': ' Хорошо!',
    'что делаешь?': ' Программирую',
    'как погода?': ' Холодно',
    'ты бот?': ' Нет!'
} 

def ask_user(user_say):
    if user_say in questions_answers.keys():
        print(questions_answers[user_say])
    else:
        print('Может другой вопрос? ')



while True:
    ask_user(input('Задай вопрос: ').lower())
