from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    text = item['text']
    answer = item['answer']
    question = Question(text, answer)
    question_bank.append(question)
quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")