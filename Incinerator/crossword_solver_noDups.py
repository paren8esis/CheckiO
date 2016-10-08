# -*- coding: utf-8 -*-

# This program uses the Forward Checking (FC) algorithm.
#
# Sources:
#  http://www.cs.toronto.edu/~fbacchus/Papers/liu.pdf
#  http://www.cs.toronto.edu/~fbacchus/Papers/BGCP95.pdf

import numpy as np

def dwo(constraints, validWords, v, domain):
    ''' The domain wipe-out function. 
    Checks if there are any possible values left for a word and if so returns
    False. Otherwise it returns True. '''
    for value_ind in range(len(validWords[constraints[v][v][0]])):
        if domain[v][value_ind] == -1:
            return False
    return True

def restore(constraints, validWords, words, level, domain):
    '''' Restores the domains after dropping a certain value, so that value
    can be used again in the future for another word. '''
    for word in words:
        for value_ind in range(len(validWords[constraints[word][word][0]])):
            if (domain[word][value_ind] == level):
                domain[word][value_ind] = -1

def check_forward(constraints, validWords, words, domain, level, v, value_v):
    ''' The forward checking part of the algorithm.
    Performs constraint propagation for future values. '''
    for w in words:
        if constraints[v][w][0] != -1:
            for value_w_ind, value_w in enumerate(validWords[constraints[w][w][0]]):
                if domain[w][value_w_ind] == -1:
                    if (constraints[v][w][0] != -1):
                        if (value_v[constraints[v][w][0]] != value_w[constraints[v][w][1]]):
                            domain[w][value_w_ind] = level
            if dwo(constraints, validWords, w, domain):
                return False
    return True

def mark_domains(constraints, words, ind, domain, length, level):
    ''' After selecting a certain value, this function marks all other
    domains so the value won't be used again for another word. '''
    for w in words:
        if (constraints[w][w][0] == length) and (domain[w][ind] == -1):
            domain[w][ind] = level

def search_FC(constraints, validWords, words, domain, level, solution):
    ''' The main FC algorithm. '''
    v = words.pop(0)
    for value_v_ind, value_v in enumerate(validWords[constraints[v][v][0]]):
        if domain[v][value_v_ind] == -1:
            mark_domains(constraints, words, value_v_ind, domain, len(value_v), level)
            solution.append((v, value_v))
            if len(words) == 0:
                return solution
            else:
                if check_forward(constraints, validWords, words, domain, level, v, value_v) and search_FC(constraints, validWords, words, domain, level+1, solution):
                    return solution
                else:
                    solution.remove((v, value_v))
                    restore(constraints, validWords, words, level, domain)
    words.insert(0, v)
    return False

def mark_word(crossword, crossword_marked, label, i, j, horizontal=True):
    ''' Marks each cell of the crossword belonging to a word with that word's
    label. '''
    length = 0
    while (crossword[i][j] == '.'):
        crossword_marked[i][j] += ' ' + label + '-' + str(length)
        length += 1
        if horizontal:
            j += 1
            if j >= crossword.shape[1]:
                return (crossword_marked, length)
        else:
            i += 1
            if i >= crossword.shape[0]:
                return (crossword_marked, length)
    return (crossword_marked, length)

def solver(crossword, wordlist):

    # Prepare the crossword for searching
    crossword = [[x for x in row] for row in crossword]
    crossword = np.asarray(crossword)

    # Create another crossword grid with all words labeled
    crossword_marked = np.asarray([[''] * crossword.shape[1] for x in range(crossword.shape[0])], dtype=(str, 110))
    label = 0
    nodeCond = {}
    for i in range(crossword.shape[0]):
        for j in range(crossword.shape[1]):
            if crossword[i][j] == '.':
                if (i < crossword.shape[0]-1) and (i == 0 or crossword[i-1][j] == 'X') and (crossword[i+1][j] == '.'):
                    crossword_marked, word_length = mark_word(crossword, crossword_marked, str(label), i, j, horizontal=False)
                    nodeCond[label] = word_length
                    label += 1
                if (j < crossword.shape[1]-1) and (j == 0 or crossword[i][j-1] == 'X') and (crossword[i][j+1] == '.'):
                    crossword_marked, word_length = mark_word(crossword, crossword_marked, str(label), i, j, horizontal=True)
                    nodeCond[label] = word_length
                    label += 1

    words = list(range(label))

    # Create an ndarray with the constraints.
    # Node constraint: Length of the word
    # Edge constraint: Letters that must be equal to letters of another crossing word
    constraints = []
    for i in range(len(words)):
        c1 = list()
        for j in range(len(words)):
            if (i == j):
                c1.append([nodeCond[i], nodeCond[i]])
            else:
                c1.append([-1, -1])
        constraints.append(c1)

    constraints = np.asarray(constraints)

    for i in range(crossword.shape[0]):
        for j in range(crossword.shape[1]):
            if len(crossword_marked[i][j]) > 0:
                const = crossword_marked[i][j].strip().split(' ')
                c1, c1_ind = const[0].split('-')
                for c_next in range(1, len(const)):
                    c2, c2_ind = const[c_next].split('-')
                    constraints[int(c1)][int(c2)][0] = int(c1_ind)
                    constraints[int(c1)][int(c2)][1] = int(c2_ind)
                    constraints[int(c2)][int(c1)][0] = int(c2_ind)
                    constraints[int(c2)][int(c1)][1] = int(c1_ind)

    # Create a structure containing all valid words for different word lengths.
    validWords = {}
    for word_length in range(3, constraints.max()+2):
        validWords[word_length] = [x for x in wordlist if len(x) == word_length]

    # Create the domain of each word and initialize it with -1 for every value.
    domain = []
    for v in words:
        domain.append([-1] * len(validWords[constraints[v][v][0]]))

    # Run the algorithm
    solution = search_FC(constraints, validWords, words, domain, 1, [])

    # Modify the solution so it complies with the required output form.
    solution_dict = {}
    for i in solution:
        solution_dict[int(i[0])] = i[1]

    for i in range(crossword.shape[0]):
        for j in range(crossword.shape[1]):
            if crossword[i][j] == '.':
                c, c_ind = crossword_marked[i][j].strip().split(' ')[0].split('-')
                crossword[i][j] = solution_dict[int(c)][int(c_ind)]
    return [''.join(crossword[x]) for x in range(crossword.shape[0])]