import math
import string

class MdpTester:
    @staticmethod
    def calculate_entropy(password):
        """
        Calcule l'entropie du mot de passe.
        """
        charset_size = 0
        if any(c.islower() for c in password):
            charset_size += len(string.ascii_lowercase)
        if any(c.isupper() for c in password):
            charset_size += len(string.ascii_uppercase)
        if any(c.isdigit() for c in password):
            charset_size += len(string.digits)
        if any(c in string.punctuation for c in password):
            charset_size += len(string.punctuation)

        entropy = len(password) * math.log2(charset_size)
        return entropy

    @staticmethod
    def rate_password(entropy):
        """
        Retourne une note en fonction de l'entropie.
        """
        if entropy < 28:
            return "Faible"
        elif entropy < 36:
            return "Moyen"
        elif entropy < 60:
            return "Fort"
        else:
            return "Très fort"
