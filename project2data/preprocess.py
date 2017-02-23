import numpy as np
import string
from hmmlearn import hmm
from nltk.corpus import cmudict
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

    # collect lines in sonnets 99 and 126
    for i in xrange(len(lines)):
        if lines[i] == '99':
            for j in xrange(1, 16):
                bad_list.append(lines[i + j])
        elif lines[i] == '126':
            for k in xrange(1, 13):
                bad_list.append(lines[i + k])

    # put non-number lines and lines not in sonn. 99 and 126 in good_lines
    for i in xrange(len(lines)):
        if lines[i] not in bad_list:
            good_lines.append(strip_punc(lines[i]).split())

    syllables = []
    for i in xrange(len(good_lines)):
        syls = []
        for j in xrange(len(good_lines[i])):
            num_syls = nsyl(good_lines[i][j])
            if len(num_syls) > 1:
                num_syls = [num_syls[0]]
            syls.append(num_syls)
        syllables.append(syls)

    # The average number of syllables with this method is 9.95864661654
    # lump_sum = 0
    # for i in xrange(len(syllables)):
    #     summation = 0
    #     for j in xrange(len(syllables[i])):
    #         summation += syllables[i][j][0]
    #     lump_sum += summation

    return good_lines


def main():
    shakespeare = '/Users/someone250/Desktop/21Sonnets/project2data/shakespeare.txt'

    separate_sonnets(shakespeare)

main()