import csv
import time
from problem.Problem import Problem
class Agente():
    def __init__(self, *args, **kwargs):
        self.problem = Problem(args[0],args[1],args[2])
        print(' ')
        print(self.breadthFirstSearch(self.problem))    

    def childNode(self,problem,parent,coast):
        node = {
            'state': problem,
            'parent': parent,
            'coast': coast
        }
        return node

    def breadthFirstSearch(self,problem):
        coast = 0
        frontier = []
        explored = []
        node = self.childNode(problem.initialState,None,0)
        if problem.goalTest(node['state']):
            return node['state'] +" custo:"+ str(coast + node['coast'])    
        frontier.append(node)

        while True:
            if len(frontier) is 0:
                return False
            front = frontier.pop(0)
            explored.append(front['state'])
            for possibiliti in problem.actions(front['state']):
                node = self.childNode(possibiliti[1],front,possibiliti[2]+front['coast'])
                if node not in frontier or node not in explored:
                    if problem.goalTest(node['state']):
                        frontier.append(node)
                        return frontier[len(frontier) - 1]
                    frontier.append(node)
inicio = time.time()
Agente('arad','bucharest','maps.csv')
fim = time.time()
print(fim - inicio)