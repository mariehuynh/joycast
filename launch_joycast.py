#!/usr/bin/env python
"""
Take a picture when you smile and upload it to Twitter.
"""
from argparse import ArgumentParser
from time import time

from joycast.camera import takeSnapshot
from joycast.emo import getNextHappiness
from joycast.twitter import uploadPhoto


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("connectionType", type=int,
                        help="1 for an Emotiv EPOC headset, 2 for EmoComposer")
    parser.add_argument("-p", "--profile-file",
                        help="headset training profile")
    parser.add_argument("-r", "--refractory-time", type=int, default=10,
                         help="how long to disarm after snapping a photo (seconds)")
    parser.add_argument("-f", "--filter-length", type=int, default=5, help="length of filter (samples)")
    parser.add_argument("-a", "--trigger-threshold", type=float, default=0.8,
                         help="snap a picture if filtered happiness goes above TRIGGER_THRESHOLD")
    parser.add_argument("-b", "--rearm-threshold", type=float, default=0.2,
                         help="only rearm trigger if filtered happiness goes below REARM_THRESHOLD")
    parser.add_argument("-T", "--no-tweet", action="store_false",
                        dest="do_tweet",
                        help="do everything except send the Tweet")
    return parser.parse_args()

class HappinessFilter(object):
    """
    Simple tophat filter for simplicity.
    """
    def __init__(self, filterLength):
        self.history = [0] * filterLength

    def update(self, x):
        self.history = self.history[1:] + [x]
        mean = sum(self.history) / len(self.history)
        return mean

args = parse_args()

happinessFilter = HappinessFilter(args.filter_length)
lastTriggerTime = None
state = "armed"
for smileScore in getNextHappiness(args.connectionType,
                                   profileFile=args.profile_file):
    filteredHappiness = happinessFilter.update(smileScore)
    print(filteredHappiness)
    if state == "armed":
        if filteredHappiness > args.trigger_threshold:
            print("trigger!")
            imagePath = takeSnapshot(rotate180=True)
            if args.do_tweet:
                uploadPhoto(imagePath)
                print("Chirp chirp!")
            state = "disarmed"
            print("disarmed")
            lastTriggerTime = time()
    elif state == "disarmed":
        waited = time() - lastTriggerTime
        print("{0:f} seconds since triggered".format(waited))
        if waited > args.refractory_time:
            state = "awaiting calm"
            print("awaiting calm")
    elif state == "awaiting calm":
        if filteredHappiness < args.rearm_threshold:
            state = "armed"
            print("armed")
    else:
        raise ValueError("illegal state")
