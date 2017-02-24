########################################
# CS/CNS/EE 155 2017
# Problem Set 5
#
# Author:       Andrew Kang
# Description:  Set 5
########################################

from HMM import unsupervised_HMM
from Utility import Utility
import numpy as np
import string
import nltk 
from hmmlearn import hmm
from nltk.corpus import cmudict
import itertools
from collections import Counter
from itertools import chain


d = cmudict.dict()
def nsyl(word):
    try:
        s = [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
    except KeyError:
        new_word = word[:-1]
        s = nsyl(new_word)
    return s

def unsupervised_learning(n_states, n_iters):
    '''
    Trains an HMM using supervised learning on the file 'shake_words.txt' and
    prints the results.

    Arguments:
        n_states:   Number of hidden states that the HMM should have.
    '''
    genres, genre_map = Utility.load_poem_hidden()
    genres = genres[:-1]

    # Train the HMM.
    HMM = unsupervised_HMM(genres, n_states, n_iters)

    # Print the transition matrix.
    # print("Transition Matrix:")
    # print('#' * 70)
    # for i in range(len(HMM.A)):
    #     print(''.join("{:<12.3e}".format(HMM.A[i][j]) for j in range(len(HMM.A[i]))))
    # print('')
    # print('')

    # Print the observation matrix.
    # print("Observation Matrix:  ")
    # print('#' * 70)
    # for i in range(len(HMM.O)):
    #     print(''.join("{:<12.3e}".format(HMM.O[i][j]) for j in range(len(HMM.O[i]))))
    # print('')
    # print('')

    inv_map = {v: k for k, v in genre_map.iteritems()}
    x = HMM.generate_emission(10)
    # print x
    lst_x = x.split()
    # print inv_map
    word_emission = []
    for i in lst_x:
        #print word_emission
        num1 = int(i)
        if inv_map[int(i)] == '%':
            while inv_map[num1] == '%':
                replace = HMM.generate_emission(1)
                lst_r = replace.split()
                num1 = int(lst_r[0])
                # print 'PRINTING WORD:'
                # print inv_map[num1]
                # print nsyl(inv_map[num1])
        word_emission.append(inv_map[num1])
    syl_count = 0 
    for i in xrange(len(word_emission)):
        if (syl_count + (nsyl(word_emission[i])[0]) > 10):
            word_emission = word_emission[:i]
            break 
        else: 
            syl_count += (nsyl(word_emission[i])[0])
    
    return ' '.join(word_emission)


if __name__ == '__main__':
    print('')
    print('')
    print('#' * 70)
    print("{:^70}".format("Running Code For Question 2H"))
    print('#' * 70)
    print('')
    print('')

# hmm1 = unsupervised_learning(4, 10)
# print hmm1.lower()

sonnet = []
for i in xrange(14):
    hmm1 = unsupervised_learning(20, 10)
    sonnet.append(hmm1.lower())

for i in xrange(len(sonnet)):
    print sonnet[i]

