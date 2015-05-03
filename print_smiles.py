#!/usr/bin/env python
"""
Print the happiness values from each Emo state update.
"""
from joycast.emo import getNextHappiness
from sys import argv

connectOption = int(argv[1])

for happiness in getNextHappiness(connectOption):
    print(happiness)
