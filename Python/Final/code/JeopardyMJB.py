from tkinter import *
import tkinter as tk
import psycopg2 as pg

conn = pg.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432"
)
cur = conn.cursor()
cur.execute("SELECT * FROM trivia ORDER by id LIMIT 50")

data = cur.fetchall()
id = [row[0] for row in data]
questions = [row[1] for row in data]  
answers = [row[2] for row in data]    
points = [row[3] for row in data]
cur.close()
conn.close()

window = tk.Tk()
window.title("Matt's Jeopardy")
window.geometry("725x600")
window.configure(bg="black")

# Initialize score and score label
score = 0
score_label = tk.Label(window, text=f"Score: {score}", bg="black", fg="white", font=("Arial", 20))
score_label.grid(row=5, column=0, columnspan=6, pady=10)

def show_question(index, button):
    question_window = tk.Toplevel(window)
    question_window.title("Question")
    question_window.geometry("600x400")
    question_window.configure(bg="black")

    # Display the question
    question_label = tk.Label(question_window, text=questions[index], bg="black", fg="white", font=("Arial", 20), wraplength=500)
    question_label.pack(pady=20)

    # Entry for the answer
    answer_entry = tk.Entry(question_window, bg="black", fg="white", font=("Arial", 20))
    answer_entry.pack(pady=20)

    # Function to check the answer
    def check_answer():
        global score
        user_answer = answer_entry.get().strip().lower()
        if user_answer == answers[index]:
            score += points[index]
            result_text = "Correct!"
        else:
            result_text = f"Wrong! The correct answer was: {answers[index]}"
            score -= points[index]
        score_label.config(text=f"Score: {score}")
        button.config(state="disabled")  # Disable the button after answering
        result_label = tk.Label(question_window, text=result_text, bg="black", fg="white", font=("Arial", 16))
        result_label.pack(pady=10)
        close_button = tk.Button(question_window, text="Close", command=question_window.destroy, bg="black", fg="white", font=("Arial", 16))
        close_button.pack(pady=10)

    # Submit button
    submit_button = tk.Button(question_window, text="Submit", command=check_answer, bg="black", fg="white", font=("Arial", 20))
    submit_button.pack(pady=20)



question0 = tk.Button(window, text=points[0], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(0))
question0.grid(row=0, column=0, padx=10, pady=10)

question1 = tk.Button(window, text=points[1], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(1))
question1.grid(row=0, column=1, padx=10, pady=10)

question2 = tk.Button(window, text=points[2], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(2))
question2.grid(row=0, column=2, padx=10, pady=10)

question3 = tk.Button(window, text=points[3], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(3))
question3.grid(row=0, column=3, padx=10, pady=10)

question4 = tk.Button(window, text=points[4], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(4))
question4.grid(row=0, column=4, padx=10, pady=10)

question5 = tk.Button(window, text=points[5], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(5))
question5.grid(row=1, column=0, padx=10, pady=10)

question6 = tk.Button(window, text=points[6], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(6))
question6.grid(row=1, column=1, padx=10, pady=10)

question7 = tk.Button(window, text=points[7], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(7))
question7.grid(row=1, column=2, padx=10, pady=10)

question8 = tk.Button(window, text=points[8], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(8))
question8.grid(row=1, column=3, padx=10, pady=10)

question9 = tk.Button(window, text=points[9], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(9))
question9.grid(row=1, column=4, padx=10, pady=10)

question10 = tk.Button(window, text=points[10], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(10))
question10.grid(row=2, column=0, padx=10, pady=10)

question11 = tk.Button(window, text=points[11], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(11))
question11.grid(row=2, column=1, padx=10, pady=10)

question12 = tk.Button(window, text=points[12], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(12))
question12.grid(row=2, column=2, padx=10, pady=10)

question13 = tk.Button(window, text=points[13], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(13))
question13.grid(row=2, column=3, padx=10, pady=10)

question14 = tk.Button(window, text=points[14], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(14))
question14.grid(row=2, column=4, padx=10, pady=10)

question15 = tk.Button(window, text=points[15], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(15))
question15.grid(row=3, column=0, padx=10, pady=10)

question16 = tk.Button(window, text=points[16], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(16))
question16.grid(row=3, column=1, padx=10, pady=10)

question17 = tk.Button(window, text=points[17], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(17))
question17.grid(row=3, column=2, padx=10, pady=10)

question18 = tk.Button(window, text=points[18], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(18))
question18.grid(row=3, column=3, padx=10, pady=10)

question19 = tk.Button(window, text=points[19], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(19))
question19.grid(row=3, column=4, padx=10, pady=10)

question20 = tk.Button(window, text=points[20], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(20))
question20.grid(row=4, column=0, padx=10, pady=10)

question21 = tk.Button(window, text=points[21], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(21))
question21.grid(row=4, column=1, padx=10, pady=10)

question22 = tk.Button(window, text=points[22], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(22))
question22.grid(row=4, column=2, padx=10, pady=10)

question23 = tk.Button(window, text=points[23], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(23))
question23.grid(row=4, column=3, padx=10, pady=10)

question24 = tk.Button(window, text=points[24], bg="white", fg="black", font=("Arial", 20), command=lambda: show_question(24))
question24.grid(row=4, column=4, padx=10, pady=10)

window.mainloop()