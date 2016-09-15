# -*- coding: utf-8 -*-

def flat_list(array):
 return [array] if (type(array)==int) else ([] if (array==[]) else flat_list(array[0])+flat_list(array[1:]))