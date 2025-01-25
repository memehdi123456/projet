########## ########## ##########  PROJET 2 ########## ########## ##########

import random
import string

class PasswordGenerator:
########### generation de mdp par rapport aux exigence de l'utilisateur ###########

    @staticmethod
    def generate_password(length, lowercase, uppercase, digits, special_chars):
        char_pool = (
            (string.ascii_lowercase if lowercase else "") +
            (string.ascii_uppercase if uppercase else "") +
            (string.digits if digits else "") +
            ("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" if special_chars else "")
        )
        if not char_pool:
            raise ValueError("Au moins une catégorie de caractères doit être sélectionnée.")

        return ''.join(random.choice(char_pool) for _ in range(length))
