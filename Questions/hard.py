from dataclasses import dataclass

@dataclass
class Question:
    body: str
    answer: str
    wAnswer1: str
    wAnswer2: str

    def __init__(self, body: str, answer: str, wAnswer1: str, wAnswer2: str):
        self.body = body
        self.answer = answer
        self.wAnswer1 = wAnswer1
        self.wAnswer2 = wAnswer2

questions = []

#q1
questions.append(Question('Question 1 hard', 'Q1 Answer', 'Q1 wrong answer', 'Q1 wrong answer'))

#q2
questions.append(Question('Question 2 hard', 'Q2 Answer', 'Q2 wrong answer', 'Q2 wrong answer'))

#q3
questions.append(Question('Question 3 hard', 'Q3 Answer', 'q2', 'q2'))
