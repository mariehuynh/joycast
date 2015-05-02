#!/usr/bin/env python
"""
Print the smile values from each Emo state update.
"""
from joycast.emo import getNextSmile
from sys import argv

connectOption = int(argv[1])

for smile in getNextSmile(connectOption):
    print(smile)
