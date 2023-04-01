THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # creating the window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.quiz = quiz_brain
        # score label ui
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Ui to show the highest score
        self.high_score_label = Label(text=f"Highest Score: {self.quiz.high_score}", fg="white", bg=THEME_COLOR)
        self.high_score_label.grid(row=0, column=0)

        # UI to show the question
        self.canvas = Canvas(self.window, bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, text="some questions", fill=THEME_COLOR,
                                                     width=280,
                                                     font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True button ui
        true_image = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_image, highlightthickness=0, command=self.true_check)
        self.true_btn.grid(row=2, column=0)

        # False button ui
        false_image = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_image, highlightthickness=0, command=self.false_check)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")

    def true_check(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_check(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.high_score_label.config(text=f"Highest Score: {self.quiz.high_score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
