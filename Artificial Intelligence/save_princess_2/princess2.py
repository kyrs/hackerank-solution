''' Coded by Kumar Shubham
    Date : 6-Jan-2016'''




#!/bin/python

class SavePrincess(object):
    
    def __init__(self,m, grid):
        self.SizeMatrix = m
        self.GridMatrix = grid 
        self.PrincessCordinate = None
        self.BotCordinate = None
        self.PrincessMarker = "p"
        self.BotMarker = "m"
    
    def ValidRow(self):
        return self.SizeMatrix == len(self.GridMatrix)

    
    def ValidCol(self):
        CorrectFlag =True

        for row in self.GridMatrix:
            if not len(row) == self.SizeMatrix:
                Exception("Wrong column !!")
                CorrectFlag = False
                break

        return CorrectFlag



    def ValidMatrix(self):
        RowValid = self.ValidRow()
        ColumnValid = self.ValidCol()
        return (RowValid and ColumnValid)

    
    def FindCoordinate(self, marker) :
        CoordPoint =[]
        for i,row in enumerate(self.GridMatrix):
            for j,col in enumerate(row):
                if col == marker :
                    CoordPoint = [i,j]

        if len(CoordPoint) == 0 :
            Exception("%s Marker not Found "%(marker))

        return CoordPoint


    

    def PrincessCoordinate(self):
        return self.FindCoordinate(self.PrincessMarker)

    

    def BotCoordinate(self):
        return self.FindCoordinate(self.BotMarker)



def nextMove(n,r,c,grid):
    Grid = SavePrincess(n,grid)
    Grid.BotCoordinate = [r,c]
    BotPosition = [r,c]
    if not Grid.ValidMatrix() :
        Exception ("Matrix is invalid !!!")
    else:
        PrincessPosition = Grid.PrincessCoordinate()
        PrincessPosition[0] = BotPosition[0]-PrincessPosition[0]
        PrincessPosition[1] = BotPosition[1]-PrincessPosition[1]
        
        #BotPosition = [0,0]


        BotX = 0  
        BotY = 0

        PrincessY = PrincessPosition[0]
        PrincessX = PrincessPosition[1]

        #Xdepth = BotX-PrincessX
        #Ydepth = BotY-PrincessY
        PathDistance = [abs(PrincessX),abs(PrincessY)]
        PathChoose = min(PathDistance)

        IndexMinPath = PathDistance.index(PathChoose)

        if (PathChoose == 0):
            IndexMinPath = not IndexMinPath


        if IndexMinPath == False :
            if (PrincessX>0):
                Turn = "LEFT"
            else :
                Turn = "RIGHT"

        if IndexMinPath== True :
            if (PrincessY>0):
                Turn = "UP"
            else:
                Turn = "DOWN"

        return Turn            





n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)