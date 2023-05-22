from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial"


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.ques_text = self.canvas.create_text(150, 125,
                                                 text="here goes questions",
                                                 font=(FONT, 20, "italic"),
                                                 fill=THEME_COLOR,
                                                 width=280
                                                 )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.score_label.grid(column=1, row=0)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, command=self.true_pressed, highlightthickness=0, borderwidth=1)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_img, command=self.false_pressed, highlightthickness=0, borderwidth=1)
        self.false_button.grid(column=1, row=2)
        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text= q_text)
        else:
            self.canvas.itemconfig(self.ques_text, text="You have reached to the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer(user_answer="true")
        self.feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer(user_answer="false")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
