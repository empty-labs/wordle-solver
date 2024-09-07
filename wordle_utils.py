def wordle_solver(wordle):

    eligible_correct_words = []
    good_keys = list(wordle.good_letters_good_placement.keys())
    bad_keys = list(wordle.good_letters_bad_placement.keys())

    for w in wordle.wordle_words:

        contains_good_letters = True

        # Check bad letters
        for i in range(len(w)):
            if contains_good_letters == True:
                if w[i] in wordle.bad_letters:
                    contains_good_letters = False

        # Check good letters
        if contains_good_letters == True:

            eligible_bad_keys_correct = 0
            eligible_good_keys_correct = 0

            for i in range(len(w)):

                # Check that word uses key letters and not in bad placement
                if w[i] in bad_keys:
                    if i not in wordle.good_letters_bad_placement[w[i]]:
                        eligible_bad_keys_correct += 1

                # Check that word uses key letters and in good placement
                if w[i] in good_keys:
                    if i in wordle.good_letters_good_placement[w[i]]:
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
