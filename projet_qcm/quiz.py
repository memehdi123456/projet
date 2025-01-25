

########## ########## ##########  PROJET 1 ########## ########## ##########

from question import Question
import random

        ##########      Initialise le QCM.  ##########

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def shuffle_questions(self):
        random.shuffle(self.questions)

        ############    Pose les questions au participant.  ##########

    def start(self):
        print("Répondez aux questions en écrivant a, b ou c.\n")
        self.shuffle_questions()
        for index, question in enumerate(self.questions):
            print(f"Question {index + 1}: {question.question_text}")
            for i, choice in enumerate(question.choices):
                print(f"  {chr(97 + i)}) {choice}")

        ##########    Affiche le score et le corrigé.   ##########

            user_answer = input("Votre réponse (a, b, c) : ").lower()
            while user_answer not in ['a', 'b', 'c']:
                user_answer = input("Oups, réponse invalide. Réessayez (a, b, c) : ").lower()

            if question.is_correct(user_answer):
                print("Bravo, c'est correct !\n")
                self.score += 1
            else:
                correct_index = ord(question.correct_choice) - 97
                print(f"Dommage la bonne réponse était {question.correct_choice}) {question.choices[correct_index]}\n")

        print(f"Tu as obtenu {self.score} bonne(s) réponse(s) sur {len(self.questions)}.")
