'''
Description: 
Version: 1.0
Author: Zhang AO
studentID: 518021910368
School: SJTU
Date: 2022-04-08 13:47:39
LastEditors: Seven
LastEditTime: 2022-06-12 02:40:11
'''

from stroop import stroop
from flanker import flanker
from Twoback import TwoBack
from go_nogo import go_Nogo
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import json

from psychopy.hardware import keyboard
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

if __name__ == "__main__":
    testInfo = {"admin": "testAdmin", "participant": "participantTest1", "session": 1, "gender": "male"}
    testTask = "flanker"
    if len(sys.argv) > 4:
        testInfo["admin"] = sys.argv[1]
        testInfo["participant"] = sys.argv[2]
        testInfo["session"] = sys.argv[3]
        testTask = sys.argv[4]

    # res=go_Nogo(testInfo["admin"],testInfo["participant"],testInfo["gender"],testInfo["session"])
    if testTask == "goNogo":
        res = go_Nogo(testInfo["admin"], testInfo["participant"], testInfo["session"])
        logger.info("go_Nogo res:%s \taccurate:%s" % (res.practice_record, res.getPracticeAccurate()))
    # elif testTask=="twoBack":
    #     res=TwoBack(testInfo["admin"],testInfo["participant"],testInfo["session"])
    # logger.info("twoBack res:%s \taccurate:%s"%(res.practice_record,res.getPracticeAccurate()))
    elif testTask == "flanker":
        res = flanker(testInfo["admin"], testInfo["participant"], testInfo["session"])
        logger.info("flanker res:%s \taccurate:%s" % (res.practice_record, res.getPracticeAccurate()))
    elif testTask == "stroop":
        res = stroop(testInfo["admin"], testInfo["participant"], testInfo["session"])
        logger.info("stroop res:%s \taccurate:%s" % (res.practice_record, res.getPracticeAccurate()))

    res_dist = {
        "practice_record": res.practice_record,
        "practice_accurate": res.getPracticeAccurate(),
        "ex_record": res.ex_record,
        "ex_accurate": res.getExAccurate(),
    }
    jsObj = json.dumps(res_dist)
    fileObject = open('curTmp.json', 'w')
    fileObject.write(jsObj)
    fileObject.close()
