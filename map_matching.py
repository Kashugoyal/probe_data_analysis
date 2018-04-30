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
        # x.append(row[14])
        # y.append(row[4])
        a=  row[14].split("|")
        # print a.split(",")

        for lalo in a:
            x1.append(lalo.split("/")[0])
            y1.append(lalo.split("/")[1])
            print lalo.split("/")[0],lalo.split("/")[1]
plt.scatter(x, y)
plt.show()
