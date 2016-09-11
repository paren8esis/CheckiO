# -*- coding: utf-8 -*-

class Friends:
    def __init__(self, connections):
        self.names_list = []
        self.connected_list = {}
        for connection in connections:
            c = list(connection)
            self.names_list.append(c[0])
            self.names_list.append(c[1])
            if (c[0] not in self.connected_list.keys()):
                self.connected_list[c[0]] = set([c[1]])
            else:
                self.connected_list[c[0]].add(c[1])
            if (c[1] not in self.connected_list.keys()):
                self.connected_list[c[1]] = set([c[0]])
            else:
                self.connected_list[c[1]].add(c[0])
        self.names_list = set(self.names_list)

    def add(self, connection):
        c = list(connection)
        if ((c[1] in self.names_list) and (c[0] not in self.connected_list[c[1]])):
            self.names_list.add(c[0])
            if (c[0] not in self.connected_list.keys()):
                self.connected_list[c[0]] = set([c[1]])
            else:
                self.connected_list[c[0]].add(c[1])
            self.connected_list[c[1]].add(c[0])
            return True
        elif ((c[0] in self.names_list) and (c[1] not in self.connected_list[c[0]])):
            self.names_list.add(c[1])
            if (c[1] not in self.connected_list.keys()):
                self.connected_list[c[1]] = set([c[0]])
            else:
                self.connected_list[c[1]].add(c[0])
            self.connected_list[c[0]].add(c[1])
            return True
        elif ((c[0] not in self.names_list) and (c[1] not in self.names_list)):
            self.names_list.add(c[0])
            self.names_list.add(c[1])
            if (c[0] not in self.connected_list.keys()):
                self.connected_list[c[0]] = set([c[1]])
            else:
                self.connected_list[c[0]].add(c[1])
            if (c[1] not in self.connected_list.keys()):
                self.connected_list[c[1]] = set([c[0]])
            else:
                self.connected_list[c[1]].add(c[0])
            return True
        else:
            return False

    def remove(self, connection):
        c = list(connection)
        try:
            if (c[0] in self.connected_list[c[1]]):
                if (len(self.connected_list[c[0]]) == 1):
                    self.names_list.discard(c[0])
                    del self.connected_list[c[0]]
                else:
                    self.connected_list[c[0]].discard(c[1])
                if (len(self.connected_list[c[1]]) == 1):
                    self.names_list.discard(c[1])
                    del self.connected_list[c[1]]
                else:
                    self.connected_list[c[1]].discard(c[0])
                return True
            else:
                return False
        except KeyError:
            return False

    def names(self):

        return self.names_list
    def connected(self, name):
        try:
            return self.connected_list[name]
        except KeyError:
            return set([])