
from PathSolver import *
import numpy as np

#                    gauche           droite          haut             bas
directions=[np.array([-1,0]),np.array([1,0]),np.array([0,-1]),np.array([0,1])]

def getIndexFromCoord(l):
    y,x=l
    return y*16+x


class RobotProblem:

    def nextStates(self,s,b):
        # Inputs: list containing the coordinate of the empty cell and the cell values
        p,r1,r2,r3,r4,t=s
        
        
        # ns: next states
        ns=[]
        
        robots = [r1,r2,r3,r4]
        i=0

        for r in robots:
            for d in directions:
                for x in range(256):
                    new_placement=r+d*x
                    new_index=getIndexFromCoord(new_placement)
                    if new_placement in b[new_index]:
                        
                        new_robots = robots
                        
                        new_robots[i]=new_placement
                        
                        
                        ns.append([p, new_robots[0], new_robots[1], new_robots[2], new_robots[3],t])
                        break
            i=i+1

        return ns


rp=RobotProblem()

#initial_state= ---à générer:[Player, Robot1, Robot2, Robot3, Robot4, Target]
#final_state=   ---à générer:[Player, Robot1, Robot2, Robot3, Robot4, Target] 
#--ex:
initial_state=[2,[4,4],[4,12],[12,12],[12,4],[12,15]]
#--ex:
final_state=[2,[4,4],[12,15],[12,12],[12,4],[12,15]]


#board= ---à générer:[[[0,1]],[[0,-1],[1,0]],......] ---représenter les 256 cases, chaque case contient la liste des directions bloquées


BFS(rp,initial_state,final_state,board,occurence_test=False)
BFS(rp,initial_state,final_state,board)
