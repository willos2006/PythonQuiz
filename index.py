import sys
from tkinter import * 
sys.path.insert(0, "./Questions")
from Questions import easy as e
from Questions import medium as m
from Questions import hard as h

window = Tk()
window.title("Quiz App")
window.geometry("300x200+10+20")
window.mainloop()

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
  difficulty()