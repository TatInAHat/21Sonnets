import numpy as np
import string
from hmmlearn import hmm
from nltk.corpus import cmudict
import itertools
from collections import Counter
from itertools import chain
# nltk.download('book')

# finds the number of syllables in a word.
d = cmudict.dict()

'''
Works for nonwords now by checking if KeyError
If word not real, remove last character and try again
'''
def nsyl(word):
    try:
        s = [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
    except KeyError:
        new_word = word[:-1]
        s = nsyl(new_word)
    return s

# s is a string of words
def strip_punc(s):
    return s.translate(string.maketrans("",""), string.punctuation)


def separate_sonnets(filename):
    # ignores empty lines
    lines = np.genfromtxt(filename, delimiter='\n', dtype=str)
    lines = np.ndarray.tolist(lines)

    bad_list = [str(i) for i in xrange(155)]
    good_lines = []
    words = []

    # put non-number lines in good_lines
    for i in xrange(len(lines)):
        if lines[i] not in bad_list:
            good_lines.append(lines[i].split())

    # list of all words
    words = list(itertools.chain.from_iterable(good_lines))
    distinct_words = list(set(words))

    for i in xrange(len(distinct_words)):
        distinct_words[i] = distinct_words[i].strip('()')

    print good_lines[0]
    return good_lines

# def syllable_things():
    # print distinct_words
    # syllable_dict = {}

    # for i in xrange(len(distinct_words)):
    #     syllable_dict[distinct_words[i]] = nsyl(distinct_words[i])[0]

    # print syllable_dict
    # syllables = []
    # for i in xrange(len(good_lines)):
    #     syls = []
    #     for j in xrange(len(good_lines[i])):
    #         num_syls = nsyl(good_lines[i][j])
    #         if len(num_syls) > 1:
    #             num_syls = [num_syls[0]]
    #         syls.append(num_syls)
    #     syllables.append(syls)


    # The average number of syllables with this method is 9.95864661654
    # lump_sum = 0
    # for i in xrange(len(syllables)):
    #     summation = 0
    #     for j in xrange(len(syllables[i])):
    #         summation += syllables[i][j][0]
    #     lump_sum += summation


def main():
    shakespeare = '/Users/someone250/Desktop/21Sonnets/project2data/shakespeare.txt'

    separate_sonnets(shakespeare)

main()