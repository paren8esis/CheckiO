# -*- coding: utf-8 -*-

def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if isinstance(v, dict):
                if (len(v) == 0):  # value is an empty dictionary
                    result["/".join((path + (k, )))] = ''
                else:
                    stack.append((path + (k, ), v))
            else:
                result["/".join((path + (k,)))] = v
    return result
