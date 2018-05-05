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
#
#         probe_obj=probe.Probe(row)
#         probe_data.append(probe_obj)
#         x.append(probe_obj.longitude)
#         y.append(probe_obj.latitude)
#
#         print 'No=',i,'latitude=',probe_obj.latitude,'longitude=', probe_obj.longitude
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
    i=0
    for row in spamreader:
        # print 'row_length=',row[16]
        link_obj=link.Link(row)


        for shape_point in link_obj.shape_points:
            x.append(shape_point.longitude)
            y.append(shape_point.latitude)
            print 'No=',i,'latitude=', shape_point.latitude, 'longitude=', shape_point.longitude

       #For displaying nodes only
        # x.append(link_obj.reference_node.longitude)
        # y.append(link_obj.reference_node.latitude)
        # print 'No=', i, 'latitude=', link_obj.reference_node.latitude, 'longitude=', link_obj.reference_node.longitude
        #
        # x.append(link_obj.non_reference_node.longitude)
        # y.append(link_obj.non_reference_node.latitude)
        # print 'No=', i, 'latitude=', link_obj.non_reference_node.latitude, 'longitude=', link_obj.non_reference_node.longitude

        i=i+1
        link_data.append(link_obj)

plt.scatter(x,y)
plt.show()
