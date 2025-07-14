questions=[
    {"question":"What is the capital of India?","answer":"Delhi"},
    {"question":"What is 5+7?","answer":"12"},
    {"question":"What planet is known as the red planet?","answer":"Mars"},
    {"question":"What is the chemical symbol of water?","answer":"H2O"}
]
score=0
for q in questions:
    user_answer=input(q["question"]+ " ")
    if user_answer.strip().lower()==q["answer"].lower():
        print("correct!")
        score+=1
    else:
        print(f"wrong answer! the correct answer is {q['answer']}")
print(f"final score is {score}/{len(questions)}")