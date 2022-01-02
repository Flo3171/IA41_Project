import Numpy as np


class Map:
    
    def __init__(self,playerBot):
        self._matrix=[]
        self._matrix=[[0 for i in range(15)] for j in range(15)]        # matrix full with 0
        self._directions = [np.array([0,1]),np.array([0,-1]),np.array([1,0]),np.array([-1,0])]  # down up right left
        self._playerBot = playerBot                 # Robot that must reach destination
        self._mapScore = 0                      # Less expensive path
        
    
    def addValue(self,i,j,moveCost):
        if self._matrix[i][j] == 0:
            self._matrix[i][j] = moveCost
        
        
    def addToMap(self,i,j,moveCost,board):
        for d in self._directions:
            for k in range(2,16):
                new_d_plus = d * k + np.array([i,j])
                new_d = d * (k-1) + np.array([i,j])
                new_i_plus,new_j_plus=list(new_d_plus)
                new_i,new_j=list(new_d)
                nextTo_i=0
                nextTo_j=0
                if d[0]==0:
                    nextTo_i=1
                else:
                    nextTo_j=1
                if new_i_plus>=0 and new_i_plus<=15 and new_j_plus>=0 and new_j_plus<=15:
                    if (board._cases[new_i,new_j]._bot == self._playerBot):
                        self.addValue(new_i,new_j,moveCost)
                        return moveCost
                    elif (board._cases[new_i,new_j]._walls != []) and (board._cases[new_i,new_j]._walls != [d]):
                        self.addValue(new_i,new_j,moveCost)
                        break
                    elif (board._cases[new_i + nextTo_i,new_j + nextTo_j]._bot != None) or (board._cases[new_i - nextTo_i,new_j - nextTo_j]._bot != None):
                        self.addValue(new_i,new_j,moveCost)
                        break
                    elif (board._cases[new_i,new_j]._walls != [d]) or (board._cases[new_i_plus,new_j_plus]._bot != None):
                        break
                elif new_i==0 or new_i==15 or new_j==0 or new_j==15:
                    if (board._cases[new_i,new_j]._bot == self._playerBot):
                        self.addValue(new_i,new_j,moveCost)
                        return moveCost
                    elif (board._cases[new_i,new_j]._walls != [d]) and (board._cases[new_i,new_j]._bot == None):
                        self.addValue(new_i,new_j,moveCost)
                        break
                    elif (board._cases[new_i + nextTo_i,new_j + nextTo_j]._bot != None) or (board._cases[new_i - nextTo_i,new_j - nextTo_j]._bot != None):
                        self.addValue(new_i,new_j,moveCost)
                        break
        return 0
        
                
    def generateMap(self,board):
        foundRobot = False
        moveCost = 1
        x = board._destination.coord().x()
        y = board._destination.coord().y()
        self.addValue(x,y,50)            #Value assigned to destination, that shouldn't be reached otherwise
        while (foundRobot == False):
            for i in range(15):
                for j in range(15):
                    if (self._matrix[i][j] == moveCost-1 and moveCost != 1) or (self._matrix == 50 and moveCost == 1):
                        a=self.addToMap(i,j,moveCost,board)
                        if (a!=0):
                            foundRobot=True
                            self._mapScore = a
            moveCost += 1
            
            
    def mapScore(self):
        return self._mapScore
        
        

        
                
            
            

        