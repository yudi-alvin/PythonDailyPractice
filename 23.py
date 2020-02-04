"""
Breadth First Search or BFS for a Graph

"""


"""
This problem was asked by Google.
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. 
Each False boolean represents a tile you can walk on.
Given this matrix, a start coordinate, and an end coordinate, 
return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, 
then return null. You can move up, left, down, and right. You cannot move through walls. 
You cannot wrap around the edges of the board.
For example, given the following board:
[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, 
since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

Concept:
-Deep first search
-Breadth first search
"""

import numpy as np

m =[['f', 'f', 'f', 'f'],
['t', 't', 't', 't'],
['f', 'f', 'f', 'f'],
['f', 'f', 'f', 'f']]
start=(3,0)
end=(0,0)

def minStep(m,start, end):
    #Breadth First Search
    explored=[]
    queue =[[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1] #neightbour coordinate
        if node not in explored:
        #getting neighbours coordinates
            neighbours=[]
            if node[0] + 1 < len(m) and m[node[0]+1][node[1]] == 'f':
                neighbours.append((node[0]+1,node[1]))
            if node[0] - 1 >= 0 and m[node[0]-1][node[1]] == 'f':
                neighbours.append((node[0]-1,node[1]))
            if node[1] + 1 < len(m) and m[node[0]][node[1]+1] == 'f':
                neighbours.append((node[0],node[1]+1))
            if node[1] - 1 >=0 and m[node[0]][node[1]-1] == 'f':
                neighbours.append((node[0],node[1]-1))
            
            for neighbour in neighbours:
                new_path = list(path) #[[(0,0)]]
                new_path.append(neighbour)#[[(0,0)],[(0,1)]]
                queue.append(new_path) #queue will contain each neighbour path
                if neighbour == end:
                        return new_path
            
            # mark node as explored
            explored.append(node)
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("
        

print(minStep(m,start, end))
