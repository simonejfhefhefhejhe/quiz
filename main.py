questions = {""
             "сколько планет в солчной системе?": "8",
                                                  "столица Франии?": "Париж"}
score = 0

for q, a in questions.items():
    user_answer = input(q + " ")
    if user_answer.lower() ==a.lower():
        print("правильно ")
        score += 1

    else:
        print("неверно")

print (f"ваш результат: {score} из {len(questions)}")
