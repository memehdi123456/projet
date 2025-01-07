

########## ########## ##########  PROJET 1 ########## ########## ########## 


from quiz import Quiz
from question import Question

def main():
    ###########  Liste de questions  ##########
    questions = [
        Question("Qui a écrit *Le Petit Prince* ?", ["Jules Verne", "Antoine de Saint-Exupéry", "Victor Hugo"], 1),
        Question("Dans quel pays se trouve la pyramide de Gizeh ?", ["Égypte", "Mexique", "Grèce"], 0),
        Question("Quel est le plus grand mammifère ?", ["Éléphant", "Baleine bleue", "Girafe"], 1),
        Question("Quelle est la plus petite planète de notre système solaire ?", ["Mercure", "Mars", "Pluton"], 0),
        Question("Quelle est la formule chimique de l'eau ?", ["CO2", "O2", "H2O"], 2),
        Question("Quelle est la langue la plus parlée dans le monde ?", ["Anglais", "Mandarin", "Espagnol"], 1),
        Question("Combien de côtés possède un octogone ?", ["6", "10", "8"], 2),
        Question("Combien font 7×8 ?", ["56", "64", "48"], 0),
        Question("Quel est le plus grand océan du monde ?", ["Atlantique", "Pacifique", "Indien"], 1),
        Question("Qui a peint La Joconde ?", ["Léonard de Vinci", "Michel-Ange", "Raphael"], 0),
    ]

    ###########  Initialiser et exécuter le QCM     ##########
    quiz = Quiz(questions)
    quiz.ask_questions()
    quiz.show_results()

if __name__ == "__main__":
    main()
