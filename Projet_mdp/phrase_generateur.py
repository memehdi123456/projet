########## ########## ##########  PROJET 2 ########## ########## ##########


import random

class PassphraseGenerator:
######## generation passphrase depuis fichier eff wordlist #########

    @staticmethod
    def load_wordlist(filepath):
        wordlist = {}
        with open(filepath, 'r') as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    wordlist[parts[0]] = parts[1]
        return wordlist

    @staticmethod
    def generate_passphrase(wordlist, num_words):
        dice_rolls = list(wordlist.keys())
        return ' '.join(wordlist[random.choice(dice_rolls)] for _ in range(num_words))
