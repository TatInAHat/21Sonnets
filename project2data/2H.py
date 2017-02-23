########################################
# CS/CNS/EE 155 2017
# Problem Set 5
#
# Author:       Andrew Kang
# Description:  Set 5
########################################

from HMM import unsupervised_HMM

from Utility import Utility

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
    print x
    lst_x = x.split()
    # print inv_map
    word_emission = []
    for i in lst_x:
        word_emission.append(inv_map[int(i)])
    return ' '.join(word_emission)

if __name__ == '__main__':
    print('')
    print('')
    print('#' * 70)
    print("{:^70}".format("Running Code For Question 2H"))
    print('#' * 70)
    print('')
    print('')

hmm1 = unsupervised_learning(4, 10)
print hmm1.lower()
