import numpy as np
import pandas as pd

class AddKeyWords():
    standard_keywords = np.array([ "what", "speed", "find", "length", "seconds", "time"])
    def addnewkeyword(self, newkeyword):
        self.standard_keywords.append(newkeyword)
        

class QuestionClassification():     
     def __init__(self, question_text):
         self.question_text = question_text

     def get_question_words(self):
         return list(self.question_text.split(" "))

     def get_question_keywords(self):
         question_keywords = np.array(self.get_question_words())
         print("Question Keywords", question_keywords)
         return question_keywords



question = pd.read_csv("Bank/Question_Papers.csv")

question_text = question["question_text"]
"""print(question.head)
print("*********************************************")
print(question_text)
print("*********************************************")
print(question_text[0]) """
question_type = QuestionClassification(question_text[0])
question_1_key = question_type.get_question_keywords()
next_question_type = QuestionClassification(question_text[1])
question_2_key = next_question_type.get_question_keywords()
print(np.intersect1d(question_1_key,question_2_key))
print(np.setdiff1d(question_1_key,question_2_key))
print(np.setdiff1d(question_2_key,question_1_key))
