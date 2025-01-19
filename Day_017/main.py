from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    question = Question(questions["text"],questions["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    print("\n")
print("You´ve completed he quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
