import unittest
from logic.helper_functions import make_no_round_brackets
from logic.helper_functions import make_no_square_brackets
from logic.helper_functions import make_no_curly_brackets
from logic.helper_functions import make_no_brackets

class MyTestCase(unittest.TestCase):
    def test_round_brackets_removal(self):
        self.assertEqual("Pioter", make_no_round_brackets("(Pioter)"))

    def test_round_brackets_removal_at_multiple_words(self):
        self.assertEqual("Pioter, Helikopter, hamburger",
                         make_no_round_brackets(
                             "(((Pioter), ((Helikopter))), (hamburger))"))
    def test_only_round_brackets_removal(self):
        self.assertEqual("[[Pioter], Helikopter], hamburger",
                         make_no_round_brackets(
                             "((([[Pioter]), ((Helikopter]))), (hamburger))"))
    def test_square_brackets_removal(self):
        self.assertEqual("Pioter", make_no_square_brackets("[Pioter]"))

    def test_square_brackets_removal_at_multiple_words(self):
        self.assertEqual("Pioter, Helikopter, hamburger",
                         make_no_square_brackets(
                             "[[[Pioter], [[Helikopter]]], [hamburger]]"))

    def test_only_square_brackets_removal(self):
        self.assertEqual("(((Pioter), ((Helikopter))), (hamburger))",
                         make_no_square_brackets(
                             "((([[Pioter]), ((Helikopter]))), (hamburger))"))

    def test_curly_brackets_removal(self):
        self.assertEqual("Pioter", make_no_curly_brackets("{Pioter}"))

    def test_curly_brackets_removal_at_multiple_words(self):
        self.assertEqual("Pioter, Helikopter, hamburger",
                         make_no_curly_brackets(
                             "{{{Pioter}, {{Helikopter}}}, {hamburger}}"))

    def test_only_curly_brackets_removal(self):
        self.assertEqual("((([[Pioter]), ((Helikopter]))), (hamburger))",
                         make_no_curly_brackets(
                             "((([[{Pioter}]), (({Helikopter]))), ({hamburger}}))"))
    def test_all_brackets_removal(self):
        self.assertEqual("Pioter, Helikopter, hamburger",
                         make_no_brackets("((([[{Pioter}]), (({Helikopter]))), ({hamburger}}))"))

if __name__ == '__main__':
    unittest.main()
