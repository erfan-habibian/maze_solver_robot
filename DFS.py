import numpy as np
import maze as Maze


visited = list()
pathArray = list()
start = Maze.start
goal = Maze.goal
matrix = Maze.matrix
rows = Maze.rows
columns = Maze.columns


def DFSClass():
    findPath()
    
    
    
def findPath():
    DFS(start)
    
    
    
           
def DFS(a):
    current = start
    pathArray.append(current)
    while not goal in pathArray:
        a = findAvaNab(pathArray[-1])
        if(a!=(-1,-1)):
            pathArray.append(a)
            visited.append(a)
        else:
            visited.append(pathArray.pop())
    

    for each in pathArray:
        matrix[each[0]][each[1]] = 7
    print('DFS: path is: ')
    print(matrix)
    print('\a')    
        


def findAvaNab(p):
    
    i,j = p[0],p[1]
    if(check((i+1,j)) and check2((i+1,j),'R')==1):
        return (i+1,j)
    if(check((i,j+1)) and check2((i,j+1),'U')==1):
        return (i,j+1)
    if(check((i-1,j)) and check2((i-1,j),'L')==1):
        return (i-1,j)        
    if(check((i,j-1)) and check2((i,j-1),'D')==1):
        return (i,j-1)   
    return (-1,-1)
        
def check(c):
    i,j = c[0], c[1]    
    if(not (i,j) in visited \
    and (i,j) != start \
    and i>=0 and i<=rows-1 \
    and j>=0 and j<=columns-1):
        if(matrix[i][j] == 0):
            return True
    return False
    
    
def check2(c, direction):

    if(direction == 'L' \
        and not (c[0]-1,c[1]) in pathArray \
            and not (c[0],c[1]-1) in pathArray \
                and not (c[0],c[1]+1) in pathArray):
                    return 1
    elif(direction == 'R' \
        and not (c[0]+1,c[1]) in pathArray \
            and not (c[0],c[1]-1) in pathArray \
                and not (c[0],c[1]+1) in pathArray):
                    return 1                
    elif(direction == 'U' \
        and not (c[0]+1,c[1]) in pathArray \
            and not (c[0]-1,c[1]) in pathArray \
                and not (c[0],c[1]+1) in pathArray):
                    return 1 
    elif(direction == 'D' \
        and not (c[0]+1,c[1]) in pathArray \
            and not (c[0]-1,c[1]) in pathArray \
                and not (c[0],c[1]-1) in pathArray):
                    return 1 
    return 0    
    
    