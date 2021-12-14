

class Node:
    
    def __init__(self,state,father):
        self.State=state
        self.Father=father
        
    def __repr__(self):
        return str(self.State)


def getPathFrom(e):
    l=[e.State]
    while e.Father:
        e=e.Father
        l.insert(0,e.State)
    return l


def BFS(pp,initial_state,final_state,board,occurence_test=True):
    OL=[Node(initial_state,None)]
    CL=[]
    n=0
    while OL:
        e=OL.pop(0)
        if e.State[e.State[0]]==e.State[5]:             #check final state
            print(getPathFrom(e), 'extending', n, 'nodes')
            break
        else:
            next_states=pp.nextStates(e.State,board)
            for s in next_states:
                if not occurence_test or s not in CL:
                    n+=1
                    node=Node(s,e)
                    OL.append(node)
                    if occurence_test:
                        CL.append(s)


