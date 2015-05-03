"""
The amount of global state here is disgusting, but hey, it's a hackathon.
"""

import sys
import os
import ctypes
import time

from os.path import abspath

if sys.platform.startswith('win32'):
    libEDK = ctypes.cdll.LoadLibrary("edk.dll")
elif sys.platform.startswith('linux'):
    srcDir = os.getcwd()
    libPath = srcDir + "/libedk.so.1.0.0"
    libEDK = ctypes.CDLL(libPath)
else:
    srcDir = os.getcwd()
    libPath = srcDir + "/libedk.1.0.0.dylib"
    libEDK = ctypes.CDLL(libPath)

#------------------------------------------------------------------------------
EE_EngineConnect = libEDK.EE_EngineConnect
EE_EngineConnect.argtypes = (ctypes.c_char_p,)
EE_EngineConnect.restype = ctypes.c_int

EE_EngineRemoteConnect = libEDK.EE_EngineRemoteConnect
EE_EngineRemoteConnect.argtypes = (ctypes.c_char_p, ctypes.c_uint)
EE_EngineRemoteConnect.restype = ctypes.c_int

EE_EngineDisconnect = libEDK.EE_EngineDisconnect
EE_EngineDisconnect.argtypes = None
EE_EngineDisconnect.restype = None

EE_EmoStateFree = libEDK.EE_EmoStateFree
EE_EmoStateFree.argtypes = (ctypes.c_void_p,)
EE_EmoStateFree.restype = None

EE_EmoEngineEventFree = libEDK.EE_EmoEngineEventFree
EE_EmoEngineEventFree.argtypes = (ctypes.c_void_p,)
EE_EmoEngineEventFree.restype = None

EE_EmoEngineEventCreate = libEDK.EE_EmoEngineEventCreate
EE_EmoEngineEventCreate.argtypes = None
EE_EmoEngineEventCreate.restype = ctypes.c_void_p

EE_EmoEngineEventGetEmoState = libEDK.EE_EmoEngineEventGetEmoState
EE_EmoEngineEventGetEmoState.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
EE_EmoEngineEventGetEmoState.restype = None

EE_EmoEngineEventGetUserId = libEDK.EE_EmoEngineEventGetUserId
EE_EmoEngineEventGetUserId.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint)]
EE_EmoEngineEventGetUserId.restype = None

EE_EmoEngineEventGetType = libEDK.EE_EmoEngineEventGetType
EE_EmoEngineEventGetType.argtypes = [ctypes.c_void_p]
EE_EmoEngineEventGetType.restype = ctypes.c_int

EE_EngineGetNextEvent = libEDK.EE_EngineGetNextEvent
EE_EngineGetNextEvent.argtypes = [ctypes.c_void_p]
EE_EngineGetNextEvent.restype = ctypes.c_int

ES_GetTimeFromStart = libEDK.ES_GetTimeFromStart
ES_GetTimeFromStart.argtypes = [ctypes.c_void_p]
ES_GetTimeFromStart.restype = ctypes.c_float

EE_EmoStateCreate = libEDK.EE_EmoStateCreate
EE_EmoStateCreate.restype = ctypes.c_void_p

ES_GetWirelessSignalStatus = libEDK.ES_GetWirelessSignalStatus
ES_GetWirelessSignalStatus.restype = ctypes.c_int
ES_GetWirelessSignalStatus.argtypes = [ctypes.c_void_p]

ES_ExpressivIsBlink = libEDK.ES_ExpressivIsBlink
ES_ExpressivIsBlink.restype = ctypes.c_int
ES_ExpressivIsBlink.argtypes = [ctypes.c_void_p]

ES_ExpressivIsLeftWink = libEDK.ES_ExpressivIsLeftWink
ES_ExpressivIsLeftWink.restype = ctypes.c_int
ES_ExpressivIsLeftWink.argtypes = [ctypes.c_void_p]

ES_ExpressivIsRightWink = libEDK.ES_ExpressivIsRightWink
ES_ExpressivIsRightWink.restype = ctypes.c_int
ES_ExpressivIsRightWink.argtypes = [ctypes.c_void_p]

ES_ExpressivIsLookingLeft = libEDK.ES_ExpressivIsLookingLeft
ES_ExpressivIsLookingLeft.restype = ctypes.c_int
ES_ExpressivIsLookingLeft.argtypes = [ctypes.c_void_p]

ES_ExpressivIsLookingRight = libEDK.ES_ExpressivIsLookingRight
ES_ExpressivIsLookingRight.restype = ctypes.c_int
ES_ExpressivIsLookingRight.argtypes = [ctypes.c_void_p]

ES_ExpressivGetUpperFaceAction = libEDK.ES_ExpressivGetUpperFaceAction
ES_ExpressivGetUpperFaceAction.restype = ctypes.c_int
ES_ExpressivGetUpperFaceAction.argtypes = [ctypes.c_void_p]

ES_ExpressivGetUpperFaceActionPower = libEDK.ES_ExpressivGetUpperFaceActionPower
ES_ExpressivGetUpperFaceActionPower.restype = ctypes.c_float
ES_ExpressivGetUpperFaceActionPower.argtypes = [ctypes.c_void_p]

ES_ExpressivGetLowerFaceAction = libEDK.ES_ExpressivGetLowerFaceAction
ES_ExpressivGetLowerFaceAction.restype = ctypes.c_int
ES_ExpressivGetLowerFaceAction.argtypes = [ctypes.c_void_p]

ES_ExpressivGetLowerFaceActionPower = libEDK.ES_ExpressivGetLowerFaceActionPower
ES_ExpressivGetLowerFaceActionPower.restype = ctypes.c_float
ES_ExpressivGetLowerFaceActionPower.argtypes = [ctypes.c_void_p]

ES_AffectivGetExcitementShortTermScore = libEDK.ES_AffectivGetExcitementShortTermScore
ES_AffectivGetExcitementShortTermScore.restype = ctypes.c_float
ES_AffectivGetExcitementShortTermScore.argtypes = [ctypes.c_void_p]

ES_AffectivGetExcitementLongTermScore = libEDK.ES_AffectivGetExcitementLongTermScore
ES_AffectivGetExcitementLongTermScore.restype = ctypes.c_float
ES_AffectivGetExcitementLongTermScore.argtypes = [ctypes.c_void_p]


ES_AffectivGetEngagementBoredomScore = libEDK.ES_AffectivGetEngagementBoredomScore
ES_AffectivGetEngagementBoredomScore.restype = ctypes.c_float
ES_AffectivGetEngagementBoredomScore.argtypes = [ctypes.c_void_p]

ES_CognitivGetCurrentAction = libEDK.ES_CognitivGetCurrentAction
ES_CognitivGetCurrentAction.restype = ctypes.c_int
ES_CognitivGetCurrentAction.argtypes = [ctypes.c_void_p]

ES_CognitivGetCurrentActionPower = libEDK.ES_CognitivGetCurrentActionPower
ES_CognitivGetCurrentActionPower.restype = ctypes.c_float
ES_CognitivGetCurrentActionPower.argtypes = [ctypes.c_void_p]

EE_SaveUserProfile = libEDK.EE_SaveUserProfile
EE_SaveUserProfile.restype = ctypes.c_int
EE_SaveUserProfile.argtypes = (ctypes.c_uint, ctypes.c_char_p)

EE_LoadUserProfile = libEDK.EE_LoadUserProfile
EE_LoadUserProfile.restype = ctypes.c_int
EE_LoadUserProfile.argtypes = (ctypes.c_uint, ctypes.c_char_p)

EE_UserAdded = 16
EE_EmoStateUpdated = 64  # libEDK.EE_Event_enum.EE_EmoStateUpdated
EDK_OK = 0

EXP_EYEBROW = 0x0020      # eyebrow
EXP_FURROW = 0x0040       # furrow
EXP_SMILE = 0x0080        # smile
EXP_CLENCH = 0x0100       # clench
EXP_SMIRK_LEFT = 0x0400   # smirk left
EXP_SMIRK_RIGHT = 0x0800  # smirk right
EXP_LAUGH = 0x0200        # laugh

happinessFactor = {EXP_LAUGH: 1.0,
                   EXP_SMILE: 0.9,
                   EXP_SMIRK_LEFT: 0.5,
                   EXP_SMIRK_RIGHT: 0.5}
def getNextHappiness(connectionType, profileFile=None):
    """
    You can get a convenient stream of happiness values with this
    generator.

    connectionType:
        1 - connect to headset
        2 - connect to EmoComposer

    Ex:

    >>> connectionType = int(raw_input())
    >>> for smile in getNextSmile(connectionType):
            print(smile)
    """
    if connectionType == 1:
        if EE_EngineConnect("Emotiv Systems-5") != 0:
            raise ValueError("Emotiv Engine start up failed")
    elif connectionType == 2:
        composerPort = ctypes.c_uint(1726)
        if EE_EngineRemoteConnect("127.0.0.1", composerPort) != 0:
            raise ValueError("cannot connect to EmoComposer")
    else:
        raise ValueError("option must be 1 (headset) or 2 (EmoComposer)")

    try:
        userID = ctypes.c_uint(9999)
        eEvent = EE_EmoEngineEventCreate()
        eState = EE_EmoStateCreate()

        if profileFile is not None:
            time.sleep(0.1)
            state = EE_EngineGetNextEvent(eEvent)
            if state == EDK_OK:
                eventType = EE_EmoEngineEventGetType(eEvent)
                if eventType == EE_UserAdded:
                    EE_EmoEngineEventGetUserId(eEvent, ctypes.pointer(userID))
                    status = EE_LoadUserProfile(userID, abspath(profileFile))
                    if status != EDK_OK:
                        raise IOError("could not load user profile: path {0:s}, status {1:d}".format(abspath(profileFile), status))
            else:
                raise IOError("could not load user profile: path {0:s}, status {1:d}".format(abspath(profileFile), state))

        while 1:
            time.sleep(0.05)
            state = EE_EngineGetNextEvent(eEvent)
            if state == EDK_OK:
                eventType = EE_EmoEngineEventGetType(eEvent)
                EE_EmoEngineEventGetUserId(eEvent, ctypes.pointer(userID))
                if eventType == EE_EmoStateUpdated:
                    EE_EmoEngineEventGetEmoState(eEvent, eState)
                    lfAction = ES_ExpressivGetLowerFaceAction(eState)
                    lfPower = ES_ExpressivGetLowerFaceActionPower(eState)
                    happiness = lfPower * happinessFactor.get(lfAction, 0)
                    yield happiness
            elif state != 0x0600:
                raise IOError("internal error in Emotiv Engine")
    finally:
        print("Shutting down cleanly...")
        EE_EngineDisconnect()
        EE_EmoStateFree(eState)
        EE_EmoEngineEventFree(eEvent)
