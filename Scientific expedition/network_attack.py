def find_node_neighbors(matrix, node, infected):
    return [i for i, x in enumerate(matrix[node]) if (x == 1 and i != node and i not in infected)]

def capture(matrix):
    infected = [0]
    neighbors = find_node_neighbors(matrix, 0, infected)
    connections = [[matrix[neighbor][neighbor], neighbor, find_node_neighbors(matrix, neighbor, infected)] for neighbor in neighbors]
    connections = sorted(connections, key=lambda x: x[0])
    connections_ids = [x[1] for x in connections]

    minutes = 0
    while (len(connections) > 0):
        connections = [[connection[0]-1, connection[1], connection[2]] for connection in connections]
        while (len(connections) > 0) and (connections[0][0] == 0): # Node infected!
            new_infected = connections.pop(0)
            if (new_infected[1] in connections_ids):
                connections_ids.remove(new_infected[1])
            infected.append(new_infected[1])
            neighbors = find_node_neighbors(matrix, new_infected[1], infected)
            connections += [[matrix[neighbor][neighbor], neighbor, find_node_neighbors(matrix, neighbor, infected)] for neighbor in neighbors if neighbor not in infected and neighbor not in connections_ids]
            connections_ids += neighbors
        connections = sorted(connections, key=lambda x: x[0])
        minutes += 1

    return minutes
