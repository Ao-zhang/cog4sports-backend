'''
Description: 
Version: 1.0
Author: Zhang AO
studentID: 518021910368
School: SJTU
Date: 2022-09-26 20:46:08
LastEditors: Seven
LastEditTime: 2022-10-29 22:31:06
'''
#-*- coding : utf-8-*-
# coding:unicode_escape
from flask import Flask, request
from flanker import *
from go_nogo import *
from stroop import *

from Twoback import *
from go_nogo import *
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
from multiprocessing import Process

# 创建Flask的实例对象
app = Flask(__name__)

def object2dict(obj):
    #convert object to a dict
    d = {}
    d.update(obj.__dict__)
    return d



def packRes(res={}):
    res_dist = {
        "practice_record": res.practice_record,
        "practice_accurate": res.getPracticeAccurate(),
        "ex_record": res.ex_record,
        "ex_accurate": res.getExAccurate(),
    }
    return res_dist

@app.route('/twoBack', methods=['GET'])
def do_TwoBack():
    args = request.args
    # print(args)
    admin = args.get('admin')
    participant = args.get('participant')
    group = args.get('group')
    session = args.get('session')
    p = Process(target=TwoBack_write,args=(admin, participant, group, session))
    p.start() 
    return "success"

@app.route('/flanker', methods=['GET'])
def do_flanker():
    args = request.args
    # print(args)
    admin = args.get('admin')
    participant = args.get('participant')
    group = args.get('group')
    session = args.get('session')
    p = Process(target=flanker_write,args=(admin, participant, group, session))
    p.start() 
    return "success"
    # res = flanker(admin=admin, participant=participant, session=session)
    # return packRes(res=res)


@app.route('/go_nogo', methods=['GET'])
def do_go_nogo():
    args = request.args
    admin = args.get('admin')
    participant = args.get('participant')
    group = args.get('group')
    session = args.get('session')
    
    p = Process(target=go_Nogo_write,args=(admin, participant, group, session))
    p.start() 
    return "success"
    # res = go_Nogo(admin=admin, participant=participant, session=session)
    # return packRes(res=res)


@app.route('/stroop', methods=['GET'])
def do_stroop():
    args = request.args
    admin = args.get('admin')
    participant = args.get('participant')
    group = args.get('group')
    session = args.get('session')
    p = Process(target=stroop_write,args=(admin, participant, group, session))
    p.start() 
    return "success"
    # res = stroop(admin=admin, participant=participant, session=session)
    # return packRes(res=res)

def flanker_write(admin, participant, group, session):
    res=flanker(admin, participant, group, session)
    
    out_file = open("./tmp/flanker.log", "w") 
    json.dump(object2dict(res),out_file,indent=4)
    return "flanker"

def go_Nogo_write(admin, participant, group, session):
    res=go_Nogo(admin, participant, group, session)

    out_file = open("./tmp/go_Nogo.log", "w") 
    json.dump(object2dict(res),out_file,indent=4)
    return "go_Nogo"

def stroop_write(admin, participant, group, session):
    res=stroop(admin, participant, group, session)
    out_file = open("./tmp/stroop.log", "w") 
    json.dump(object2dict(res),out_file,indent=4)
    return "stroop"

def TwoBack_write(admin, participant, group, session):
    res=TwoBack(admin, participant, group, session)
    out_file = open("./tmp/TwoBack.log", "w") 
    json.dump(object2dict(res),out_file,indent=4)

    return "TwoBack"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)
