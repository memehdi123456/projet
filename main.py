from quiz import Quiz
from question import Question

if __name__ == "__main__":
    # Liste de questions
    questions = [
        Question("Quelle est la capitale de la France ?", ["Paris", "Londres", "Berlin"], 0),
        Question("Combien font 2 + 2 ?", ["3", "4", "5"], 1),
        Question("Quelle est la couleur du ciel ?", ["Rouge", "Bleu", "Vert"], 1),
        # Ajoutez plus de questions ici
    ]

    # Initialiser et exécuter le QCM
    quiz = Quiz(questions)
    quiz.ask_questions()
    quiz.show_results()
