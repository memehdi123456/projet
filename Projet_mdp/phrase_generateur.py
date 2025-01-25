import random

class PhraseGenerateur:
    @staticmethod
    def generate_passphrase(word_list, num_words=4):
        """
        Génère une passphrase à partir d'une liste de mots et du nombre souhaité.
        """
        if not word_list:
            raise ValueError("La liste de mots ne doit pas être vide.")

        return ' '.join(random.choices(word_list, k=num_words))
