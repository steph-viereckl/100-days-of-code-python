from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    # This parameter means that this parameter quiz_brain must be of the datatype QuizBrain
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, pady=20)

        # Question Canvas
        self.question_canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_text = self.question_canvas.create_text(
            150,
            125,
            width=280, # This makes the text wrap
            text="Hello",
            font=("Arial", 20, "italic")
        )
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=20)

        # Correct Button
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_img,
            command=self.mark_true,
            highlightthickness=0
        )
        self.true_button.grid(column=0, row=2, pady=20)

        # Incorrect Button
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_img,
            command=self.mark_false,
            highlightthickness=0
        )
        self.false_button.grid(column=1, row=2, pady=20)

        self.get_next_question()
        self.window.mainloop()

    ############## Additional Methods #############
    def get_next_question(self):

        self.question_canvas.configure(bg="white")

        if self.quiz.still_has_questions():
            # Get question from Quiz Brain
            question_text = self.quiz.next_question()
            # Update the Canvas with the new Canvas Text Question
            self.question_canvas.itemconfig(self.canvas_text, text=question_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.question_canvas.itemconfig(self.canvas_text, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def mark_true(self):
        answer = self.quiz.check_answer("true")
        print(f"You got it right: {answer}")
        self.give_feedback(answer)

    def mark_false(self):
        answer = self.quiz.check_answer("false")
        print(f"You got it right: {answer}")
        self.give_feedback(answer)

    def give_feedback(self, answer):
        # Flash green for 1 second if right, otherwise flash red
        if answer:
            self.question_canvas.configure(bg="green")
        else:
            self.question_canvas.configure(bg="red")

        # Reset to next question
        self.window.after(1000, self.get_next_question)