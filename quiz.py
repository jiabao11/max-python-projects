from tkinter import Tk, Label, Entry, Button, END, DISABLED
import random

tk = Tk()
tk.title("Maths Quiz!")

score = 0
lives = 3
questions = 20
question_number = 0
answer = None
numbers = list(range(1, 21))

# --- widgets ---
question_label = Label(tk, text="", font=("Arial", 14))
question_label.pack(pady=10)

entry = Entry(tk)
entry.pack()

feedback_label = Label(tk, text="", font=("Arial", 12))
feedback_label.pack(pady=5)

score_label = Label(tk, text=f"Score: {score}")
score_label.pack()

lives_label = Label(tk, text=f"Lives: {lives}")
lives_label.pack()

# --- functions ---

def next_question():
    global answer, question_number
    question_number += 1
    entry.delete(0, END)           # clear the entry box
    feedback_label.config(text="")

    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    decider = random.randint(0, 2)

    if decider == 0:
        question_label.config(text=f"Q{question_number}: {num1} + {num2} = ?")
        answer = num1 + num2
    elif decider == 1:
        if num2 > num1:
            num1, num2 = num2, num1    # swap so answer is never negative
        question_label.config(text=f"Q{question_number}: {num1} - {num2} = ?")
        answer = num1 - num2
    else:
        question_label.config(text=f"Q{question_number}: {num1} x {num2} = ?")
        answer = num1 * num2

def check():
    global score, lives
    typed = entry.get()

    if not typed.isdigit():
        feedback_label.config(text="Please enter a number!")
        return

    if int(typed) == answer:
        score += 1
        score_label.config(text=f"Score: {score}")
        feedback_label.config(text="Correct!")
    else:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")
        feedback_label.config(text=f"Wrong! Answer was {answer}")

    if lives == 0:
        question_label.config(text="Game over! Out of lives.")
        feedback_label.config(text=f"You solved {score} questions!")
        btn.config(state=DISABLED)
    elif score >= questions:
        question_label.config(text="Congrats! You won!")
        feedback_label.config(text=f"You had {lives} lives remaining.")
        btn.config(state=DISABLED)
    else:
        next_question()

btn = Button(tk, text="Submit", command=check)
btn.pack(pady=5)

# start the first question
next_question()

tk.mainloop()