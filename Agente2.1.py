import csv
class Agente():
    def __init__(self, *args, **kwargs):
        self.solution = args[1]
        self.opencsv(args[2])
        print(self.breadthFirstSearch(args[0]))
        

    maps = []

    def opencsv(self,maps):
        with open('maps.csv', 'r', newline='') as csvfile:
            spamreader = csv.DictReader(csvfile)
            for row in spamreader:
                self.maps.append([row['current'],row['goal'],int(row['distance'])])

    def childNode(self,problem,parent,coast):
        node = {
            'state': problem,
            'parent': parent,
            'coast': coast
        }
        return node

    def goalTest(self,state):
        if state == self.solution:

            return True
        else:
            return False

    def breadthFirstSearch(self,problem):
        coast = 0
        frontier = []
        explored = []
        node = self.childNode(problem,None,0)
        if self.goalTest(node['state']):
            return node['state'] +" custo:"+ str(coast + node['coast'])    
        frontier.append(node)

        while True:
            if len(frontier) is 0:
                return False
            front = frontier.pop(0)
            explored.append(front['state'])
            possibilities = list(filter(lambda opt: opt[0] == front['state'], self.maps))
            for possibiliti in possibilities:
                node = self.childNode(possibiliti[1],front,possibiliti[2]+front['coast'])
                if node not in frontier:
                    if node not in explored:
                        if self.goalTest(node['state']):
                            frontier.append(node)
                            return frontier[len(frontier) - 1]
                        frontier.append(node)
                        
Agente('oradea','iasi','maps.csv')