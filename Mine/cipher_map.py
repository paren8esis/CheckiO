# -*- coding: utf-8 -*-

import numpy as np

def recall_password(cipher_grille, ciphered_password):
    cipher = []
    for row in ciphered_password:
        cipher.append([x for x in row])
    cipher = np.asarray(cipher)

    grille = []
    for row in cipher_grille:
        grille.append([x == 'X' for x in row])
    grille = np.asarray(grille)

    deciphered = ''
    for i in range(4):
        grille = np.rot90(grille)
        deciphered = ''.join(cipher[grille]) + deciphered

    return deciphered