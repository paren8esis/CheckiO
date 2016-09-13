# -*- coding: utf-8 -*-

def generate_lines(dot, offset):
    lines = []
    difference = offset
    while (difference > 0):
        # Horizontal lines
        lines.append([dot+difference-1, dot+difference])
        lines.append([dot+difference+(offset*4)-1, dot+difference+(offset*4)])
        # Vertical lines
        lines.append([dot+((difference-1)*4), dot+(difference*4)])
        lines.append([dot+offset+((difference-1)*4), dot+offset+(difference*4)])
        difference -= 1
    return lines

def checkio(lines_list):
    squares = 0
    for dot in range(1, 17):
        for offset in range(1, 4):
            lines = generate_lines(dot, offset)
            for line in lines:
                if (line not in lines_list) and ([line[1],line[0]] not in lines_list):
                    break
            else:
                squares += 1
    return squares