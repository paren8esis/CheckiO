#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def create_intervals(data):
    import itertools

    lst = sorted(list(data))
    if len(lst) == 0:
        return []

    s = list(itertools.filterfalse(lambda x: x == lst[lst.index(x)-1] + 1, lst))
    e = list(itertools.filterfalse(lambda x: x == lst[lst.index(x)+1] - 1, lst[:-1]))
    if (lst[-1] not in e):
        e.append(lst[-1])

    return list(zip(s,e))
