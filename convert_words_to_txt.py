# Third party libraries
import os

# Local module
import wordle_utils as wu

# Constants
# https://github.com/dwyl/english-words/blob/master/words_alpha.txt
WORDS_FILEPATH = r"source_data/words_alpha.txt"

# https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/English/Wikipedia_(2016)#1-1000
TOP_WORDS_FILEPATH_1 = r"source_data/frequent_words_1-1000.txt"
TOP_WORDS_FILEPATH_2 = r"source_data/frequent_words_1001-2000.txt"
TOP_WORDS_FILEPATH_3 = r"source_data/frequent_words_2001-3000.txt"
TOP_WORDS_FILEPATH_4 = r"source_data/frequent_words_3001-4000.txt"
TOP_WORDS_FILEPATH_5 = r"source_data/frequent_words_4001-5000.txt"
TOP_WORDS_FILEPATH_6 = r"source_data/frequent_words_5001-6000.txt"
TOP_WORDS_FILEPATH_7 = r"source_data/frequent_words_6001-7000.txt"
TOP_WORDS_FILEPATH_8 = r"source_data/frequent_words_7001-8000.txt"
TOP_WORDS_FILEPATH_9 = r"source_data/frequent_words_8001-9000.txt"
TOP_WORDS_FILEPATH_10 = r"source_data/frequent_words_9001-10000.txt"
TOP_WORDS_FILEPATH_11 = r"source_data/frequent_words_10001-20000.txt"
TOP_WORDS_FILEPATH_12 = r"source_data/frequent_words_20001-30000.txt"
TOP_WORDS_FILEPATH_13 = r"source_data/frequent_words_30001-40000.txt"
TOP_WORDS_FILEPATH_14 = r"source_data/frequent_words_40001-50000.txt"
TOP_WORDS_FILEPATH_15 = r"source_data/frequent_words_50001-60000.txt"
TOP_WORDS_FILEPATH_16 = r"source_data/frequent_words_60001-70000.txt"
TOP_WORDS_FILEPATH_17 = r"source_data/frequent_words_70001-80000.txt"
TOP_WORDS_FILEPATH_18 = r"source_data/frequent_words_80001-90000.txt"
TOP_WORDS_FILEPATH_19 = r"source_data/frequent_words_90001-100000.txt"
TOP_WORDS_FILEPATH_20 = r"source_data/frequent_words_100001-110000.txt"
TOP_WORDS_FILEPATH_21 = r"source_data/frequent_words_110001-120000.txt"
TOP_WORDS_FILEPATH_22 = r"source_data/frequent_words_120001-130000.txt"
TOP_WORDS_FILEPATH_23 = r"source_data/frequent_words_130001-140000.txt"
TOP_WORDS_FILEPATH_24 = r"source_data/frequent_words_140001-150000.txt"
TOP_WORDS_FILEPATH_25 = r"source_data/frequent_words_150001-157000.txt"


def ordered_set(word_list):

    word_list_set = list(set(word_list))
    ordered_word_list = []

    for word in word_list:
        if word in word_list_set and word not in ordered_word_list:
            ordered_word_list.append(word)

    return ordered_word_list


def read_words(filepath):

    words = []
    f = open(filepath, "r")

    for x in f:
        words.append(x.strip())

    return words


def read_top_words(filepath):

    top_words = []
    f = open(filepath, "r")

    for x in f:
        words = x.strip().split(' ')
        for word in words:
            top_words.append(word)

    return ordered_set(word_list=top_words)


def read_all_top_words():

    top_words = read_top_words(filepath=TOP_WORDS_FILEPATH_1)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_2)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_3)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_4)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_5)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_6)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_7)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_8)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_9)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_10)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_11)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_12)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_13)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_14)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_15)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_16)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_17)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_18)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_19)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_20)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_21)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_22)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_23)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_24)
    top_words = top_words + read_top_words(filepath=TOP_WORDS_FILEPATH_25)

    return top_words


def limit_to_five_letters(word_list):

    wordle_words = []
    loweralphabets = "abcdefghijklmnopqrstuvwxyz"

    for word in word_list:
        if type(word) is not float:  # avoid nan being considered a float with no length
            if len(word) == 5:

                # Must be alphabetical letters, not random characters
                char_length = 0
                for char in word:
                    if char.isalpha() and char in wu.LOWER_ALPHABETS:
                        char_length += 1

                if char_length == 5:
                    wordle_words.append(word)

    return ordered_set(word_list=wordle_words)


def write_to_txt(filepath, words):

    with open(filepath, 'a') as f:
        for word in words:
            f.write(word + '\n')


def check_existing_filepath(filepath):

    if os.path.isfile(filepath):
        exc_str = "Filepath already exists: " + filepath
        raise Exception(exc_str)


def convert_to_txt(wordle_words_filepath, top_wordle_words_filepath):

    check_existing_filepath(filepath=wordle_words_filepath)
    check_existing_filepath(filepath=top_wordle_words_filepath)

    # Words list
    words = read_words(filepath=WORDS_FILEPATH)

    # Top frequent words in Wikipedia
    top_words = read_all_top_words()

    # Consolidate to 5-letter words
    wordle_words = limit_to_five_letters(word_list=words)
    wordle_words.sort()
    top_wordle_words = limit_to_five_letters(word_list=top_words)

    # Convert to TXT
    write_to_txt(filepath=wordle_words_filepath, words=wordle_words)
    write_to_txt(filepath=top_wordle_words_filepath, words=top_wordle_words)
