import tkinter as tk

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

def start():
    goButton = tk.Button(
        text = "Start!",
        bg="green",
        height = 5,
        width = 25,
        command = lambda: startRound()
    )
    goButton.pack()

    window.geometry("960x540")
    window.resizable(False, False)
    window.mainloop()