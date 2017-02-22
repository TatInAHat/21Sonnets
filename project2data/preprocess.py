import numpy as np
from hmmlearn import hmm
from nltk.corpus import cmudict
# nltk.download('book')


def separate_sonnets(filename):
    # ignores empty lines
    lines = np.genfromtxt(filename, delimiter='\n', dtype=str)
    lines = np.ndarray.tolist(lines)

    bad_list = [str(i) for i in xrange(155)]
    good_lines = []
    corpus_lines = []

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
            good_lines.append(lines[i])


def main():
    shakespeare = '/Users/someone250/Desktop/21Sonnets/project2data/shakespeare.txt'

    separate_sonnets(shakespeare)

main()