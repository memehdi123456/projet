

########## ########## ##########  PROJET 1 ########## ########## ##########


from quiz import Quiz
from question import Question

def main():
    ###########  Liste de questions  ##########
    questions = [
        Question("Qui a fondé Apple ?", ["Steve Jobs", "Bill Gates", "Elon Musk"], 0),
        Question("Quelle année a été lancée la première iPhone ?", ["2005", "2007", "2010"], 1),
        Question("Quel est le nom du système d'exploitation mobile d'Apple ?", ["Android", "iOS", "Windows Mobile"], 1),
        Question("Quel est le produit phare d'Apple ?", ["iPhone", "Macbook", "iPad"], 0),
        Question("Quel est le service de streaming vidéo d'Apple ?", ["Apple Music", "Apple TV+", "iTunes"], 1),
        Question("Quelle est la couleur de la première Apple logo ?", ["Vert", "Arc-en-ciel", "Noir"], 1),
        Question("Quel est le nom de l'assistant vocal d'Apple ?", ["Siri", "Cortana", "Alexa"], 0),
        Question("En quelle année Steve Jobs a-t-il quitté Apple pour créer NeXT ?", ["1976", "1985", "1993"], 1),
        Question("Quel est le produit de réalité virtuelle ou augmentée d'Apple ?", ["Apple VR", "Apple AR", "Vision Pro"], 2),
        Question("Combien de temps a duré la keynote de présentation de l'iPhone original ?", ["1h", "2h", "3h"], 0)
    ]

    ###########  Initialiser et exécuter le QCM     ##########
    quiz = Quiz(questions)
    quiz.ask_questions()
    quiz.show_results()

if __name__ == "__main__":
    main()
