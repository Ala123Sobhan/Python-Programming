"""
import header.py and all its functions
"""
import header
from header import *

def do_hill_climbing(tweak_function = shuffle_function):
    """
    Runs hill climmbing algorithm
    Keyword argument:
    tweak_function- the tweaking function you want to use- it can be swap_function(default) or shuffle_function
    returns solution state and its fitnes
    """
    #Initialization step
    current_fitness = None
    current = generate_random_permutation()
    iteration = 200 #number of iterations, you can change it

    while(iteration>=0):
        iteration -=1
        current_fitness = fitness_function(current) #calculating fitness
        #print('current',current, current_fitness)
        if current_fitness == 28:
            break
        #Modification step
        #generates next step and calculates fitness
        neighbour = generate_next_state(current,tweak_function)
        neighbour_fitness = fitness_function(neighbour)
        #print('neighbour',neighbour, neighbour_fitness)
        if current_fitness < neighbour_fitness:
            #print("assigning")
            current = neighbour

    return current,current_fitness

if __name__ == "__main__":

    random.seed()
    print("Solving 5 queen 3 rook problem")
    
    #You can use shuffle_function instead of swap_function
    solution, fitness = (do_hill_climbing(shuffle_function))
    print("Solution using Hill Climbing")
    printBoard(solution)
    print("Fitness is ",fitness)
    
