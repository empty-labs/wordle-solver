# Local libraries
from Tools import wordle_utils as wu

# Constants
# https://github.com/dwyl/english-words/blob/master/words_alpha.txt
WORDS_FILEPATH = r"Data/Active/wordle_words.txt"

# https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/English/Wikipedia_(2016)#1-157000
TOP_WORDS_FILEPATH = r"Data/Active/frequent_wordle_words.txt"


class Wordle:

    def __init__(self):

        self.wordle_words = []
        self.top_wordle_words = []
        self.guess_words = []
        self.good_letters_good_placement = {}
        self.good_letters_bad_placement = {}
        self.bad_letters = []

    def set_data(self):

        self.wordle_words = wu.read_txt(filepath=WORDS_FILEPATH)
        self.top_wordle_words = wu.read_txt(filepath=TOP_WORDS_FILEPATH)    # Ordered by most used

        print("Number of top Wordle words", len(self.top_wordle_words))
        print("Number of eligible Wordle words:", len(self.wordle_words))

    def wordle_guess(self, guess_word: str, good_letters: list = [], good_letters_bad_placement: list = [],
                     good_letters_good_placement: list = []):
        """
        placement is 0-based indexing
        """

        self.guess_words.append(guess_word)
        print('\nGuess:', guess_word)

        # Assign good letters to dictionaries
        for i in range(len(good_letters_good_placement)):

            # Good placement
            if good_letters_good_placement[i] is not None:
                if good_letters[i] in list(self.good_letters_good_placement.keys()):
                    self.good_letters_good_placement[good_letters[i]].append(good_letters_good_placement[i])
                    # Trim to unique letters only
                    self.good_letters_good_placement[good_letters[i]] = list(set(self.good_letters_good_placement[good_letters[i]]))
                else:
                    self.good_letters_good_placement[good_letters[i]] = []
                    self.good_letters_good_placement[good_letters[i]].append(good_letters_good_placement[i])

        for i in range(len(good_letters_bad_placement)):

            # Bad placement
            if good_letters_bad_placement[i] is not None:
                if good_letters[i] in list(self.good_letters_bad_placement.keys()):
                    self.good_letters_bad_placement[good_letters[i]].append(good_letters_bad_placement[i])
                    # Trim to unique letters only
                    self.good_letters_bad_placement[good_letters[i]] = list(set(self.good_letters_bad_placement[good_letters[i]]))
                else:
                    self.good_letters_bad_placement[good_letters[i]] = []
                    self.good_letters_bad_placement[good_letters[i]].append(good_letters_bad_placement[i])

        # Find bad letters
        for a in guess_word:
            if a not in good_letters:
                self.bad_letters.append(a)

        self.bad_letters = list(set(self.bad_letters))

        print('Good placement dictionary:', self.good_letters_good_placement)
        print('Bad placement dictionary:', self.good_letters_bad_placement)
        print('Bad letters:', self.bad_letters)
