"""
V1.0
"""
from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search

#______________________________________________________________________________
# Steven Richter
# An implementation of the Jugs problem.
# Tuple format = [<Node (X_Current_Capacity, Y_Current_Capacity)>]
# State is a tuple (XCC, YCC) with initial value (0,0).
# Actions consist of filling jug X, filling jug Y,
# emptying jug X, emptying jug Y, and finally swapping
# amounts of water between jugs.

class Jug(Problem):
    X_CAPACITY = 4; Y_CAPACITY = 9
    XCC = 0 # index of X jug
    YCC = 1 # index of Y jug
    
    def __init__(self, initState,goalState):
    	Problem.__init__(self, initState, goalState)
    
    def actions(self, state):
        #actions are simply the result states possible in this example
        list=[]

        # if X not full, fill with Y until X full
        if state[Jug.XCC] < Jug.X_CAPACITY and state[Jug.YCC] > 0:
            x = state[Jug.XCC]
            y = state[Jug.YCC] 
            while (y > 0 and x < Jug.X_CAPACITY):
                x += 1
                y -= 1
            newstate = (x,y)
            if self.validate(newstate):
                list.append(newstate)

        # if Y not full, fill with X until Y full
        if state[Jug.YCC] < Jug.Y_CAPACITY and state[Jug.XCC] > 0:
            x = state[Jug.XCC]
            y = state[Jug.YCC]
            while (x > 0 and y < Jug.Y_CAPACITY):
                y += 1
                x -= 1
            newstate = (x,y)
            if self.validate(newstate):
                list.append(newstate)

        # if X empty, fill with spout
        if state[Jug.XCC] == 0:
            newstate = (state[Jug.XCC] + Jug.X_CAPACITY, state[Jug.YCC])
            if self.validate(newstate):
                list.append(newstate)

        # if Y empty, fill with spout
        if state[Jug.YCC] == 0:
            newstate = (state[Jug.XCC], state[Jug.YCC] + Jug.Y_CAPACITY)
            if self.validate(newstate):
                list.append(newstate)

        # if X full, dump on ground
        if state[Jug.XCC] == Jug.X_CAPACITY:
            newstate = (0, state[Jug.YCC])
            if self.validate(newstate):
                list.append(newstate)
        
        # if Y full, dump on ground
        if state[Jug.YCC] == Jug.Y_CAPACITY:
            newstate = (state[Jug.XCC], 0)
            if self.validate(newstate):
                list.append(newstate)

        return list

    def validate(self, state):
        # verify x_current_cap < x_capacity
        if state[Jug.XCC] > Jug.X_CAPACITY:
            return False

        # verify X_current_cap >= 0
        if state[Jug.XCC] < 0:
            return False
        
        # verify YCC < Y_CAP
        if state[Jug.YCC] > Jug.Y_CAPACITY:
            return False

        # verify YCC >= 0
        if state[Jug.YCC] < 0:
            return False

        return True  
        
    def result(self, state, action):
        return action #since states are so lightweight, the action is itself the new state

def main():
    print('Jugs Problem: ')
    print(' Tuples are in this format --> [<Node (X_Current_Capacity, Y_Current_Capacity)>]')
    initState = (0,0)
    goalState = (0,6)

    problem = Jug(initState, goalState)
    goal = breadth_first_search(problem)
    print("\nPath = ",goal.path(),"\n\nPath cost = ",goal.path_cost)
    print()

main()