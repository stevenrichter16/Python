from search import Problem
from utils import probability, argmax, weighted_sample_with_replacement
import random
#DESCRIBE YOUR ALGORITHM SPECIFICS HERE: Part B.3
#______________________________________________________________________________
#Genetic algorithms

def genetic_search(problem, fitness_fn, ngen=1000, pmut=0.1):
    """Call genetic_algorithm on the appropriate parts of a problem.
    This requires the problem to have states that can mate and mutate,
    plus a value method that scores states.
    """
    s = problem.initial
    states = [problem.result(s, a) for a in problem.actions(s)]
    random.shuffle(states)
    return genetic_algorithm(states, problem.value, ngen, pmut)
    
def genetic_algorithm(population, fitness_fn, ngen=1000, pmut=0.1):
    highest = 0
    highestEvolved = None
    for i in range(ngen):
        new_population = []
        for j in range(len(population)):
            fitnesses = map(fitness_fn, population)
            
            p1, p2 = weighted_sample_with_replacement(population, fitnesses, 2)
            child = p1.mate(p2)
            if random.uniform(0, 1) < pmut:
                child.mutate()
            new_population.append(child)
        population = new_population
        
        #Check and keep track of max; not necessarily pure GA
        #Add i and n returned
        currentEvolved = argmax(population, fitness_fn)
        currentHigh = fitness_fn(currentEvolved)
        if currentHigh > highest:    
            highest = currentHigh
            highestEvolved = currentEvolved
    return highestEvolved   
     
class GAState:
    "Abstract class for individuals in a genetic search."
    def __init__(self, genes):
        self.genes = genes

    def mate(self, other):
        "Return a new individual crossing self and other."
        c = random.randrange(len(self.genes))
        return self.__class__(self.genes[:c] + other.genes[c:])

    def mutate(self):
        "Change a few of my genes."
        abstract

    def __repr__(self):
        return "%s" % (self.genes,)
    
    #override if this is not what you want
    def __eq__(self,other):
        return isinstance(other, GAState) and self.genes == other.genes

#______________________________________________________________________________
#ExampleProblem and ExampleState
class ExampleState(GAState):
    '''
    Example that does really nothing; just illustrates the process
    '''
    def __init__(self, genes):
        GAState.__init__(self, genes)

    def mutate(self):
        #flip a random bit
        c = random.randrange(len(self.genes))
        self.genes[c] = 1 - self.genes[c]

class ExampleProblem(Problem):
    '''
    An example problem with a list of bits as a list
    '''
    def __init__(self, init):
        self.initial = init

    def actions(self, state):
        '''
        Generate randomly flip one bit; do this twice to generate 2 neighbors
        Actions are just the genes
        '''
        choices=[]
        for i in range(2):
            candidate = list(state.genes)
            c = random.randrange(len(candidate))
            if probability(0.5):
                candidate[c] = 1 - candidate[c]
            choices.append(candidate)           
        return choices
    
    def result(self, state, action):
        ''' Wrap the action genes in an ExampleState and return that'''
        return ExampleState(action)

    def value(self, state):
        '''
            Simply counts number of 1's and returns 1 + that value; 
            We want to avoid  fitnesses of 0 always.
        '''
        return state.genes.count(1) + 1

         
#______________________________________________________________________________   
def main():
    
    # initialize population
    population = []
    ordered = [i for i in range(26)]
    population.append(ordered)
    for i in range(9):
        x = [i for i in ordered]
        random.shuffle(x)
        population.append(x)


    f = open(r'')
    cities = []
    for i in f.readlines():
        cities.append(i.strip())

    

    gp = ExampleProblem(ExampleState(population)) 
    goal = genetic_search(gp, ExampleProblem.value, ngen=100, pmut=0.1)
    #print("Goal = ",goal)    
   

main()