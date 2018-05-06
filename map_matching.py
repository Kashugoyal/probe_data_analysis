#! /usr/bin/env python
import csv
import numpy as np
import matplotlib.pyplot as plt
import probe
import link
import link_dist
from shapely.geometry import LineString as line, Point as point

x=[]
y=[]
#
# x1=[]
# y1=[]

probe_data=[]
link_data=[]








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


def distance(p_x, p_y, line_points):
  # l = line([(1, 1), (-1,1)])
  link_line = line(line_points)
  p = point(p_x,p_y)
  return p.distance(link_line)


def search_link(num, precision = 0.01):
  '''
  arguments
   num: The probe_data point in the probe_data array.
   precision: size of the filter box, 2nd decimal places corresponds to around 1 Km 
  This function takes in one probe point and does the following:
   1. Taking one link at a time, it filters out the links whose shape points are not within a specified range
   2. For the selected ink, it buils a linear approximation, considering all shape points and calculates the
   minimum distance of the probe point from the link. 
   3. The link ID and the distance from that link is stored in respective arrays.
  Call this function recusrsively to evaluate multiple probe points.
  '''
  dist=[]
  link_id = []
  for item in link_data:
    flag = 0
    line_points=[]
    for pt in item.shape_points:
      if abs(pt.latitude - probe_data[num].latitude) < precision and abs(pt.longitude - probe_data[num].longitude) < precision:
        flag = 1
      else:
        continue
    if flag!=0:
      link_id.append(item.linkPVID)
      for pt in item.shape_points:
        line_points.append((pt.latitude,pt.longitude))
      dist.append(distance(probe_data[num].latitude, probe_data[num].longitude, line_points))
    else:
      continue
  out = sorted(zip(link_id,dist), key=lambda x:x[1])
  probe_data[num].update_link_info(out)
  return out



def main():
  read_probe()
  read_link()

  print 'The number of links is ' ,len(link_data)
  print max(item.length for item in link_data)
  print min(item.length for item in link_data)
  print probe_data[200].latitude, probe_data[200].longitude

  out = search_link(200)

  print len(out)
  
  # for x,y in out:
    # print x,y
    # print item
  # for idd, dis  in zip(link_id, dist):
    # print idd, dis

  # plt.scatter(x,y)
  # plt.show()


if __name__=="__main__":
  main()