########## ########## ##########  PROJET 2 ########## ########## ##########


import math

class PasswordTester:

######## Test force mdp ########

    @staticmethod
    def calculate_entropy(password):

        pool_size = 0


        if any(c.islower() for c in password):
            pool_size += 26
        if any(c.isupper() for c in password):
            pool_size += 26
        if any(c.isdigit() for c in password):
            poolsize += 10
        if any(c in '!@#$%^&*()-=+[]{}|;:'",.<>?/`~' for c in password):
            pool_size += 32


        entropy = len(password) * math.log2(pool_size) if pool_size > 0 else 0
        return entropy

    @staticmethod
    def assess_strength(entropy):

        if entropy < 28:
            return "Très faible"
        elif entropy < 36:
            return "Faible"
        elif entropy < 60:
            return "Moyenne"
        elif entropy < 128:
            return "Forte"
        else:
            return "Très forte"
