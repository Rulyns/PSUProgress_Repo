class Queue:
    '''
        Python list implementation of a FIFO Queue
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


class Graph:
    '''
        >>> g1 = {'B': ['E', 'C'],
        ...       'F': [],
        ...       'C': ['F'],
        ...       'A': ['D', 'B'],
        ...       'D': ['C'],
        ...       'E': ['F']}
        >>> g = Graph(g1)
        >>> g.bfs('A')
        ['A', 'B', 'D', 'C', 'E', 'F']

        >>> g2 = {'Bran': ['East', 'Cap'],
        ...       'Flor': [],
        ...       'Cap':  ['Flor'],
        ...       'Apr':  ['Dec', 'Bran'],
        ...       'Dec':  ['Cap'],
        ...       'East': ['Flor']}
        >>> g = Graph(g2)
        >>> g.bfs('Apr')
        ['Apr', 'Bran', 'Dec', 'Cap', 'East', 'Flor']
    '''
    def __init__(self, graph_repr):
        self.adjacency_list = graph_repr

    def bfs(self, start):
        '''
        bfs(start)
            Let Q be an empty queue
            Q.enqueue(start) 
            Mark 'start' as visited
            while Q is not empty:
                #- Remove an item from Q, its neighbors will be visited now
                node = Q.dequeue()
                #- For each neighbor, add it to the queue if it is unvisited
                for each neighbor 'x' of node: 
                    if x is not visited 
                        Enqueue x in Q to further visit its neighbors
        '''
        Q_Implementation = Queue()
        visited = []
        Q_Implementation.enqueue(start)
        visited += [start]
        while not Q_Implementation.isEmpty():
            node = Q_Implementation.dequeue()
            for x in sorted(self.adjacency_list.get(node)):
                if x not in visited:
                    visited += [x]
                    Q_Implementation.enqueue(x)
        return visited
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
