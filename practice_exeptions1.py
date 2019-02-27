answers = {
    'как дела?': ' Хорошо!',
    'что делаешь?': ' Программирую',
    'как погода?': ' Холодно',
    'ты бот?': ' Нет!'
} 

def get_answer(question, answers):
    return answers.get(question)

def ask_user(answers):
    while True:
        try:
            user_input = input('Задай вопрос: ').lower()
            if user_input in answers:
                answer = get_answer(user_input, answers)
                print(answer)
            elif user_input == 'пока':
                print("Пока!")
                break
            else:
                print('Может другой вопрос? ')
        except(KeyboardInterrupt):
            print("Пока!")
            break

if __name__ == "__main__":
    ask_user(answers)
