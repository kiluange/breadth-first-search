import csv

map = []

with open('maps.csv', 'r', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        map.append([row['current'],row['goal'],int(row['distance'])])
        print(map)