map = []
map.append(['oradea','zerind',71])
map.append(['oradea','sibiu',151])
map.append(['zerind','oradea',71])
map.append(['zerind','arad',75])
map.append(['arad','zerind',75])
map.append(['arad','sibiu',140])
map.append(['arad','timisoara',118])
map.append(['timisoara','arad',118])
map.append(['timisoara','lugoj',111])
map.append(['lugoj','timisoara',111])
map.append(['lugoj','mehadia',70])
map.append(['mahadia','lugoj',70])
map.append(['mehadia','dobreta',75])
map.append(['dobreta','mehadia',75])
map.append(['dobreta','craiova',120])
map.append(['craiova','dobreta',120])
map.append(['craiova','rimnicu vilcea',146])
map.append(['craiova','pitesti',138])
map.append(['rimnicu vilcea','craiova',146])
map.append(['rimnicu vilcea','pitesti',97])
map.append(['rimnicu vilcea','sibiu',80])
map.append(['sibiu','rimnicu vilcea',80])
map.append(['sibiu','fagaras',99])
map.append(['sibiu','oradea',151])
map.append(['sibiu','arad',140])
map.append(['pitesti','craiova',138])
map.append(['pitesti','rimnicu vilcea',97])
map.append(['pitesti','bucharest',101])
map.append(['fagaras','sibiu',99])
map.append(['fagaras','bucharest',211])
map.append(['bucharest','fagaras',211])
map.append(['bucharest','pitesti',101])
map.append(['bucharest','giurgiu',90])
map.append(['giurgiu','bucharest',90])
map.append(['bucharest','urziceni',85])
map.append(['urziceni','bucharest',85])
map.append(['urziceni','hirsova',98])
map.append(['hirsova','urziceni',98])
map.append(['urziceni','vaslui',142])
map.append(['vaslui','urziceni',142])
map.append(['hirsova','eforie',86])
map.append(['vaslui','iasi',92])
map.append(['iasi','vaslui',92])
map.append(['iasi','neamt',87])
map.append(['neamt','iasi',87])

solution = ''

def childNode(problem,parent,coast):
    node = {
        'state': problem,
        'parent': parent,
        'coast': coast
    }
    return node
def goalTest(state):
    if state == solution:

        return True
    else:
        return False

def breadthFirstSearch(problem):
    coast = 0
    frontier = []
    explored = []
    node = childNode(problem,None,0)
    if goalTest(node['state']):
        return node['state'] +" custo:"+ str(coast + node['coast'])    
    frontier.append(node)

    while True:
        if len(frontier) is 0:
            return False
        front = frontier.pop(0)
        explored.append(front['state'])
        possibilities = list(filter(lambda opt: opt[0] == front['state'], map))
        for possibiliti in possibilities:
            node = childNode(possibiliti[1],front,possibiliti[2]+front['coast'])
            if node not in frontier:
                if node not in explored:
                    if goalTest(node['state']):
                        frontier.append(node)
                        return frontier[len(frontier) - 1]
                    frontier.append(node)

solution = 'bucharest'
print(breadthFirstSearch('arad'))