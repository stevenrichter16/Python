"""
V1.0
"""
from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search

#______________________________________________________________________________
# Steven Richter
# An implementation of the Frog Jumping Problem
# Tuple format = [<Node (rock1, rock2, rock3, rock4, rock5, rock6)>]
# State is a tuple(rock1, rock2, rock3, rock4, rock5, rock6) with initial value (1,1,1,0,2,2,2).
# 1's represent green frogs, 2's represent red frogs, and 0 represents no frog.
# Actions consist of moving either a green or red frog to a no frog rock,
# based on where the no frog rock is.  

class Frog(Problem):
    def __init__(self, initState,goalState):
    	Problem.__init__(self, initState, goalState)

    def actions(self, state):
        #actions are simply the result states possible in this example
        list=[]
        
        # get index of blank
        _index = state.index(0)
        
        # if index of empty is 0
        if _index == 0:
            if state[_index + 1] == 2: # _2x
                newState = swap(_index, _index+1, [x for x in state])
                if self.validate(newState):
                    list.append(newState)

            if state[_index + 2] == 2:
                newState = swap(_index, _index+2, [x for x in state])
                if self.validate(newState):
                    list.append(newState)

        # if index of empty is 1
        if _index == 1:
            if state[_index-1] == 1: # 1_x
                newState = swap(_index, _index-1, [x for x in state])
                if self.validate(newState):
                    list.append(newState)

            if state[_index+1] == 2: # x_2
                newState = swap(_index, _index+1, [x for x in state])
                if self.validate(newState):
                    list.append(newState)
            
            if state[_index+2] == 2: # x_x2
                newState = swap(_index, _index+2, [x for x in state])
                if self.validate(newState):
                    list.append(newState)

        # if index of empty is 2,3,4
        if _index == 2 or _index == 3 or _index == 4:
            for i in range(_index-2, _index):
                if state[i] == 1: # 11_xx
                    newState = swap(_index, i, [x for x in state])
                    if self.validate(newState):
                        list.append(newState)

            for i in range(_index+1, _index+3):
                try:
                    if state[i] == 2: # xx_22
                        newState = swap(_index, i, [x for x in state])
                        if self.validate(newState):
                            list.append(newState)
                except IndexError:
                    continue


        # if index of empty is 5
        if _index == 5:
            for i in range(_index-2, _index):
                if state[i] == 1: # ...x11_x
                    newState = swap(_index, i, [x for x in state])
                    if self.validate(newState):
                        list.append(newState)

            if state[_index+1] == 2: # ...xx_2
                newState = swap(_index, _index+1, [x for x in state])
                if self.validate(newState):
                    list.append(newState)

        
        # if index of empty is 6
        if _index == 6:
            if state[_index-1] == 1: # ...1_
                newState = swap(_index, _index-1, [x for x in state])
                if self.validate(newState):
                    list.append(newState)
        return list

    def validate(self, state):
        if 0 not in state:
            return False
        else:
            return True
        
    def result(self, state, action):
        return action #since states are so lightweight, the action is itself the new state

def checkRight(right, row_index, col_index, g):
    if right is ' ':
        g[(row_index,col_index)][(row_index,col_index + 1)] = 1
    elif right is 'G':
        g[(row_index,col_index)][(row_index,col_index + 1)] = 1
    else:
        g[(row_index,col_index)][(row_index,col_index + 1)] = right
    return g

def checkBelow(below, row_index, col_index, g):
    if below is ' ':
        g[(row_index,col_index)][(row_index + 1,col_index)] = 1
    elif below is 'G':
        g[(row_index,col_index)][(row_index + 1,col_index)] = 1
    else:
        g[(row_index,col_index)][(row_index + 1,col_index)] = below
    return g

def main():
    #Runs the Cannibals and Missionary problem, will provide a solution to getting all missionaries
    #and all cannibals to the other side, without missionaries ever being outnumbered by cannibals
    #on either side.
    #print('Missionaries/Cannibals Problem: ')
    #print(' Tuples are in this format --> [<Node (leftMissionaries, rightMissionaries, leftCannibals, rightCannibals, boatSide)>]')

    f = open(r'')
    lines = [i.strip() for i in f]
    g = {}
    for row_index,i in enumerate(lines):
        for col_index,cell in enumerate(i):
            if cell is not 'B':

                # if key doesn't exist in g yet
                if (row_index,col_index) not in g and cell is not 'G':
                    g[(row_index,col_index)] = {}

                # if cell is on bottom row 
                if row_index == len(lines) and col_index != len(i):
                    checkRight(right, row_index, col_index, g)
                
                elif col_index == len(i):
                    checkBelow(below, row_index, col_index, g)

                elif row_index == len(lines) and col_index == len(i):
                    print("AT GOAL")
                
                else:
                    right = lines[row_index][col_index + 1];
                    below = lines[row_index + 1][col_index];
                    if right is not 'B':
                        g = checkRight(right, row_index, col_index, g)
                    if below is not 'B':
                        g = checkBelow(below, row_index, col_index, g)
    print(g)

main()


