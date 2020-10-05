from dataclasses import dataclass

@dataclass
class Question:
    body: str
    answer: str

    def __init__(self, body: str, answer: str):
        self.body = body
        self.answer = answer

questions = []

#q test
questions.append(Question('This is the body', 'This is the answer'))