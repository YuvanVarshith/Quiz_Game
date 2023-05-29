from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for lp in range(len(question_data)):
    ques = question_data[lp]["question"]
    ans = question_data[lp]["correct_answer"]
    new_question = Question(ques, ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("you have completed the quiz")
print(f"Your Final Score is {quiz.score}/ {len(quiz.question_list)}")
