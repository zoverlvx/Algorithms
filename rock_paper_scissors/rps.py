#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    perms = []
    def rps(n, prefix=[]):
        if n == 0: perms.append(prefix)
        else:
            rps(n - 1, prefix + ["rock"])
            rps(n - 1, prefix + ["paper"])
            rps(n - 1, prefix + ["scissors"])
        rps(n)
        return perms


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
