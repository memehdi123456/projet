

########## ########## ##########  PROJET 1 ########## ########## ##########

import random
from question import Question

class Quiz:
    def __init__(self, questions):

        ##########      Initialise le QCM.  ##########


        self.questions = questions
        random.shuffle(self.questions)
        self.score = 0
        self.user_answers = []

    def ask_questions(self):

        ############    Pose les questions au participant.  ##########

        for index, question in enumerate(self.questions):
            print(f"Question {index + 1}: {question.text}")
            for i, choice in enumerate(question.choices):
                print(f"  {chr(97 + i)}) {choice}")

            user_answer = input("Votre réponse (a, b, c) : ").lower()
            while user_answer not in ['a', 'b', 'c']:
                user_answer = input("Réponse invalide. Essayez à nouveau (a, b, c) : ").lower()

            answer_index = ord(user_answer) - ord('a')
            self.user_answers.append(answer_index)
            if question.is_correct(answer_index):
                self.score += 1

    def show_results(self):

        ##########    Affiche le score et le corrigé.   ##########

        print("\n--- Résultats ---")
        print(f"Votre score : {self.score}/{len(self.questions)}")
        print("\n--- Corrigé ---")
        for index, question in enumerate(self.questions):
            correct_letter = chr(97 + question.correct_choice)
            print(f"Question {index + 1}: {question.text}")
            print(f"  Correct : {correct_letter}) {question.choices[question.correct_choice]}")
            user_letter = chr(97 + self.user_answers[index])
            result = "✅" if question.is_correct(self.user_answers[index]) else "❌"
            print(f"  Votre réponse : {user_letter}) {question.choices[self.user_answers[index]]} {result}\n")
