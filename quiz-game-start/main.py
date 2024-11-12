from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:

    new_question = Question(item["question"], item["correct_answer"])
    question_bank.append(new_question)

my_quiz = QuizBrain(question_bank)

while my_quiz.still_has_questions():
    my_quiz.get_question()

print(f"You've completed the quiz! Your final score is {my_quiz.score}/{my_quiz.question_number}")