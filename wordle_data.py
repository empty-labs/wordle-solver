# Constants
WORDS_FILEPATH = r"/Users/derekfromtexas/Downloads/words_alpha.txt"


class Wordle:

    def __init__(self):

        data = []
        f = open(WORDS_FILEPATH, "r")
        for x in f:
            data.append(x.strip())

        # Baseline
        self.data = data
        self.words = []
        self.wordle_words = []
        self.guess_words = []
        self.good_letters_good_placement = {}
        self.good_letters_bad_placement = {}
        self.bad_letters = []

    def set_data(self):

        self.words = list(self.data)

        wordle_words = []

        for w in self.words:
            if type(w) is not float:  # avoid nan being considered a float with no length
                if len(w) == 5 and \
                        '-' not in w and \
                        ' ' not in w:
                    wordle_words.append(w)

        self.wordle_words = list(set(wordle_words))
        self.wordle_words.sort()
        print("Number of eligible Wordle words:",len(self.wordle_words))

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

    def wordle_solver(self):

        eligible_correct_words = []
        good_keys = list(self.good_letters_good_placement.keys())
        bad_keys = list(self.good_letters_bad_placement.keys())

        for w in self.wordle_words:

            contains_good_letters = True

            # Check bad letters
            for i in range(len(w)):
                if contains_good_letters == True:
                    if w[i] in self.bad_letters:
                        contains_good_letters = False

            # Check good letters
            if contains_good_letters == True:

                eligible_bad_keys_correct = 0
                eligible_good_keys_correct = 0

                for i in range(len(w)):

                    # Check that word uses key letters and not in bad placement
                    if w[i] in bad_keys:
                        if i not in self.good_letters_bad_placement[w[i]]:
                            eligible_bad_keys_correct += 1

                    # Check that word uses key letters and in good placement
                    if w[i] in good_keys:
                        if i in self.good_letters_good_placement[w[i]]:
                            eligible_good_keys_correct += 1

                # Check all bad keys are in word at least once
                all_bad_keys_at_least_once = 0
                for k in bad_keys:
                    if k in w:
                        all_bad_keys_at_least_once += 1

                # Check all good keys are in word at least once
                all_good_keys_at_least_once = 0
                for k in good_keys:
                    if k in w:
                        all_good_keys_at_least_once += 1

                if eligible_bad_keys_correct >= len(bad_keys) and \
                        all_bad_keys_at_least_once == len(bad_keys) and \
                        eligible_good_keys_correct >= len(good_keys) and \
                        all_good_keys_at_least_once == len(good_keys):
                    eligible_correct_words.append(w)

        print("\nEligible word count:", len(eligible_correct_words))
        print("Eligible word list:\n", eligible_correct_words)

