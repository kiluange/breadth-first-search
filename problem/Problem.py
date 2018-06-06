import csv

class Problem(object):
    def __init__(self, *args, **kwargs):
        self.initialState = args[0]
        self.finalState = args[1]
        self.filemap = args[2]
        #open map
        self.opencsv(self.filemap)
        pass

    maps = []

    def opencsv(self,maps):
        with open('maps.csv', 'r', newline='') as csvfile:
            spamreader = csv.DictReader(csvfile)
            for row in spamreader:
                self.maps.append([row['current'],row['goal'],int(row['distance'])])
    
    def goalTest(self, state):
        if state == self.finalState:

            return True
        else:
            return False
        pass
    
    def actions(self, state):
        possibilities = list(filter(lambda opt: opt[0] == state, self.maps))
        print(possibilities)
        return possibilities

        