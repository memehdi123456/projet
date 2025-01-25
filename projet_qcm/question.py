

########## ########## ##########  PROJET 1 ########## ########## ##########

import random

class Question:
    def __init__(self, question_text, choices, correct_choice):


        ##########  Initialise une question.    ##########

        self.question_text = question_text
        self.choices = choices
        self.correct_choice = correct_choice.lower()

    def is_correct(self, choice):
        ##########  Vérifie si une réponse est correcte.    ##########
        
        return choice.lower() == self.correct_choice
