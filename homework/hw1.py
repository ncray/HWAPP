from question import Question,Homework
import random

class AdditionQuestion(Question):
    name = 'addquest'
    points = 5
    
    def __init__(self,seed):
        random.seed(seed)
        self.a = random.randint(1,9)
        self.b = random.randint(1,9)
        self.c = random.randint(100,999)
        self.body = 'What is ' + str(self.a) + ' + ' + str(self.b) + '? <<int>> \nWhat is ' + str(self.a) + ' + ' + str(self.c) + '? <<int>>'
        self.set_types()

    def check_ans(self,ans):
        points = 0
        correct = [False,False]
        comments = ''
        if ans[0]==self.a+self.b:
            points += 2
            correct[0] = True
        elif ans[0]:
            comments += "You can't even do simple math? Shame on you!<br>"
        if ans[1]==self.a+self.c:
            points += 3
            correct[1] = True
            comments += 'Well done! That was tough.'
        return {"points": points, "correct": correct, "comments": comments}

class MultiplicationQuestion(Question):
    name = 'multquest'
    points = 5
    
    def __init__(self,seed):
        random.seed(seed+1)
        self.a = random.randint(1,9)
        self.b = random.randint(1,9)
        self.body = 'What is ' + str(self.a) + ' x ' + str(self.b) + '? \n Ans: <<int>>'
        self.set_types()

    def check_ans(self,ans):
        if ans[0]==self.a*self.b:
            return {"points": 5, "correct": [True], "comments": ''}
        elif ans[0]:
            return {"points": 0, "correct": [False], "comments": 'Review your multiplication table!'}

homework = Homework(id=1,name='Homework 1: Basic Arithmetic',
                             questions=[AdditionQuestion,MultiplicationQuestion])
