import csv
import numpy as np
import matplotlib.pyplot as plt

x=[]
y=[]

x1=[]
y1=[]

with open('Partition6467ProbePoints.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        x.append(row[3])
        y.append(row[4])
        print 'latitude=',row[3],'longitude=', row[4]
        # print '\n'

plt.scatter(x, y)
plt.show()

with open('Partition6467LinkData.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        x.append(row[3])
        y.append(row[4])
        print 'latitude=',row[3],'longitude=', row[4]
