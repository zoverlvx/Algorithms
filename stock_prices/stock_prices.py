#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # creates new copy of original order of prices
    original = [] + prices
    # sorts prices in ascending order
    prices.sort()
    # points to the highest value price
    lastIndex = len(prices) - 1
    highest = prices[lastIndex]

    # find the index of the highest value in the original order
    indexOfOriginal = original.index(highest)
    lowest = highest
    length = len(prices) - 1
    for i in range(length):
        if i < indexOfOriginal:
            if original[i] < lowest:
                lowest = original[i]
                print(lowest)


    return highest - lowest

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

