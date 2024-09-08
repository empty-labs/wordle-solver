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
TOP_WORDS_FILEPATH_12 = r"/Users/derekfromtexas/Downloads/frequent_words_20001-30000.txt"
TOP_WORDS_FILEPATH_13 = r"/Users/derekfromtexas/Downloads/frequent_words_30001-40000.txt"
TOP_WORDS_FILEPATH_14 = r"/Users/derekfromtexas/Downloads/frequent_words_40001-50000.txt"
TOP_WORDS_FILEPATH_15 = r"/Users/derekfromtexas/Downloads/frequent_words_50001-60000.txt"
TOP_WORDS_FILEPATH_16 = r"/Users/derekfromtexas/Downloads/frequent_words_60001-70000.txt"
TOP_WORDS_FILEPATH_17 = r"/Users/derekfromtexas/Downloads/frequent_words_70001-80000.txt"
TOP_WORDS_FILEPATH_18 = r"/Users/derekfromtexas/Downloads/frequent_words_80001-90000.txt"
TOP_WORDS_FILEPATH_19 = r"/Users/derekfromtexas/Downloads/frequent_words_90001-100000.txt"
TOP_WORDS_FILEPATH_20 = r"/Users/derekfromtexas/Downloads/frequent_words_100001-110000.txt"
TOP_WORDS_FILEPATH_21 = r"/Users/derekfromtexas/Downloads/frequent_words_110001-120000.txt"
TOP_WORDS_FILEPATH_22 = r"/Users/derekfromtexas/Downloads/frequent_words_120001-130000.txt"
TOP_WORDS_FILEPATH_23 = r"/Users/derekfromtexas/Downloads/frequent_words_130001-140000.txt"
TOP_WORDS_FILEPATH_24 = r"/Users/derekfromtexas/Downloads/frequent_words_140001-150000.txt"
TOP_WORDS_FILEPATH_25 = r"/Users/derekfromtexas/Downloads/frequent_words_150001-157000.txt"


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
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_12)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_13)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_14)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_15)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_16)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_17)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_18)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_19)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_20)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_21)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_22)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_23)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_24)
        top_words = top_words + wu.read_top_words(filepath=TOP_WORDS_FILEPATH_25)

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

        with open('wordle_words.txt', 'a') as f:
            for w in self.wordle_words:
                f.write(w + '\n')

        with open('frequent_wordle_words.txt', 'a') as f:
            for w in self.top_wordle_words:
                f.write(w + '\n')

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

