########## ########## ##########  PROJET 1 ########## ########## ##########
from question import Question
from quiz import Quiz
    ###########  Liste de questions  ##########
def main():

        quiz = Quiz()

        quiz.add_question(Question("Qui a fondé Apple ?", ["Steve Jobs", "Bill Gates", "Elon Musk"], "a"))
        quiz.add_question(Question("Quelle année a été lancée la première iPhone ?", ["2005", "2007", "2010"], "b"))
        quiz.add_question(Question("Quel est le nom du système d'exploitation mobile d'Apple ?", ["Android", "iOS", "Windows Mobile"], "b"))
        quiz.add_question(Question("Quel est le produit phare d'Apple ?", ["iPhone", "Macbook", "iPad"], "a"))
        quiz.add_question(Question("Quel est le service de streaming vidéo d'Apple ?", ["Apple Music", "Apple TV+", "iTunes"], "b"))
        quiz.add_question(Question("Quelle est la couleur de la première Apple logo ?", ["Vert", "Arc-en-ciel", "Noir"], "b"))
        quiz.add_question(Question("Quel est le nom de l'assistant vocal d'Apple ?", ["Siri", "Cortana", "Alexa"], "a"))
        quiz.add_question(Question("En quelle année Steve Jobs a-t-il quitté Apple pour créer NeXT ?", ["1976", "1985", "1993"], "b"))
        quiz.add_question(Question("Quel est le produit de réalité virtuelle ou augmentée d'Apple ?", ["Apple VR", "Apple AR", "Vision Pro"], "c"))
        quiz.add_question(Question("Combien de temps a duré la keynote de présentation de l'iPhone original ?", ["1h", "2h", "3h"], "a"))

    ###########  Lancement du quiz  ##########
        quiz.start()

if __name__ == "__main__":
    main()
