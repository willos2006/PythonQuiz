import tkinter as tk
from tkinter import messagebox
import sys

window = tk.Tk()
title = tk.Label(
    text="Quiz App!",
    font = (None, 30)
)
title.pack()

def clear():
    for i in window.winfo_children():
        i.destroy()

def startRound():
    import Round1

def credits():
  messagebox.showinfo(
    title = "Credits",
    message = "This app was created by Tyler2P & willos2006."
  )

def start():
    goButton = tk.Button(
        text = "Start!",
        bg="green",
        height = 5,
        width = 25,
        command = lambda: startRound()
    )
    goButton.pack()
    creditButton = tk.Button(
      text = "Credits",
      bg = "blue",
      height = 5,
      width = 5,
      command = lambda: credits()
    )
    creditButton.pack()

    window.geometry("960x540")
    window.resizable(False, False)
    window.mainloop()