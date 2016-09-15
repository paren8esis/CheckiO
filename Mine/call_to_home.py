# -*- coding: utf-8 -*-

from math import ceil

def total_cost(calls):
    cost = 0
    if (len(calls) == 0):
        return cost

    current_day = calls[0].split()[0]
    call_duration_day = 0
    for i in range(len(calls)):
        if (calls[i].startswith(current_day)):
            call_duration_day += ceil(int(calls[i].split()[2]) / 60)
        else:
            if (call_duration_day > 100):
                cost += 100 + ((call_duration_day - 100)*2)
            else:
                cost += call_duration_day
            current_day = calls[i].split()[0]
            call_duration_day = ceil(int(calls[i].split()[2]) / 60)


    if (call_duration_day > 100):
        cost += 100 + ((call_duration_day - 100)*2)
    else:
        cost += call_duration_day
    return cost