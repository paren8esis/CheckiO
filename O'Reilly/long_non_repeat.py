#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def non_repeat(line):
    visited = {}

    max_substring = ''
    curr_substring = ''
    for i in range(len(line)):
        if line[i] not in visited.keys():
            curr_substring += line[i]
            visited[line[i]] = i
        else:
            curr_substring = line[visited[line[i]]+1:i+1]
            visited = dict(filter(lambda x: x[1]>visited[line[i]],
                                  iter(visited.items())))
            visited[line[i]] = i
        if len(curr_substring) > len(max_substring):
            max_substring = curr_substring
    return max_substring