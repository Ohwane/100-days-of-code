from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
q_inc=0
q_bank=[]
for i in range (len(question_data)):
    q_bank.append(Question(question_data[q_inc]["text"],question_data[q_inc]["answer"]))
    q_inc+=1

quiz= QuizBrain(q_bank)

while quiz.still_has_questions():
    quiz.next_question()
    # self.question_list[self.question_number].text