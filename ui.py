from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)
        self.label = Label(text=f"Score : {0}", bg=THEME_COLOR,  fg="white")
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.qn_text = self.canvas.create_text(150, 125, width=280, text="", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        false = PhotoImage(file="images/false.png")
        true = PhotoImage(file="images/true.png")
        self.button1 = Button(image=true, highlightthickness=0, command=self.true_btn)
        self.button1.config(padx=0, pady=20)
        self.button1.grid(column=0, row=2)
        self.button2 = Button(image=false, highlightthickness=0, command=self.false_btn)
        self.button2.config(padx=10, pady=20)
        self.button2.grid(column=1, row=2)
        self.next_qstn()


        self.window.mainloop()

    def next_qstn(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.qn_text, text=q_text)
        else:
            messagebox.showinfo(title="Game Over",
                                message=f"Thank you for playing your score was {self.quiz.score} / 10"
                                )
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")

    def true_btn(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_btn(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_qstn)
