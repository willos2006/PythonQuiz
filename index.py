import sys
import tkinter as tk
from tkinter import messagebox
sys.path.insert(0, "./Questions")
from Questions import easy as e
from Questions import medium as m
from Questions import hard as h

# App Rendering
class mainUI(tk.Tk):
  
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    self.title("Quiz App")
    self.geometry("1000x500")
    self.resizable(False, False)
    self.protocol("WM_DELETE_WINDOW", self.on_closing)

    self.frames = {}
    container = tk.Frame(self)
    for F in (startPage):
      page_name = F.__name__
      frame = F(parent=container, controller=self)
      self.frames[page_name] = frame
      frame.grid(row=0, column=0, sticky="nsew")
    self.show_frame("StartPage")

  def on_closing(self):
    if messagebox.askokcancel("Quit", "Are you sure?"):
      self.destroy()
  
  def show_frame(self, page_name):
    frame = self.frames[page_name]
    frame.tkraise()

class startPage(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    label = tk.Label(self, text="        Home Page        ", font=self.controller.title_font,fg="#263942")
    label.grid(row=0, sticky="ew")
    


def diffRedirect():
  difficulty()

def difficulty():
  print('Please select a difficulty.')
  print('1 - easy')
  print('2 - medium')
  print('3 - hard')
  print("")
  difficulty = input('')

  if difficulty == '1':
    for i in e.questions:
      print(i.body)
      print(i.answer)
      print("")

  elif difficulty == '2':
    for i in m.questions:
      print(i.body)
      print(i.answer)
      print("")

  elif difficulty == '3':
    for i in h.questions:
      print(i.body)
      print(i.answer)
      print("")
  
  elif difficulty == 'easy':
      for i in e.questions:
        print(i.body)
        print(i.answer)
        print("")

  elif difficulty == 'medium':
    for i in m.questions:
      print(i.body)
      print(i.answer)
      print("")

  elif difficulty == 'hard':
    for i in h.questions:
      print(i.body)
      print(i.answer)
      print("")
  else:
    print('Invalid Input')
    diffRedirect()


if __name__ == '__main__':
  app = mainUI()
  app.mainloop()