src = int(input('Src:'))
dest = int(input('dest'))

# def solution(src, dest):
#     #Your code here
#     # distance = abs(dest - src)
#     num_moves = 0
#     splinter = src
#     moves = [-17, -15, -10, -6, 6, 10, 15, 17]
#     while(src != dest):
#         num_moves += 1
#         for move in moves:
#             if((src + move) == dest):
#                 src = src + move
#                 break
#             elif()
#     return num_moves


# print(str(solution(src, dest)))

import heapq
from collections import defaultdict

BOARD_SIZE = 8
BOARD_MOVEMENTS =[(1, 2), (1, -2), (-1, 2), (-1, -2), (2,1), (2, -1), (-2, 1), (-2, -1)]

class Node():
    def __init__(self, x, y, distance=0):
        self.x = x
        self.y = y
        self.distance = distance
    ## Makes the node iterable, meaning it becomes a generator, not storing the values just returning them
    def __iter__ (self):
        for i in [self.x, self.y]:
            yield i
    ## Defines the equivalent method for nodes
    def __eq__(self, node):
        return self.x == node.x and self.y == node.y
    ## Defines the less than method
    def __lt__(self, node):
        return self.x < node.x or (self.x == node.x and self.y < node.y)
    
    def __hash__(self):
        return hash(tuple(self))
    
class Board():
    def __init__(self, size, movements):
        self.size = size
        self.movements = movements
    
    def node(self, position):
        ## Turns the Range of numbers/squares into Nodes
        return Node(int(position % self.size) + 1, int(position / self.size) + 1)
    ## Ternary, checks if x, is greater than 0 and less than the limits
    def valid(self, x, y):
        return True if x>= 0 < self.size and y >= 0 < self.size else False
     
    def distance(self, start, end):
        ## Finding the shortest distance using Breadth-First search
        queue = []
        queue.append(start)
        visited = {}  ## Create a dictionary to hold the visted nodes
        ## If there is a valid in the queue
        while queue:
            ## Gets the node at position 0 of the []
            node = queue.pop(0)
            ## The node reached the endpoint
            if node == end:
                return node.distance
            ## Only runs if the node has not been moved to
            if node not in visited:
                visited[node] = True
                ## Finds direction the knight should move in
                for offset in self.movements:
                    x, y = list(tuple(x + y for x, y in zip(tuple(node), offset)))
                    ## If the node is valid, push it into the queue
                    if self.valid(x, y):
                        queue.append(Node(x, y, node.distance + 1))
            
        return float('inf')
                        

def solution(src, dest):
    ## Create the "cheeseboard"
    cheeseboard = Board(size = BOARD_SIZE, movements = BOARD_MOVEMENTS)
    
    ## Creates the src and dest Nodes
    start = cheeseboard.node(src)
    end = cheeseboard.node(dest)
    
    return cheeseboard.distance(start, end)


print(str(solution(src, dest)))