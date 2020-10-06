import tkinter as tk
from tkinter import messagebox
import mainGUI
import sys
sys.path.insert(0, '././questionScripts')
sys.path.insert(0, '././')
import round1_easy as q
import main
questionNo = 0

window = mainGUI.window
mainGUI.clear()

title = tk.Label(
    text="Round 1",
    font = (None, 30)
)
title.pack()

def questionDone(answer):
    answer = str(answer)
    global questionNo
    if answer == '':
        messagebox.showerror(message="Please type an answer", title="Invalid Answer")
    elif answer.lower() != q.questions[questionNo].answer.lower():
        messagebox.showerror(message="Wrong! The correct answer was "+str(q.questions[questionNo].answer), title="Wrong Answer!")
        questionNo += 1
        mainGUI.clear()
        loadQuestion()
    else:
        messagebox.showinfo(title="Correct Answer!", message="You were correct! You have gained a point")
        questionNo += 1
        main.score += 1
        print(main.score)
        mainGUI.clear()
        loadQuestion()

def loadQuestion():
    try:
        global questionNo
        global doneButton
        tk.Label(text = (str(questionNo + 1) + ") " + str(q.questions[questionNo].question)), font = (None, 15), wraplength = 1000, justify = "center").pack()
        if(q.questions[questionNo].multipleChoice):
            tk.Label(text = ("A) " + str(q.questions[questionNo].a1)), font = (None, 10), wraplength = 1000).pack()
            tk.Label(text = ("B) " + str(q.questions[questionNo].a2)), font = (None, 10), wraplength = 1000).pack()
            tk.Label(text = ("C) " + str(q.questions[questionNo].a3)), font = (None, 10), wraplength = 1000).pack()
            tk.Label(text = ("D) " + str(q.questions[questionNo].a4)), font = (None, 10), wraplength = 1000).pack()
        line = tk.Label(text="\n\n").pack()
        tk.Label(text="Enter Answer:", font = (None, 14)).pack()
        text = tk.Entry(bd=3)
        text.pack(ipadx=50, ipady=10)
        tk.Label(text='\n\n').pack()
        doneButton = tk.Button(text="Submit Answer", height = 1, width = 15, bg = "blue", fg = "white", font = (None, 20), command=lambda: questionDone(text.get())).pack()

    except:
        tk.Label(text = "Round over! You got a score of: " + str(main.score), font = (None, 15), wraplength = 1000, justify = "center").pack()

loadQuestion()