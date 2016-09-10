# -*- coding: utf-8 -*-

def color_map(region):
    # Find all countries and their neighbors
    countries = []
    neighbors = {}
    for row_ind, row in enumerate(region):
        for col_ind, cell in enumerate(row):
            if (cell not in countries):
                countries.append(cell)

            # Check for neighbors with greater ID
            neighs = []
            if (col_ind > 0):
                if (region[row_ind][col_ind-1] > cell):
                    neighs.append(region[row_ind][col_ind-1])
            try:
                if (region[row_ind+1][col_ind] > cell):
                    neighs.append(region[row_ind+1][col_ind])
            except IndexError:
                pass
            try:
                if (region[row_ind][col_ind+1] > cell):
                    neighs.append(region[row_ind][col_ind+1])
            except IndexError:
                pass
            if (row_ind > 0):
                if (region[row_ind-1][col_ind] > cell):
                    neighs.append(region[row_ind-1][col_ind])

            if (cell not in neighbors.keys()):
                neighbors[cell] = set(neighs)
            else:
                neighbors[cell] = set(neighs) | neighbors[cell]

    countries = sorted(countries)
    # Initialize possible colors for each country
    colors = []
    for country in countries:
        colors.append([1,2,3,4])

    # Colorize!
    res = []
    for country in countries:
        res.append(colors[country].pop(0))
        for neigh in neighbors[country]:
            if (res[-1] in colors[neigh]):
                colors[neigh].remove(res[-1])

    return res