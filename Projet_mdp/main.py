from mdp_tester import MdpTester
from mdp_generateur import MdpGenerateur
from phrase_generateur import PhraseGenerateur

def main():
    print("Bienvenue dans l'outil de gestion de mots de passe.")

    # Tester la force d'un mot de passe
    password = input("Entrez un mot de passe à tester : ")
    entropy = MdpTester.calculate_entropy(password)
    rating = MdpTester.rate_password(entropy)
    print(f"Entropie : {entropy:.2f} bits, Force : {rating}")

    # Générer un mot de passe
    print("\nGénération d'un mot de passe aléatoire.")
    lowercase = int(input("Nombre de minuscules : "))
    uppercase = int(input("Nombre de majuscules : "))
    digits = int(input("Nombre de chiffres : "))
    special = int(input("Nombre de caractères spéciaux : "))
    password = MdpGenerateur.generate_password(lowercase, uppercase, digits, special)
    print(f"Mot de passe généré : {password}")

    # Générer une passphrase
    print("\nGénération d'une passphrase.")
    word_list = ["soleil", "arbre", "étoile", "mer", "lune", "montagne"]  # Exemple de liste
    passphrase = PhraseGenerateur.generate_passphrase(word_list)
    print(f"Passphrase générée : {passphrase}")

if __name__ == "__main__":
    main()
