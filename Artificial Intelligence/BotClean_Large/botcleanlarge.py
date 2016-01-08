#!/usr/bin/python

""" Coded by Kumar Shuvham
    Date 8 -January 2015
                        """

class Bot(object):
    
    def __init__(self,size,position, board) :
        self.size = size
        self.botPosition = position
        self.board = board
        self.noDirt = None
        self. dirtCoord = None
        self.nearestDirt = None
        self.dirtMarker = "d"

    def validRow(self):
        return (self.size[0]==len(self.board))

    def validColumn(self):
        for i ,row in enumerate(self.board):
            if not (self.size[1]==len(row)):
                Exception("Column mis match !!")
        return True

    def validMatrix(self):

        return (self.validRow() and self.validColumn())

    def coordinate (self,marker):
        coordinateList =[]

        for i, row in enumerate(self.board):
            for j , col in enumerate(row):
                if col == marker:
                    coordinateList.append([i,j])
                else:
                    continue

        return coordinateList

    def nearestCoordinate(self,point, coordList):

        ## following code is written for relative position of the coordinates
        distanceDist = {abs(temp[0])+ abs(temp[1]):i for i, temp in enumerate(coordList)}
        minDist = min(distanceDist.keys())
        #print distanceDist
        indexMin = distanceDist[minDist]

        return coordList[indexMin]
        

    def relativecoordinate(self,botCoordinate,dirtCoordList):
        ## calculating the relative distance of the different cooordinte
        listRelativeDirt = [[botCoordinate[0]-dirt[0],botCoordinate[1]-dirt[1]] for dirt in dirtCoordList]
        return listRelativeDirt


    def move(self,botCoordinate,DirtCoordinate):
        ## code for computing the next move based on the current coordinate of the bot]
        nearestPoint = self.nearestCoordinate(botCoordinate,DirtCoordinate)

        dirtY = nearestPoint[0]
        dirtX = nearestPoint[1]

        if ([0,0] == nearestPoint):
            return "CLEAN"
        else:
            PathDistance = [abs(dirtX),abs(dirtY)]
            PathChoose = min(PathDistance)

            IndexMinPath = PathDistance.index(PathChoose)

            if (PathChoose == 0):
                IndexMinPath = not IndexMinPath


            if IndexMinPath == False :
                if (dirtX>0):
                    Turn = "LEFT"
                else :
                    Turn = "RIGHT"

            if IndexMinPath== True :
                if (dirtY>0):
                    Turn = "UP"
                else:
                    Turn = "DOWN"

            return Turn






def next_move(posr, posc, dimh, dimw, board):
    ## function to find the next move in the game
    wallECoord = [posr,posc]
    boardDim = [dimh,dimw]
    wallE = Bot(boardDim,wallECoord, board)
    dirtCoordinateList = wallE.coordinate(wallE.dirtMarker)
    wallERelative =  wallE.relativecoordinate(wallECoord,dirtCoordinateList)
    wallEMove = wallE.move(wallECoord,wallERelative)
    print wallEMove




if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    dim = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
