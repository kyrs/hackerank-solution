#!/usr/bin/python

class stack:
    def __init__ (self):
        self.item =[]

    def isEmpty(self):
        return self.item == []

    def push(self,value):
        self.item.append(value)

    def pop (self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def size (self):
        return len(self.item)



class pacMan(object):
    def __init__(self,food,pacMan,gridDim,grid):
        self.food = food
        self.pacMan = pacMan
        self.gridDim = gridDim
        self.grid = grid
        self.obstacleMarker = "%"
        self.pacmanMarker = "p"
        self.foodMarker = "."
        self.priority = ["UP","LEFT","RIGHT","DOWN"]
    
    def isBlocked(self,coord):
        return self.grid[coord[0]][coord[1]]== self.obstacleMarker

    def validRow(self):
        return self.gridDim[0]== len(self.grid)

    def validCol(self):
        for i,row in enumerate(self.grid):
            if self.gridDim[1] != len(row):
                Exception("Wrong dimesion is provided for the matrix")
                return False
            else:
                return True

    def ValidMatrix(self):
        return self.validRow() and self.validCol()

    def movePosition(self,coord):
        upCoord = [coord[0]-1,coord[1]]
        downCoord = [coord[0]+1,coord[1]]
        leftCoord = [coord[0],coord[1]-1]
        rightCoord = [coord[0],coord[1]+1]

        ## devloping a disctionary of move
        moveDict = {}
        
        if (upCoord[0]<0 or self.isBlocked(upCoord)):
            moveDict["UP"] = 0
        else:
            moveDict["UP"] = upCoord

        if (downCoord[0]>=self.gridDim[0] or self.isBlocked(downCoord)):
            moveDict["DOWN"] = 0
        else:
            moveDict["DOWN"] = downCoord

        if (leftCoord[1]<0 or self.isBlocked(leftCoord)):
            moveDict["LEFT"] = 0
        else:
            moveDict["LEFT"] = leftCoord

        if (rightCoord[1]>=self.gridDim[1] or self.isBlocked(rightCoord)):
            moveDict["RIGHT"] = 0
        else:
            moveDict["RIGHT"] = rightCoord


        return moveDict

    def distancePacman(self,coord):
        return (abs(self.pacMan[0]-coord[0]) + abs(self.pacMan[1]-coord[1]))

    def dfsPathGenerator(self,dfsList):
        stackDfs= dfsList[0:-1]
        listPop = []
        pathGenerator = []
        pathGenerator.append([])
        pathGenerator.append(dfsList[-1])
        while (len(stackDfs)!=0) :
            flag =0
            temp = stackDfs.pop()
            lastStep =pathGenerator[-1]
            possibleDirectionDictionary = self.movePosition(lastStep)
            possibleDirection = [possibleDirectionDictionary[direction] for direction in possibleDirectionDictionary.keys() if possibleDirectionDictionary[direction]]
            prev2LastStep =pathGenerator[-2]
            #possibleDirection = list (set(possibleDirection)-set(prev2LastStep))
            possibleDirection = [dirc for dirc in possibleDirection if dirc !=  prev2LastStep ]
            if self.pacMan in possibleDirection:
                pathGenerator.append(self.pacMan)
                break
            disttemp = self.distancePacman(temp)
            for direction in possibleDirection:
                if direction in listPop:
                    distDir = self.distancePacman(direction)
                    if (distDir < disttemp):
                        pathGenerator.append(direction)
                        flag =1
                        break
                    else:
                        continue
            if ((not flag) and (temp in possibleDirection)):
                pathGenerator.append(temp) 
            listPop.append(temp)
        return pathGenerator


    def foodSearch(self):
        count = 0
        presentCoord = self.pacMan
        searchList = []
        searchList.append(self.pacMan)
        searchStack = stack()
        while (presentCoord != self.food):
            moveDict=self.movePosition(presentCoord)
            presentCoordNew = presentCoord
            for i in self.priority:
                if(moveDict[i] and (moveDict[i] not in searchList) ):
                    presentCoordNew= moveDict[i]    
                    break
                #print presentCoord
            if presentCoordNew == presentCoord:
                searchStack.pop()
                presentCoord = searchStack.peek()
            else:
                presentCoord = presentCoordNew
                searchStack.push(presentCoordNew)
                searchList.append(presentCoordNew)
        return self.dfsPathGenerator(searchList)[1:][::-1]
        #return searchList

def printOutput(listItem) :
    for i,j in listItem:
        print i,j


def dfs( r, c, pacman_r, pacman_c, food_r, food_c, grid):
    pacManCoord =[pacman_r,pacman_c]
    foodCoord = [food_r,food_c]
    gridDim = [r,c] 
    myPac = pacMan(foodCoord,pacManCoord,gridDim,grid)
    if(not myPac.ValidMatrix()) :
        Exception("MAtrix is Invalid !!")
    else:
        listSearch = myPac.foodSearch()
        print len(listSearch)
        printOutput(listSearch)
        print len(listSearch)-1
        printOutput(listSearch)
        #print listSearch
    return




pacman_r = 3
pacman_c = 1
food_r = 5
food_c = 1
r = 7
c = 20
grid = []
grid.append("%%%%%%%%%%%%%%%%%%%%")
grid.append("%--------------%---%")
grid.append("%-%%-%%-%%-%%-%%-%-%")
grid.append("%P---------------%-%")
grid.append("%%%%%%%%%%%%%%%%%%-%")
grid.append("%.-----------------%")
grid.append("%%%%%%%%%%%%%%%%%%%%")
dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)


# if __name__ == "__main__":
#     pacman_r, pacman_c = [ int(i) for i in raw_input().strip().split() ]
#     food_r, food_c = [ int(i) for i in raw_input().strip().split() ]
#     r,c = [ int(i) for i in raw_input().strip().split() ]

#     grid = []
#     for i in xrange(0, r):
#         grid.append(raw_input().strip())
#     #print "INPUT TAKEN"
#     dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)







