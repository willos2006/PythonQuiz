#this defines the class structure for all questions
class Question:
    diff: int
    question: str
    answer: str
    multipleChoice: bool
    #'optional' params
    a1: str 
    a2: str 
    a3: str 
    a4: str

    def __init__(self, diff, question, answer, multipleChoice = False, a1 = None, a2 = None, a3 = None, a4 = None):
        self.diff = diff
        self.question = question
        self.answer = answer
        self.multipleChoice = multipleChoice
        self.a1 = a1 
        self.a2 = a2 
        self.a3 = a3 
        self.a4 = a4 