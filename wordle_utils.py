def read_txt(filepath):

    data = []
    f = open(filepath, "r")

    for x in f:
        data.append(x.strip())

    return data


def list_top_wordle_words(wordle):

    i = 0

    # Sort by top words
    for word in wordle.top_wordle_words:

        i += 1
        if i == 1:
            print("Top eligible word list:")
        print("{}.) {}".format(i, word))


def wordle_solver(wordle):

    # Collect list of eligible words given good/bad letters
    eligible_correct_words = find_all_eligible_words(wordle)

    # Print list of top words
    find_all_top_words_from_eligible_list(wordle, eligible_correct_words)


def find_all_top_words_from_eligible_list(wordle, eligible_correct_words):

    top_eligible_correct_words_idx = []
    top_eligible_correct_words = []
    top_words_idx = 0
    all_eligible_idx = 0

    # Sort by top words, otherwise print alphabetically
    for word in wordle.top_wordle_words:
        top_words_idx += 1
        if word in eligible_correct_words:
            all_eligible_idx += 1
            top_eligible_correct_words.append(word)
            top_eligible_correct_words_idx.append(top_words_idx)

            if len(top_eligible_correct_words) == 1:
                print("Top eligible word list:")

            print("{}-{}.) {}".format(all_eligible_idx, top_words_idx, word))

    return



def find_all_eligible_words(wordle, show_all_eligible_words: bool=False):

    eligible_correct_words = []
    good_keys = list(wordle.good_letters_good_placement.keys())
    bad_keys = list(wordle.good_letters_bad_placement.keys())

    # Find all eligible words
    for word in wordle.wordle_words:

        contains_good_letters = check_for_any_good_letters(wordle=wordle, word=word)

        # Check good letters
        if contains_good_letters == True:

            eligible_bad_keys_correct, eligible_good_keys_correct = check_eligible_letters(
                wordle=wordle, bad_keys=bad_keys, good_keys=good_keys, word=word)

            # Check all bad keys are in word at least once
            all_bad_keys_at_least_once = check_all_keys_at_once(keys=bad_keys, word=word)

            # Check all good keys are in word at least once
            all_good_keys_at_least_once = check_all_keys_at_once(keys=good_keys, word=word)

            if eligible_bad_keys_correct >= len(bad_keys) and \
                    all_bad_keys_at_least_once == len(bad_keys) and \
                    eligible_good_keys_correct >= len(good_keys) and \
                    all_good_keys_at_least_once == len(good_keys):
                eligible_correct_words.append(word)

    if show_all_eligible_words:
        print("\nEligible word count:", len(eligible_correct_words))
        print("Eligible word list:\n", eligible_correct_words)

    return eligible_correct_words


def check_for_any_good_letters(wordle, word):

    contains_good_letters = True

    # Check bad letters
    for i in range(len(word)):
        if contains_good_letters == True:
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
