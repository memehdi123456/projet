import unittest
from mdp_tester import MdpTester
from mdp_generateur import MdpGenerateur

class TestMdpTools(unittest.TestCase):
    def test_entropy(self):
        self.assertAlmostEqual(MdpTester.calculate_entropy("abc"), 14.0, delta=1.0)

    def test_generate_password(self):
        password = MdpGenerateur.generate_password(2, 2, 2, 2)
        self.assertEqual(len(password), 8)

if __name__ == "__main__":
    unittest.main()
