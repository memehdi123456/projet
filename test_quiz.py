

########## ########## ##########  PROJET 1 ########## ########## ########## 

##########  initialisation test unitaire ##########
import unittest
from question import Question

class TestQuestion(unittest.TestCase):
    def test_is_correct(self):
        q = Question("Test", ["a", "b", "c"], 1)
        self.assertTrue(q.is_correct(1))
        self.assertFalse(q.is_correct(0))
        self.assertFalse(q.is_correct(2))

if __name__ == "__main__":
    unittest.main()
