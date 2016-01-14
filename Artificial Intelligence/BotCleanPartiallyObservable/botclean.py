#!/usr/bin/python

""" Coded by Kumar Shuvham
    Date 7 -January 2015
                        """
import pickle
import os

class Bot(object):
    
    def __init__(self,size,position, board) :
        self.size = size
        self.botPosition = position
        self.board = board
        self.noDirt = None
        self. dirtCoord = None
        self.nearestDirt = None
        self.dirtMarker = "d"
        self.unobserve = "o"
    def validRow(self):
        return (self.size==len(self.board))

    def validColumn(self):
        for i ,row in enumerate(self.board):
            if not (self.size==len(row)):
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






def next_move(posr, posc, board):
    ## function to find the next move in the game
    wallECoord = [posr,posc]
    wallE = Bot(len(board),wallECoord, board)
    dirtCoordinateList = wallE.coordinate(wallE.dirtMarker)
    if (len(dirtCoordinateList) ==0) :
        f = open('output.txt','rb')
        visitList = pickle.load(f)
        #print visitList
        f.close()
        if (len(visitList) !=0):
            coordinate = visitList[0]
            #print coordinate
            if(coordinate != wallECoord):
                dirtCoordinateList = [coordinate]
                #print coordinate,wallECoord
                wallERelative =  wallE.relativecoordinate(wallECoord,dirtCoordinateList)
                wallEMove = wallE.move(wallECoord,wallERelative)
                print wallEMove
                
            else:
                try:
                    coordinateNew = visitList[1]
                    visitList.pop(0)
                    f = open('output.txt','wb')
                    f.truncate()
                    pickle.dump(visitList, f)
                    f.close()
                    dirtCoordinateList = [coordinateNew]
                    wallERelative =  wallE.relativecoordinate(wallECoord,dirtCoordinateList)
                    wallEMove = wallE.move(wallECoord,wallERelative)
                    print wallEMove
                except Exception as e:
                    pass

                




        
    else:
        wallERelative =  wallE.relativecoordinate(wallECoord,dirtCoordinateList)
        wallEMove = wallE.move(wallECoord,wallERelative)
        print wallEMove





if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    
    if( not os.path.isfile('output.txt')):
        f = open('output.txt', 'wb')
        listVisit = [[1,1],[1,3],[3,1],[3,3]]
        pickle.dump(listVisit, f)
        f.close()
    
    next_move(pos[0], pos[1], board)
    