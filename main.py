import time
questions = {
             "сколько планет в солчной системе?": "8",
                                                  "столица Франии?": "Париж"}
score = 0

for q, a in questions.items():
    start_time = time.time()
    user_answer = input(q + " ")
    end_time = time.time()
    if round(end_time - start_time, 1 ) > 5:
        print('вы не уложились в таймер 5 секнд')
        user_answer = 'wrong'
    print (f"врем ответа : {round(end_time - start_time, 1)} сек ")
    if user_answer.lower() ==a.lower():
        print("правильно ")
        score += 1

    else:
        print("неверно")

print (f"ваш результат: {score} из {len(questions)}")



