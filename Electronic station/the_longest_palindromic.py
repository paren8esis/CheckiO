# -*- coding: utf-8 -*-
#! /usr/env/python3

# Code taken from: 
# http://www.geeksforgeeks.org/longest-palindromic-substring-set-2/

def LPS(s):
    maxLength = 1

    start = 0
    length = len(s)

    low = 0
    high = 0

    # One by one consider every character as center point of
    # even length palindromes
    for i in range(1, length):
        # Find the longest even length palindrome with center
        # points as i-1 and i.
        low = i - 1
        high = i
        while (low >= 0) and (high < length) and (s[low] == s[high]):
            if (high - low + 1 > maxLength):
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

        # Find the longest odd length palindrome with center 
        # point as i
        low = i - 1
        high = i + 1
        while (low >= 0) and (high < length) and (s[low] == s[high]):
            if (high - low + 1 > maxLength):
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

    return s[start:start + maxLength]

if __name__ == '__main__':
    print(LPS('forgeeksskeegfor'))