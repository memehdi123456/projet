class Question:
    def __init__(self, text, choices, correct_choice):
        """
        Initialise une question.
        :param text: Texte de la question.
        :param choices: Liste des réponses possibles.
        :param correct_choice: Indice (0, 1, ou 2) de la bonne réponse.
        """
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

    def is_correct(self, answer):
        """
        Vérifie si une réponse est correcte.
        :param answer: Indice de la réponse (0, 1 ou 2).
        :return: True si correct, sinon False.
        """
        return answer == self.correct_choice
