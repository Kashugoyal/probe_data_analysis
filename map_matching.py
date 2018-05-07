#! /usr/bin/env python
import csv
import numpy as np
import matplotlib.pyplot as plt
import probe
import link
import link_dist
from shapely.geometry import LineString as line, Point as point
import math
import matched_point
import pickle

x=[]
y=[]
#
# x1=[]
# y1=[]

probe_data=[]
link_data=[]
matched_data=[]



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
            if i>2000:
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


def search_link(num, precision = 0.001):
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
    links=[]
    for pt in item.shape_points:
      if abs(pt.latitude - probe_data[num].latitude) < precision and abs(pt.longitude - probe_data[num].longitude) < precision:
        flag = 1
      else:
        continue
    if flag!=0:
      link_id.append(item.linkPVID)
      links.append(item)
      for pt in item.shape_points:
        line_points.append((pt.latitude,pt.longitude))
      dist.append(distance(probe_data[num].latitude, probe_data[num].longitude, line_points))
    else:
      continue
  out = sorted(zip(link_id,dist), key=lambda x:x[1])
  probe_data[num].update_link_info(out)
  return out

def calculate_heading_diff(point, link):
    min=10000
    # plot_point_n_links(point, [link])

    heading=point.heading*1
    for angle in link.angles:
        diff= abs(angle-int(point.heading))
        if diff <min:
            min=diff
    return min

# plots a point with the given set of links for comparison
def plot_point_n_links(pnt,links):
    for link in links:
        lon = []
        lat = []
        for shapepoint in link.shape_points:

            lon.append(shapepoint.longitude)
            lat.append(shapepoint.latitude)
        plt.plot(lon, lat, 'ro-')
    plt.plot(pnt.longitude, pnt.latitude, 'ro-', color='blue')
    # plt.ylim(ymin=0)
    # plt.xlim(xmin=0)
    # plt.show()

def distance_calc(node1,node2):
    x1=node1.longitude
    x2=node2.longitude
    y1 = node1.latitude
    y2 = node2.latitude
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def main():
  read_probe()



  read_link()

  print 'The number of links is ' ,len(link_data)
  probe_data_length=len(probe_data)
  for probe_index in range(probe_data_length):
      print probe_index,'/',probe_data_length
      input_point=probe_data[probe_index]
      # print input_point.latitude, input_point.longitude

      out = search_link(probe_index)

      print len(out)

      links_plot=[]

      min=100000
      min_linkId=0
      min_link=link_data[0]
      for link_id,dist in out:
        link=next((x for x in link_data if x.linkPVID == link_id), None)
        links_plot.append(link)
        heading_diff=calculate_heading_diff(input_point,link)
        dscore=dist*100000
        hscore=heading_diff/10
        score=dscore+hscore

        # print 'Score=',score
        if score<min:
            min=score
            min_linkId=link_id
            min_link=link
        # plot_point_n_links(input_point, [link])
      dfromref=distance_calc(min_link.reference_node,input_point)
      match_obj = matched_point.Matched_point(input_point,min_linkId,'F',dfromref,dist)
      matched_data.append(match_obj)

      # for link_id, dist in out:
      #     if link_id==min_linkId:
      #         link = next((x for x in link_data if x.linkPVID == link_id), None)
      #         dfromref=distance_calc(link.reference_node,input_point)
      #         match_obj = matched_point.Matched_point(input_point,link_id,'F',dfromref,dist)
      #         matched_data.append(match_obj)


      # plot_point_n_links(input_point,links_plot)

  fileObject = open('matched_points', 'wb')
  pickle.dump(matched_data, fileObject)

  print 'Matched points length=',len(matched_data)
  print 'Probe points length=', len(probe_data)





if __name__=="__main__":
  main()
