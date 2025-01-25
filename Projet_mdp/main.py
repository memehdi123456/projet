########## ########## ##########  PROJET 2 ########## ########## ##########



from mdp_tester import PasswordTester
from mdp_generateur import PasswordGenerator
from phrase_generateur import PassphraseGenerator

if __name__ == "__main__":

    print("Gestion mdp")
    print("1. Tester un mot de passe")
    print("2. Générer un mot de passe")
    print("3. Générer une passphrase")

    choice = input("Choisissez une option (1/2/3) : ")

    if choice == "1":
        password = input("Entrez le mot de passe à tester : ")
        entropy = PasswordTester.calculate_entropy(password)
        strength = PasswordTester.assess_strength(entropy)
        print(f"Entropie : {entropy:.2f} bits, Force : {strength}")

    elif choice == "2":
        length = int(input("Longueur du mot de passe : "))
        lowercase = input("Inclure des minuscules ? (o/n) : ").lower() == 'o'
        uppercase = input("Inclure des majuscules ? (o/n) : ").lower() == 'o'
        digits = input("Inclure des chiffres ? (o/n) : ").lower() == 'o'
        special_chars = input("Inclure des caractères spéciaux ? (o/n) : ").lower() == 'o'

        password = PasswordGenerator.generate_password(length, lowercase, uppercase, digits, special_chars)
        print(f"Mot de passe généré : {password}")

    elif choice == "3":
        wordlist_file = "eff_large_wordlist.txt"
        wordlist = PassphraseGenerator.load_wordlist(wordlist_file)
        num_words = int(input("Nombre de mots dans la passphrase : "))
        passphrase = PassphraseGenerator.generate_passphrase(wordlist, num_words)
        print(f"Passphrase générée : {passphrase}")

    else:
        print("Option invalide.")
