import random
import tkinter as tk
from tkinter import messagebox

# ---------- LOGIC (no tkinter in here) ----------
quiz_answer = {
    "What is 15 multiplied by 4?": "B",
    "What is the capital of Ghana?": "C",
    "How many sides does a hexagon have?": "B",
    "Which country has Lagos as its former capital?": "C",
    "What is the square root of 144?": "C",
    "Which West African country is famous for cocoa production?": "A",
    "How many days are in a leap year?": "C",
    "What is the largest ocean in the world?": "D",
    "What is 25% of 200?": "C",
    "Which country was formerly known as Dahomey?": "B",
    "How many states are in Nigeria?": "C",
    "What is the smallest prime number?": "C",
    "Which planet is known as the Red Planet?": "B",
    "What is the capital of Senegal?": "C",
    "How many minutes are in 3 hours?": "C",
    "Which West African country has Monrovia as its capital?": "B",
    "What is 100 divided by 4?": "B",
    "Which major river flows through Nigeria?": "C",
    "In which year did Nigeria gain independence?": "C",
    "How many degrees are in a right angle?": "C",
}

quiz = {
    "What is 15 multiplied by 4?": ("A. 45", "B. 60", "C. 65", "D. 75"),
    "What is the capital of Ghana?": ("A. Lagos", "B. Kumasi", "C. Accra", "D. Dakar"),
    "How many sides does a hexagon have?": ("A. 5", "B. 6", "C. 7", "D. 8"),
    "Which country has Lagos as its former capital?": ("A. Ghana", "B. Togo", "C. Nigeria", "D. Benin"),
    "What is the square root of 144?": ("A. 10", "B. 11", "C. 12", "D. 14"),
    "Which West African country is famous for cocoa production?": ("A. Ghana", "B. Niger", "C. Senegal", "D. Liberia"),
    "How many days are in a leap year?": ("A. 364", "B. 365", "C. 366", "D. 367"),
    "What is the largest ocean in the world?": ("A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"),
    "What is 25% of 200?": ("A. 25", "B. 40", "C. 50", "D. 75"),
    "Which country was formerly known as Dahomey?": ("A. Togo", "B. Benin", "C. Ghana", "D. Guinea"),
    "How many states are in Nigeria?": ("A. 30", "B. 35", "C. 36", "D. 37"),
    "What is the smallest prime number?": ("A. 0", "B. 1", "C. 2", "D. 3"),
    "Which planet is known as the Red Planet?": ("A. Venus", "B. Mars", "C. Jupiter", "D. Mercury"),
    "What is the capital of Senegal?": ("A. Bamako", "B. Conakry", "C. Dakar", "D. Lome"),
    "How many minutes are in 3 hours?": ("A. 120", "B. 150", "C. 180", "D. 240"),
    "Which West African country has Monrovia as its capital?": ("A. Sierra Leone", "B. Liberia", "C. Gambia", "D. Guinea"),
    "What is 100 divided by 4?": ("A. 20", "B. 25", "C. 30", "D. 40"),
    "Which major river flows through Nigeria?": ("A. River Nile", "B. River Congo", "C. River Niger", "D. River Zambezi"),
    "In which year did Nigeria gain independence?": ("A. 1957", "B. 1958", "C. 1960", "D. 1963"),
    "How many degrees are in a right angle?": ("A. 45", "B. 60", "C. 90", "D. 180"),
}

DIFFICULTY = {"easy": 5, "mid": 7, "hard": 10}


def questions(n):
    yield from random.sample(list(quiz.keys()), n)


def check_answer(question, choice):
    return choice.strip().lower() == quiz_answer[question].strip().lower()


def get_feedback(score, total):
    """A message for the final score."""
    if score == total:
        return "A perfect score for the Scholar!"
    if score == 0:
        return "Zero this time. Don't give up, try again!"
    if score / total >= 0.5:
        return "Above average, well done!"
    return "This is quite low, let's do better!"


# ---------- WINDOW CODE ----------
state = {"gen": None, "question": None, "score": 0, "total": 0, "answered": False}


def show_frame(frame):
    for f in (start_frame, quiz_frame, end_frame):
        f.pack_forget()
    frame.pack(fill="both", expand=True, padx=20, pady=15)


def start_game(level):
    state["gen"] = questions(DIFFICULTY[level])
    state["score"] = 0
    state["total"] = 0
    show_frame(quiz_frame)
    next_question()


def next_question():
    try:
        state["question"] = next(state["gen"])
    except StopIteration:
        finish_game()
        return
    state["total"] += 1
    state["answered"] = False
    selected.set("")
    question_label.config(text=state["question"])
    for rb, text in zip(option_buttons, quiz[state["question"]]):
        rb.config(text=text, value=text[0], state="normal")
    status_label.config(text="", fg="black")
    action_button.config(text="Submit", command=on_submit)
    progress_label.config(text=f"Question {state['total']}  |  Score: {state['score']}")


def on_submit():
    ans = selected.get()
    if not ans:
        messagebox.showwarning("No choice", "Please choose A, B, C or D.")
        return
    if check_answer(state["question"], ans):
        state["score"] += 1
        status_label.config(text="Correct", fg="green")
    else:
        right = state["question"]
        correct_letter = quiz_answer[right]
        status_label.config(text=f"Incorrect (answer: {correct_letter})", fg="red")
    state["answered"] = True
    for rb in option_buttons:
        rb.config(state="disabled")
    progress_label.config(text=f"Question {state['total']}  |  Score: {state['score']}")
    action_button.config(text="Next", command=next_question)


def finish_game():
    result_label.config(text=f"You scored {state['score']} / {state['total']}")
    feedback_label.config(text=get_feedback(state["score"], state["total"]))
    show_frame(end_frame)


root = tk.Tk()
root.title("Quiz Game")
root.geometry("460x380")

welcome_msg = (
    "Welcome to our quiz game!\n"
    "There are four options and one is the right choice.\n"
    "Let's get into it."
)

# --- start screen ---
start_frame = tk.Frame(root)
tk.Label(start_frame, text=welcome_msg, font=("Arial", 12)).pack(pady=15)
tk.Label(start_frame, text="Choose difficulty:").pack()
for level in DIFFICULTY:
    tk.Button(
        start_frame, text=level.capitalize(), width=12,
        command=lambda lv=level: start_game(lv),
    ).pack(pady=4)

# --- quiz screen ---
quiz_frame = tk.Frame(root)
progress_label = tk.Label(quiz_frame, text="")
progress_label.pack(anchor="e")
question_label = tk.Label(quiz_frame, text="", font=("Arial", 13, "bold"), wraplength=400)
question_label.pack(pady=10)
selected = tk.StringVar(value="")
option_buttons = []
for _ in range(4):
    rb = tk.Radiobutton(quiz_frame, text="", variable=selected, value="", anchor="w")
    rb.pack(fill="x", padx=40)
    option_buttons.append(rb)
status_label = tk.Label(quiz_frame, text="", font=("Arial", 11))
status_label.pack(pady=8)
action_button = tk.Button(quiz_frame, text="Submit", command=on_submit)
action_button.pack()

# --- end screen ---
end_frame = tk.Frame(root)
result_label = tk.Label(end_frame, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=20)
feedback_label = tk.Label(end_frame, text="", font=("Arial", 12), wraplength=400)
feedback_label.pack(pady=10)
tk.Button(end_frame, text="Play again", command=lambda: show_frame(start_frame)).pack(pady=5)
tk.Button(end_frame, text="Quit", command=root.destroy).pack()

show_frame(start_frame)
root.mainloop()
