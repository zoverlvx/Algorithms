#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    profitable = []
    for item in items:
        if item[1] < item[2]:
            difference = item[2] - item[1]
            print(F"Penalty: {item[1]}", F"Value: {item[2]}", F"ROI: {difference}", F"Room left: {capacity - item[1]}")
            profitable.append((item[0], item[1], item[2], difference))


    print("Profitable items: ", profitable)
    print("Here is capacity", capacity)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
