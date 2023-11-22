import maze as Maze

pathArray = list()
nodeArray = list()
visited = list()
maze = Maze.matrix
start = Maze.start
goal = Maze.goal
rows = Maze.rows
columns = Maze.columns



class Node:
    x = -1
    y = -1
    parent = None
    
    def setParent(self, p):
        self.parent = p
        
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        
    

def BFS():
    finalNode = buildTree()
    current = finalNode
    while(current != None):
        pathArray.append((current.x,current.y))
        current = current.parent
    for each in pathArray:
        maze[each[0]][each[1]] = 7
    print('BFS path is:')
    print(maze)      
            
            
            
def buildTree():
    current = Node(0,0)
    nodeArray.append(current)
    while(len(nodeArray)>0):
        current = nodeArray.pop()
        i , j = current.x , current.y 
        visited.append((i,j))
        if((i,j) == goal):
            return current
        if(isValid(i+1,j) and check2((i+1,j),'R')==1):
            newNode = Node(i+1,j)
            newNode.setParent(current)
            nodeArray.append(newNode)
        if(isValid(i-1,j) and check2((i-1,j),'L')==1):
            newNode = Node(i-1,j)
            newNode.setParent(current)
            nodeArray.append(newNode)
        if(isValid(i,j+1) and check2((i,j+1),'U')==1):
            newNode = Node(i,j+1)
            newNode.setParent(current)
            nodeArray.append(newNode)
        if(isValid(i,j-1) and check2((i,j-1),'D')==1):
            newNode = Node(i,j-1)
            newNode.setParent(current)
            nodeArray.append(newNode)            
            
            
def isValid(i,j):
    if(not (i,j) in visited \
    and i>=0 and j>=0 \
    and i<=rows-1 and j<=columns-1):
        if(maze[i][j] == 0):
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
    

        