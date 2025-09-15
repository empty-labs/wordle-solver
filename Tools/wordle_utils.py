def read_txt(filepath):
    """Read text files for word options"""
    data = []
    f = open(filepath, "r")

    for x in f:
        data.append(x.strip())

    return data


def list_top_wordle_words(wordle, show_words: bool=False):
    """Show top words from Wiki list"""
    if show_words:
        print("Top eligible word list:")
        # Sort by top words
        for i, w in enumerate(wordle.top_wordle_words):
            print("{}.) {}".format(i+1, w))


def wordle_solver(wordle, show_eligible_words_unsorted: bool=False):
    """Solve wordle with eligible word choices"""

    eligible_correct_words = []
    good_keys = list(wordle.good_letters_good_placement.keys())
    bad_keys = list(wordle.good_letters_bad_placement.keys())

    # Find eligible words
    for w in wordle.wordle_words:

        contains_good_letters = check_for_any_good_letters(wordle=wordle, word=w)

        # Check good letters
        if contains_good_letters:

            eligible_bad_keys_correct, eligible_good_keys_correct = check_eligible_letters(
                wordle=wordle, bad_keys=bad_keys, good_keys=good_keys, word=w)

            # Check all bad keys are in word at least once
            all_bad_keys_at_least_once = check_all_keys_at_once(keys=bad_keys, word=w)

            # Check all good keys are in word at least once
            all_good_keys_at_least_once = check_all_keys_at_once(keys=good_keys, word=w)

            if eligible_bad_keys_correct >= len(bad_keys) and \
                    all_bad_keys_at_least_once == len(bad_keys) and \
                    eligible_good_keys_correct >= len(good_keys) and \
                    all_good_keys_at_least_once == len(good_keys):
                eligible_correct_words.append(w)

    if show_eligible_words_unsorted:
        print("\nEligible word count:", len(eligible_correct_words))
        print("Eligible word list:\n", eligible_correct_words)

    top_eligible_correct_words = []
    j = 0

    # Sort by top words, otherwise print alphabetically
    for i, w in enumerate(wordle.top_wordle_words):
        if w in eligible_correct_words:

            top_eligible_correct_words.append(w)
            n = len(top_eligible_correct_words)
            if n == 1:
                print("Top eligible word list:")

            print("{}-{}.) {}".format(n, i+1, w))

            if n == 25:
                break  # Stop sharing after top 25 words


def check_for_any_good_letters(wordle, word):

    contains_good_letters = True

    # Check bad letters
    for i in range(len(word)):
        if contains_good_letters:
            if word[i] in wordle.bad_letters:
                contains_good_letters = False

    return contains_good_letters


def check_eligible_letters(wordle, bad_keys, good_keys, word):

    eligible_bad_keys_correct = 0
    eligible_good_keys_correct = 0

    for i in range(len(word)):

        # Check that word uses key letters and not in bad placement
        if word[i] in bad_keys:
            if i not in wordle.good_letters_bad_placement[word[i]]:
                eligible_bad_keys_correct += 1

        # Check that word uses key letters and in good placement
        if word[i] in good_keys:
            if i in wordle.good_letters_good_placement[word[i]]:
                eligible_good_keys_correct += 1

    return eligible_bad_keys_correct, eligible_good_keys_correct


def check_all_keys_at_once(keys, word):

    all_keys_at_least_once = 0

    for k in keys:
        if k in word:
            all_keys_at_least_once += 1

    return all_keys_at_least_once
