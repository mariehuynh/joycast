#!/usr/bin/env python
"""
Take a picture when you smile and upload it to Twitter.
"""
from argparse import ArgumentParser
from joycast.camera import takeSnapshot
from joycast.emo import getNextSmile
from joycast.twitter import uploadPhoto


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("connectionType", type=int,
                        help="1 for an Emotiv EPOC headset, 2 for EmoComposer")
    return parser.parse_args()

args = parse_args()

for smileScore in getNextSmile(args.connectionType):
    print("smileScore = {0:f}".format(smileScore))
    if smileScore > 0.5:  # FIXME: insert real classifier here
        imagePath = takeSnapshot(rotate180=True)
        uploadPhoto(imagePath)
