import unittest
from mdp_tester import PasswordTester
from mdp_generateur import PasswordGenerator
from phrase_generateur import PassphraseGenerator

class TestPasswordTester(unittest.TestCase):
    def test_entropy_calculation(self):

        self.assertAlmostEqual(PasswordTester.calculate_entropy("abc"), 14.08, places=2)
        self.assertAlmostEqual(PasswordTester.calculate_entropy("ABC123!"), 41.31, places=2)

    def test_assess_strength(self):

        self.assertEqual(PasswordTester.assess_strength(10), "Très faible")
        self.assertEqual(PasswordTester.assess_strength(50), "Moyenne")

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password(self):

        password = PasswordGenerator.generate_password(10, True, True, True, True)
        self.assertEqual(len(password), 10)
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))

class TestPassphraseGenerator(unittest.TestCase):
    def test_generate_passphrase(self):

        wordlist = {"11111": "abacus", "11112": "abdomen"}
        passphrase = PassphraseGenerator.generate_passphrase(wordlist, 2)
        self.assertEqual(len(passphrase.split()), 2)

if __name__ == "__main__":
    unittest.main()
