

########## ########## ##########  PROJET 1 ########## ########## ##########


class Question:
    def __init__(self, text, choices, correct_choice):

        ##########  Initialise une question.    ##########

        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

    def is_correct(self, answer):

        ##########  Vérifie si une réponse est correcte.    ##########

        return answer == self.correct_choice
