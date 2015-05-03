#!/usr/bin/env python
"""
Take a picture when you smile and upload it to Twitter.
"""
from argparse import ArgumentParser
from joycast.camera import takeSnapshot
from joycast.emo import getNextHappiness
from joycast.twitter import uploadPhoto


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("connectionType", type=int,
                        help="1 for an Emotiv EPOC headset, 2 for EmoComposer")
    parser.add_argument("-p", "--profile-file",
                        help="headset training profile")
    parser.add_argument("-T", "--no-tweet", action="store_false",
                        dest="do_tweet",
                        help="do everything except send the Tweet")
    return parser.parse_args()

args = parse_args()

for smileScore in getNextHappiness(args.connectionType,
                                   profileFile=args.profile_file):
    print("smileScore = {0:f}".format(smileScore))
    if smileScore > 0.5:  # FIXME: insert real classifier here
        imagePath = takeSnapshot(rotate180=True)
        if args.do_tweet:
            uploadPhoto(imagePath)
            print("Chirp chirp!")
