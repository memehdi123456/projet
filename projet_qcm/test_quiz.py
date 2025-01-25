

########## ########## ##########  PROJET 1 ########## ########## ##########

##########  initialisation test unitaire ##########
import unittest
from question import Question

class TestQuestion(unittest.TestCase):
    def test_is_correct(self):
        question = Question("Qui a fondé Apple ?", ["Steve Jobs", "Bill Gates", "Elon Musk"], "a")
        self.assertTrue(question.is_correct("a"))
        self.assertFalse(question.is_correct("b"))

if __name__ == "__main__":
    unittest.main()
