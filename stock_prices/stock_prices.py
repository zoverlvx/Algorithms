#!/usr/bin/python

import argparse

def find_max_profit(prices):
    highest = 0
    for price in prices:
        if price > highest:
            highest = price
    indexOfHighest = prices.index(highest)
    length = len(prices) - 1
    if indexOfHighest == 0:
        nextHighest = 0
        for i in range(length):
            if prices[i+1] > nextHighest:
                nextHighest = prices[i+1]
        return nextHighest - highest

    lowest = highest
    for i in range(length):
        if i < indexOfHighest:
            if prices[i] < lowest:
                lowest = prices[i]
    return highest - lowest


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

