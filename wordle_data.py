import wordle_utils as wu

# Constants
# https://github.com/dwyl/english-words/blob/master/words_alpha.txt
WORDS_FILEPATH = r"/Users/derekfromtexas/Downloads/words_alpha.txt"

# https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/English/Wikipedia_(2016)#1-1000
TOP_WORDS_FILEPATH_1 = r"/Users/derekfromtexas/Downloads/frequent_words_1-1000.txt"
TOP_WORDS_FILEPATH_2 = r"/Users/derekfromtexas/Downloads/frequent_words_1001-2000.txt"
TOP_WORDS_FILEPATH_3 = r"/Users/derekfromtexas/Downloads/frequent_words_2001-3000.txt"
TOP_WORDS_FILEPATH_4 = r"/Users/derekfromtexas/Downloads/frequent_words_3001-4000.txt"
TOP_WORDS_FILEPATH_5 = r"/Users/derekfromtexas/Downloads/frequent_words_4001-5000.txt"
TOP_WORDS_FILEPATH_6 = r"/Users/derekfromtexas/Downloads/frequent_words_5001-6000.txt"
TOP_WORDS_FILEPATH_7 = r"/Users/derekfromtexas/Downloads/frequent_words_6001-7000.txt"
TOP_WORDS_FILEPATH_8 = r"/Users/derekfromtexas/Downloads/frequent_words_7001-8000.txt"
TOP_WORDS_FILEPATH_9 = r"/Users/derekfromtexas/Downloads/frequent_words_8001-9000.txt"
TOP_WORDS_FILEPATH_10 = r"/Users/derekfromtexas/Downloads/frequent_words_9001-10000.txt"
TOP_WORDS_FILEPATH_11 = r"/Users/derekfromtexas/Downloads/frequent_words_10001-20000.txt"


class Wordle:

    def __init__(self):

        data = []
        f = open(WORDS_FILEPATH, "r")
        for x in f:
            data.append(x.strip())

        top_words = wu.read_top_words(filepath=TOP_WORDS_FILEPATH_1)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_2)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_3)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_4)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_5)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_6)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_7)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_8)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_9)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_10)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_11)

        print("Number of top words", len(top_words))

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
        print("Number of top Wordle words", len(self.top_wordle_words))
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

