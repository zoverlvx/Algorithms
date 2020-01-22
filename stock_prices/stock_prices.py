#!/usr/bin/python

import argparse

def find_max_profit(prices):
    highest = 0
    for i in range(1, len(prices)):
        if prices[i] > highest:
            highest = prices[i]
    indexOfHighest = prices.index(highest)
    profits_losses = [highest - price for price in prices[:indexOfHighest]]
    profits_losses.sort()
    return profits_losses[-1]


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

