# hangman_test.py

import unittest
import string
from hangman import is_word_guessed, get_guessed_word, get_available_letters, match_with_gaps, show_possible_matches, get_score

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
    
    def test_match_with_gaps(self):
        self.assertFalse(match_with_gaps("t__t", "tacts"))
        self.assertFalse(match_with_gaps("a____", "below"))
        self.assertTrue(match_with_gaps("apple", "apple"))
        self.assertTrue(match_with_gaps("a__le", "apple"))
        self.assertFalse(match_with_gaps("a_ple", "apple"))
    
    def test_show_possible_matches(self):
        self.assertListEqual(show_possible_matches("t__t"), "tact tart taut teat tent test text that tilt tint toot tort tout trot tuft twit".split())
        self.assertListEqual(show_possible_matches("abbbb_"), [])
        self.assertListEqual(show_possible_matches("a_pl_"), ["ample", "amply"])
    
    def test_get_score(self):
        self.assertEqual(get_score("apple", 2), 8)

if __name__=="__main__":
    unittest.main()