# hangman_test.py

import unittest
import string
from hangman import is_word_guessed, get_guessed_word, get_available_letters

class TestHangman(unittest.TestCase):

    def test_is_word_guessed(self):
        self.assertTrue(is_word_guessed("apple", ["a", "e", "l", "p", "m"]))
        self.assertFalse(is_word_guessed("apple", ["a", "e", "l"]))
        self.assertFalse(is_word_guessed("apple", []))
    
    def test_get_guessed_word(self):
        self.assertEqual(get_guessed_word("apple", ["a", "e"]), "a___e")
        self.assertEqual(get_guessed_word("apple", []), "_____")
        self.assertEqual(get_guessed_word("apple", ["m", "n", "l"]), "___l_")
        self.assertEqual(get_guessed_word("apple", ["a", "p", "l", "e"]), "apple")
    
    # Test get_available_letters
    def test_get_available_letters(self):
        self.assertEqual(get_available_letters([]), string.ascii_lowercase)
        self.assertEqual(get_available_letters(['a','d']), 'bcefghijklmnopqrstuvwxyz')

if __name__=="__main__":
    unittest.main()