from Point import Point
from queueNode import queueNode
from BFS import BFS


def FindDestination(mat, val:int):
    dest=[(index, row.index(val)) for index, row in enumerate(mat) if val in row]
    return Point(dest[0][0],dest[0][1])

#Can accept user input but test case used here
#create unit tests to verify it working
mat=[[1,1,0],[0,1,0],[9,1,0]]
#mat = input()
source = Point(0,0)
dest = FindDestination(mat, 9)
dist = BFS(mat,source,dest, 9)
print(dist)
