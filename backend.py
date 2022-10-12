'''
Description: 
Version: 1.0
Author: Zhang AO
studentID: 518021910368
School: SJTU
Date: 2022-09-26 20:46:08
LastEditors: Seven
LastEditTime: 2022-10-13 01:22:55
'''
#-*- coding : utf-8-*-
# coding:unicode_escape
from flask import Flask, request
from flanker import flanker
from go_nogo import go_Nogo
from stroop import stroop

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

# 创建Flask的实例对象
app = Flask(__name__)


def packRes(res={}):
    res_dist = {
        "practice_record": res.practice_record,
        "practice_accurate": res.getPracticeAccurate(),
        "ex_record": res.ex_record,
        "ex_accurate": res.getExAccurate(),
    }
    return res_dist


@app.route('/flanker', methods=['GET'])
def do_flanker():
    args = request.args
    # print(args)
    admin = args.get('admin')
    participant = args.get('participant')
    session = args.get('session')
    res = flanker(admin=admin, participant=participant, session=session)
    return packRes(res=res)


@app.route('/go_nogo',methods=['GET'])
def do_go_nogo():
    args=request.args
    admin = args.get('admin')
    participant = args.get('participant')
    session = args.get('session')
    res=go_Nogo(admin=admin, participant=participant, session=session)
    return packRes(res=res)

@app.route('/stroop',methods=['GET'])
def do_stroop():
    args=request.args
    admin = args.get('admin')
    participant = args.get('participant')
    session = args.get('session')
    res=stroop(admin=admin, participant=participant, session=session)
    return packRes(res=res)

@app.route('/helloworld', methods=['GET'])
def helloworld():
    return "helloworld"




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)
