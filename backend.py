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

from ANT import ANT
from TTC import TTC
from flanker import *
from go_nogo import *
from mental import mental
from more_odd import moreOdd
from posner import posner
from stop_signal import stopSignal
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

@app.route('/ant', methods=['GET'])
def do_ANT():
    args = request.args
    admin = args.get('admin')
    participant = args.get('participant')
    group = args.get('group')
    session = args.get('session')
    p = Process(target=ANT_write,args=(admin, participant, group, session))
    p.start()
    return "success"

@app.route('/mental', methods=['GET'])
def do_mental():
    args = request.args
    admin = args.get('admin')
    participant = args.get('participant')
    group = args.get('group')
    session = args.get('session')
    p = Process(target=mental_write,args=(admin, participant, group, session))
    p.start()
    return "success"

@app.route('/moreOdd', methods=['GET'])
def do_more_odd():
    args = request.args
    admin = args.get('admin')
    participant = args.get('participant')
    group = args.get('group')
    session = args.get('session')
    p = Process(target=moreOdd_write,args=(admin, participant, group, session))
    p.start()
    return "success"

@app.route('/posner', methods=['GET'])
def do_posner():
    args = request.args
    admin = args.get('admin')
    participant = args.get('participant')
    group = args.get('group')
    session = args.get('session')
    p = Process(target=posner_write,args=(admin, participant, group, session))
    p.start()
    return "success"

@app.route('/stopSignal', methods=['GET'])
def do_stop_signal():
    args = request.args
    admin = args.get('admin')
    participant = args.get('participant')
    group = args.get('group')
    session = args.get('session')
    p = Process(target=stop_signal_write,args=(admin, participant, group, session))
    p.start()
    return "success"

@app.route('/TTC', methods=['GET'])
def do_TTC():
    args = request.args
    admin = args.get('admin')
    participant = args.get('participant')
    group = args.get('group')
    session = args.get('session')
    p = Process(target=TTC_write,args=(admin, participant, group, session))
    p.start()
    return "success"

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


def ANT_write(admin, participant, group, session):
    res=ANT(admin, participant, group, session)
    out_file = open("./tmp/ANT.log", "w")
    json.dump(object2dict(res),out_file,indent=4)
    return "ANT"

def mental_write(admin, participant, group, session):
    res=mental(admin, participant, group, session)
    out_file = open("./tmp/mental.log", "w")
    json.dump(object2dict(res),out_file,indent=4)
    return "ANT"

def moreOdd_write(admin, participant, group, session):
    res=moreOdd(admin, participant, group, session)
    out_file = open("./tmp/more_odd.log", "w")
    json.dump(object2dict(res),out_file,indent=4)
    return "more_odd"

def posner_write(admin, participant, group, session):
    res=posner(admin, participant, group, session)
    out_file = open("./tmp/posner.log", "w")
    json.dump(object2dict(res),out_file,indent=4)
    return "posner"

def stop_signal_write(admin, participant, group, session):
    res=stopSignal(admin, participant, group, session)
    out_file = open("./tmp/stop_signal.log", "w")
    json.dump(object2dict(res),out_file,indent=4)
    return "stop_signal"

def TTC_write(admin, participant, group, session):
    res=TTC(admin, participant, group, session)
    out_file = open("./tmp/TTC.log", "w")
    json.dump(object2dict(res),out_file,indent=4)
    return "TTC"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)
