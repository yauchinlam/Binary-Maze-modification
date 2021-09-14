from Point import Point
from queueNode import queueNode
from collections import deque

def isValid(row: int, col: int, mat: list):
    COL = len(mat[0]) 
    ROW = len(mat)
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)


rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

def BFS(mat, src: Point, dest: Point, val: int):
    COL = len(mat[0])     
    ROW = len(mat)

    if mat[src.x][src.y]!=1 or mat[dest.x][dest.y]!=val:
        return -1
    visited = [[False for x in range(COL)] for y in range(ROW)]

    visited[src.x][src.y] = True
    
    q = deque()
    
    s = queueNode(src,0)
    q.append(s)     

    while q:

        curr = q.popleft()

        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist
        
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            if (isValid(row,col,mat) and (mat[row][col] == 1 or mat[row][col] == val) and not visited[row][col]):
                visited[row][col] = True
                Adjcell = queueNode(Point(row,col), curr.dist+1)
                q.append(Adjcell)
    
    return -1


