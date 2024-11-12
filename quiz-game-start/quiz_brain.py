class QuizBrain:

    def __init__(self, question_list):

        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):

        return len(self.question_list) > self.question_number

    def get_question(self):

        # Get question from list
        current_question = self.question_list[self.question_number]
        # Increase by 1 so that it proceeds to the next question and that the number is not 0 indexed
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False?): ')
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Wrong!")

        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
