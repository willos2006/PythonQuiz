from dataclasses import dataclass

@dataclass
class Question:
    body: str
    answer: str

    def __init__(self, body: str, answer: str):
        self.body = body
        self.answer = answer

questions = []

#q1
questions.append(Question('Question 1 easy', 'Q1 Answer'))

#q2
questions.append(Question('Question 2 easy', 'Q2 Answer'))

#q3
questions.append(Question('Question 3 easy', 'Q3 Answer'))
