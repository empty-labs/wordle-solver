import wordle_utils as wu

# Constants
# https://github.com/dwyl/english-words/blob/master/words_alpha.txt
WORDS_FILEPATH = r"/Users/derekfromtexas/Downloads/words_alpha.txt"

# https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/English/Wikipedia_(2016)#1-1000
TOP_WORDS_FILEPATH = r"/Users/derekfromtexas/Downloads/frequent_words_1-1000.txt"


class Wordle:

    def __init__(self):

        data = []
        f = open(WORDS_FILEPATH, "r")
        for x in f:
            data.append(x.strip())

        top_words = []
        fq = open(TOP_WORDS_FILEPATH, "r")
        for x in fq:
            words = x.strip().split(' ')
            for word in words:
                top_words.append(word)

        top_words = list(set(top_words))

        # Baseline
        self.data = data
        self.top_words = top_words

        self.words = []
        self.wordle_words = []
        self.top_wordle_words = []
        self.guess_words = []
        self.good_letters_good_placement = {}
        self.good_letters_bad_placement = {}
        self.bad_letters = []

    def set_data(self):

        self.words = list(self.data)
        self.wordle_words = wu.limit_to_five_letters(word_list=self.words)
        self.top_wordle_words = wu.limit_to_five_letters(word_list=self.top_words)
        self.wordle_words.sort()
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
                else:
                    self.good_letters_good_placement[good_letters[i]] = []
                    self.good_letters_good_placement[good_letters[i]].append(good_letters_good_placement[i])

        for i in range(len(good_letters_bad_placement)):

            # Bad placement
            if good_letters_bad_placement[i] is not None:
                if good_letters[i] in list(self.good_letters_bad_placement.keys()):
                    self.good_letters_bad_placement[good_letters[i]].append(good_letters_bad_placement[i])
                else:
                    self.good_letters_bad_placement[good_letters[i]] = []
                    self.good_letters_bad_placement[good_letters[i]].append(good_letters_bad_placement[i])

        # Find bad letters
        for a in guess_word:
            if a not in good_letters:
                self.bad_letters.append(a)

        self.bad_letters = list(set(self.bad_letters))

        print('Good placement dictionary', self.good_letters_good_placement)
        print('Bad placement dictionary', self.good_letters_bad_placement)
        print('Bad letters', self.bad_letters)

