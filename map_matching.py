#! /usr/bin/env python
import csv
import numpy as np
import matplotlib.pyplot as plt
import probe
import link
from shapely.geometry import LineString as line, Point as point

x=[]
y=[]
#
# x1=[]
# y1=[]

probe_data=[]
link_data=[]


dist=[]
link_id = []






def read_probe():
  #reading Probe Data
    print 'reading probe points ...'
    with open('Partition6467ProbePoints.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i=0
        for row in spamreader:
            probe_obj=probe.Probe(row)
            probe_data.append(probe_obj)
            # x.append(probe_obj.longitude)
            # y.append(probe_obj.latitude)

            # print 'No=',i,'latitude=',probe_obj.latitude,'longitude=', probe_obj.longitude
            i=i+1
            if i>1000:
                break
            # print '\n'

    # plt.scatter(x,y)
    # plt.show()



def read_link():
    #reading Link Data
  print 'reading link data ...'
  with open('Partition6467LinkData.csv', 'rb') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
      i=0
      for row in spamreader:
          # print 'row_length=',row[16]
          link_obj=link.Link(row)


          # for shape_point in link_obj.shape_points:
          #     x.append(shape_point.longitude)
          #     y.append(shape_point.latitude)
          #     print 'No=',i,'latitude=', shape_point.latitude, 'longitude=', shape_point.longitude

         #For displaying nodes only
          # x.append(link_obj.reference_node.longitude)
          # y.append(link_obj.reference_node.latitude)
          # print 'No=', i, 'latitude=', link_obj.reference_node.latitude, 'longitude=', link_obj.reference_node.longitude
          #
          # x.append(link_obj.non_reference_node.longitude)
          # y.append(link_obj.non_reference_node.latitude)
          # print 'No=', i, 'latitude=', link_obj.non_reference_node.latitude, 'longitude=', link_obj.non_reference_node.longitude

          i=i+1
          # print type(link_obj.reference_node.latitude)
          link_data.append(link_obj)


def distance(p_x, p_y, line):
  # l = line([(1, 1), (-1,1)])
  p = point(p_x,p_y)
  return p.distance(line)


def search_link():

  # for item in link_data:
  #     if abs(item.reference_node.latitude - probe_data[200].latitude) < 0.1 and abs(item.reference_node.longitude - probe_data[200].longitude) < 0.1:
  #       l = line([(item.reference_node.latitude, item.reference_node.longitude), (item.non_reference_node.latitude, item.non_reference_node.longitude)])
  #       dist.append(distance(probe_data[200].latitude, probe_data[200].longitude, l))
  #       link_id.append(item.linkPVID)
  #     else:
  #       continue


  for item in link_data:
    flag = 0
    line_points=[]
    for pt in item.shape_points:
      if abs(pt.latitude - probe_data[200].latitude) < 0.01 and abs(pt.longitude - probe_data[200].longitude) < 0.01:
        flag = 1
      else:
        continue
    if flag!=0:
      link_id.append(item.linkPVID)
      for pt in item.shape_points:
        line_points.append((pt.latitude,pt.longitude))
      link_line = line(line_points)
      dist.append(distance(probe_data[200].latitude, probe_data[200].longitude, link_line))
    else:
      continue
  # return link_id, dist



def main():
  read_probe()
  read_link()

  print 'The number of links is ' ,len(link_data)
  print max(item.length for item in link_data)
  print min(item.length for item in link_data)
  # print sorted(item2.length for item2 in link_data)[-10:]
  print probe_data[200].latitude, probe_data[200].longitude


  search_link()


  print len(link_id), len(dist)
  out = sorted(zip(link_id,dist), key=lambda x:x[1])
  for x,y in out:
    print x,y
    # print item
  # for idd, dis  in zip(link_id, dist):
    # print idd, dis

  # plt.scatter(x,y)
  # plt.show()


if __name__=="__main__":
  main()