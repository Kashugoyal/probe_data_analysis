import csv
import numpy as np
import matplotlib.pyplot as plt
import probe
import link

x=[]
y=[]
#
# x1=[]
# y1=[]

probe_data=[]
link_data=[]

#reading Probe Data
# with open('Partition6467ProbePoints.csv', 'rb') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     i=0
#     for row in spamreader:
#
#         probe_obj=probe.Probe(row)
#         probe_data.append(probe)
#         x.append(probe_obj.longitude)
#         y.append(probe_obj.latitude)
#
#         print probe_obj.latitude
#         print 'latitude=',probe_obj.latitude,'longitude=', probe_obj.longitude
#         i=i+1
#         # if i>10000:
#         #     break
#         # print '\n'
#
# plt.scatter(x,y)
# plt.show()

#reading Link Data
with open('Partition6467LinkData.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        link_obj=link.Link(row)
        link_data.append(link)
        print link_obj.length


print 'Hello'
