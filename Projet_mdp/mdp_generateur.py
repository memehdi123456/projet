import random
import string

class MdpGenerateur:
    @staticmethod
    def generate_password(lowercase, uppercase, digits, special):
        """
        Génère un mot de passe avec les critères spécifiés.
        """
        if sum([lowercase, uppercase, digits, special]) == 0:
            raise ValueError("Au moins un caractère doit être choisi.")

        password = []
        password += random.choices(string.ascii_lowercase, k=lowercase)
        password += random.choices(string.ascii_uppercase, k=uppercase)
        password += random.choices(string.digits, k=digits)
        password += random.choices(string.punctuation, k=special)

        random.shuffle(password)
        return ''.join(password)
