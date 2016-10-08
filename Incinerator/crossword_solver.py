import numpy as np

def dwo(v, validWords, domain):
    for value_ind in range(len(validWords[v])):
        if domain[v][value_ind] == -1:
            return False
    return True

def restore(words, level, validWords, domain):
    for word in words:
        for value_ind in range(len(validWords[word])):
            if (domain[word][value_ind] == level):
                domain[word][value_ind] = -1

def check_forward(validWords, constraints, words, domain, level, v, value_v):
    for w in words:
        if constraints[v][w][0] != -1:
            for value_w_ind, value_w in enumerate(validWords[w]):
                if domain[w][value_w_ind] == -1:
                    if (constraints[v][w][0] != -1):
                        if (value_v[constraints[v][w][0]] != value_w[constraints[v][w][1]]):
                            domain[w][value_w_ind] = level
            if dwo(w, validWords, domain):
                return False
    return True

def search_FC(constraints, words, domain, validWords, level, solution):
    v = words.pop(0)
    for value_v_ind, value_v in enumerate(validWords[v]):
        if domain[v][value_v_ind] == -1:
            solution.append((v, value_v))
            if len(words) == 0:
                return solution
            else:
                if check_forward(validWords, constraints, words, domain, level, v, value_v) and search_FC(constraints, words, domain, validWords, level+1, solution):
                    return solution
                else:
                    solution.remove((v, value_v))
                    restore(words, level, validWords, domain)
    words.insert(0, v)
    return False

def mark_word(crossword, crossword_marked, label, i, j, horizontal=True):
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
    crossword = [[x for x in row] for row in crossword]
    crossword = np.asarray(crossword)

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

    validWords = {}
    for word in words:
        validWords[word] = [x for x in wordlist if len(x) == nodeCond[word]]

    domain = []
    for v in words:
        domain.append([-1] * len(validWords[v]))
    solution = search_FC(constraints, words, domain, validWords, 1, [])

    solution_dict = {}
    for i in solution:
        solution_dict[int(i[0])] = i[1]

    for i in range(crossword.shape[0]):
        for j in range(crossword.shape[1]):
            if crossword[i][j] == '.':
                c, c_ind = crossword_marked[i][j].strip().split(' ')[0].split('-')
                crossword[i][j] = solution_dict[int(c)][int(c_ind)]
    return [''.join(crossword[x]) for x in range(crossword.shape[0])]