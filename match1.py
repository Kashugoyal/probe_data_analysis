#! /usr/bin/env python
import csv
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString as line, Point as point

x=[]
y=[]

xref=[]
yref=[]

xnref = []
ynref = []

def probe():
  with open('../probe_data_map_matching/Partition6467ProbePoints.csv', 'rb') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
      for row in spamreader:
        if(row[0] == '4552'):
          x.append(float(row[3]))
          y.append(float(row[4]))
        # print 'latitude=',row[3]
        # print 'latitude=',Decimal(row[3])
        # break
          # print float(row[3])
  print x[-1], y[-1]
  # return x,y
  plt.scatter(x, y)
  plt.show()
  

def link():
  with open('../probe_data_map_matching/Partition6467LinkData.csv', 'rb') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
      for row in spamreader:
          a = row[14].split("|")
          i = a[0].split("/")
          # x.append(i[0])
          # y.append(i[1])
          j = a[-1].split('/')
          x1.append(j[0])
          y1.append(j[1])
          print "ref ",i," nref", j, d
  plt.scatter(x,y)
  plt.show()


def distance(p_x, p_y, line):
  # l = line([(1, 1), (-1,1)])
  p = point(p_x,p_y)
  return p.distance(line)


def search_link():
  # for row in enum(x,y):
  id_array = []
  dist =[]
  with open('../probe_data_map_matching/Partition6467LinkData.csv', 'rb') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
      for row in spamreader:
          a = row[14].split("|")
          l_id = row[0]
          i = float(a[0].split("/"))
          # x.append(i[0])
          # y.append(i[1])
          j = float(a[-1].split('/'))

          # if (abs(x[0] - float(i[0])) < 0.001 and abs(y[0] - float(i[1])) < 0.001) or (abs(x[0] - float(j[0])) < 0.001 and abs(y[0] - float(j[1])) < 0.001):
          if (abs(x[0] - i[0]) < 0.001 and abs(y[0] - i[1]) < 0.001) or (abs(x[0] - j[0]) < 0.001 and abs(y[0] - j[1]) < 0.001):
            id_array.append(l_id)
            dist.append(distance(x[0],y[0],line([(i[0],i[1]),(j[0],j[1])])))

  return id_array, dist





def main():
  # probe()
  # link()
  # print search_link()
  l = line([(1,1), (-1,1),(1,3)])
  print distance(-2,1,l)


if __name__=="__main__":
  main()
