class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list 

    def still_has_questions(self):
        return self.question_number==len(self.question_list)
    
    def next_question(self):
        # for i in range (len(self.question_list)):
            self.this_question=input(f"Q{self.question_number+1}: {self.question_list[self.question_number].text} (True/False): ")
            self.question_number+=1
            # if self.this_question != self.question_list[self.question_number].answer: