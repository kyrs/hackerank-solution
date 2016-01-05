""" Coded by Kumar shubham """
""" Date 5-January 2016 """
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

                
    def PathToPrincess(self, BotCoordinate, PrincessCoordinate):
        Journey = []

        BotX = BotCoordinate[0]
        BotY = BotCoordinate[1]

        PrincessY = PrincessCoordinate[0]
        PrincessX = PrincessCoordinate[1]

        #Xdepth = BotX-PrincessX
        #Ydepth = BotY-PrincessY

        if (PrincessX>0):
            TurnHoriz = "LEFT"
        else :
            TurnHoriz = "RIGHT"


        if (PrincessY>0):
            TurnVert = "UP"
        else:
            TurnVert = "DOWN"


        for turns in xrange(0,abs(PrincessX)):
            Journey.append(TurnVert)

        for turns in xrange(0,abs(PrincessY)):
            Journey.append(TurnHoriz)


        return "\n".join(Journey)




def displayPathtoPrincess(n,grid):
#print all the moves here
    Matrix = SavePrincess(n,grid)
    CorrectFlag = Matrix.ValidMatrix()
    if not CorrectFlag:
        Exception("Grid Input is Wrong")
    else:
        BotPosition = Matrix.BotCoordinate()
        PrincessPosition = Matrix.PrincessCoordinate()
        #print BotPosition, PrincessPosition

        ## Changing the coordinate wrt to BOT
        PrincessPosition[0] = BotPosition[0]-PrincessPosition[0]
        PrincessPosition[1] = BotPosition[1]-PrincessPosition[1]
        BotPosition = [0,0]
        #print BotPosition, PrincessPosition
        print Matrix.PathToPrincess(BotPosition,PrincessPosition)       


m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
