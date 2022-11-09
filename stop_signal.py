#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 十一月 09, 2022, at 23:53
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\psychopy程序\\stop signal\\stop signal 最后\\stop_signal.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "introduction"
introductionClock = core.Clock()
stop_introduction = visual.TextStim(win=win, name='stop_introduction',
    text='欢迎参加实验\n您需要对屏幕上呈现的图片刺激作形状判断\n图片有两种形状，一种是圆形，一种是方形。\n如果是圆形请按Z键，如果是方形请按M键。\n在无停止信号任务中，\n呈现的图片并需要您既快又准的判断。\n在停止信号任务中，\n图片刺激呈现后间隔一定的时间向您呈现一个红色圆形\n要求看到该提示时不做反应。\n明白后按空格键进入练习。',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
introduction_resp = keyboard.Keyboard()

# Initialize components for Routine "fix"
fixClock = core.Clock()
signal_fix = visual.TextStim(win=win, name='signal_fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "stop_trial"
stop_trialClock = core.Clock()
stop_image = visual.ImageStim(
    win=win,
    name='stop_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.9, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
stop_signal = visual.ImageStim(
    win=win,
    name='stop_signal', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
stop_resp = keyboard.Keyboard()
IAI = .25

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback = 0
practice_feedback = visual.TextStim(win=win, name='practice_feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "interval"
intervalClock = core.Clock()
signal_interval = visual.TextStim(win=win, name='signal_interval',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "start"
startClock = core.Clock()
stop_start = visual.TextStim(win=win, name='stop_start',
    text='按空格键开始正式实验',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "fix"
fixClock = core.Clock()
signal_fix = visual.TextStim(win=win, name='signal_fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "stop_trial"
stop_trialClock = core.Clock()
stop_image = visual.ImageStim(
    win=win,
    name='stop_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.9, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
stop_signal = visual.ImageStim(
    win=win,
    name='stop_signal', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
stop_resp = keyboard.Keyboard()
IAI = .25

# Initialize components for Routine "interval"
intervalClock = core.Clock()
signal_interval = visual.TextStim(win=win, name='signal_interval',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "rest"
restClock = core.Clock()
stop_rest = visual.TextStim(win=win, name='stop_rest',
    text='休息一下',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fix"
fixClock = core.Clock()
signal_fix = visual.TextStim(win=win, name='signal_fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "stop_trial"
stop_trialClock = core.Clock()
stop_image = visual.ImageStim(
    win=win,
    name='stop_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.9, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
stop_signal = visual.ImageStim(
    win=win,
    name='stop_signal', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
stop_resp = keyboard.Keyboard()
IAI = .25

# Initialize components for Routine "interval"
intervalClock = core.Clock()
signal_interval = visual.TextStim(win=win, name='signal_interval',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "end"
endClock = core.Clock()
stop_end = visual.TextStim(win=win, name='stop_end',
    text='实验结束，感谢参与。',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "introduction"-------
continueRoutine = True
# update component parameters for each repeat
introduction_resp.keys = []
introduction_resp.rt = []
_introduction_resp_allKeys = []
# keep track of which components have finished
introductionComponents = [stop_introduction, introduction_resp]
for thisComponent in introductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction"-------
while continueRoutine:
    # get current time
    t = introductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *stop_introduction* updates
    if stop_introduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stop_introduction.frameNStart = frameN  # exact frame index
        stop_introduction.tStart = t  # local t and not account for scr refresh
        stop_introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stop_introduction, 'tStartRefresh')  # time at next scr refresh
        stop_introduction.setAutoDraw(True)
    
    # *introduction_resp* updates
    waitOnFlip = False
    if introduction_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_resp.frameNStart = frameN  # exact frame index
        introduction_resp.tStart = t  # local t and not account for scr refresh
        introduction_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_resp, 'tStartRefresh')  # time at next scr refresh
        introduction_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(introduction_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(introduction_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if introduction_resp.status == STARTED and not waitOnFlip:
        theseKeys = introduction_resp.getKeys(keyList=['space'], waitRelease=False)
        _introduction_resp_allKeys.extend(theseKeys)
        if len(_introduction_resp_allKeys):
            introduction_resp.keys = _introduction_resp_allKeys[-1].name  # just the last key pressed
            introduction_resp.rt = _introduction_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction"-------
for thisComponent in introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('stop_introduction.started', stop_introduction.tStartRefresh)
thisExp.addData('stop_introduction.stopped', stop_introduction.tStopRefresh)
# check responses
if introduction_resp.keys in ['', [], None]:  # No response was made
    introduction_resp.keys = None
thisExp.addData('introduction_resp.keys',introduction_resp.keys)
if introduction_resp.keys != None:  # we had a response
    thisExp.addData('introduction_resp.rt', introduction_resp.rt)
thisExp.addData('introduction_resp.started', introduction_resp.tStartRefresh)
thisExp.addData('introduction_resp.stopped', introduction_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=2.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('signal.xlsx'),
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix"-------
    continueRoutine = True
    routineTimer.add(0.250000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [signal_fix]
    for thisComponent in fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *signal_fix* updates
        if signal_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            signal_fix.frameNStart = frameN  # exact frame index
            signal_fix.tStart = t  # local t and not account for scr refresh
            signal_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(signal_fix, 'tStartRefresh')  # time at next scr refresh
            signal_fix.setAutoDraw(True)
        if signal_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > signal_fix.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                signal_fix.tStop = t  # not accounting for scr refresh
                signal_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(signal_fix, 'tStopRefresh')  # time at next scr refresh
                signal_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix"-------
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('signal_fix.started', signal_fix.tStartRefresh)
    practice.addData('signal_fix.stopped', signal_fix.tStopRefresh)
    
    # ------Prepare to start Routine "stop_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    stop_image.setImage(name)
    stop_signal.setOpacity(appear)
    stop_signal.setPos((0, 0.3))
    stop_signal.setSize((0.6, 0.4))
    stop_signal.setImage(stop_name)
    stop_resp.keys = []
    stop_resp.rt = []
    _stop_resp_allKeys = []
    if stop_resp.keys==answer:
        IAI = 0.25+0.05
    else:
        IAI = 0.25-0.05
    # keep track of which components have finished
    stop_trialComponents = [stop_image, stop_signal, stop_resp]
    for thisComponent in stop_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stop_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stop_trial"-------
    while continueRoutine:
        # get current time
        t = stop_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stop_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stop_image* updates
        if stop_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stop_image.frameNStart = frameN  # exact frame index
            stop_image.tStart = t  # local t and not account for scr refresh
            stop_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stop_image, 'tStartRefresh')  # time at next scr refresh
            stop_image.setAutoDraw(True)
        if stop_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stop_image.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                stop_image.tStop = t  # not accounting for scr refresh
                stop_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stop_image, 'tStopRefresh')  # time at next scr refresh
                stop_image.setAutoDraw(False)
        
        # *stop_signal* updates
        if stop_signal.status == NOT_STARTED and tThisFlip >= IAI-frameTolerance:
            # keep track of start time/frame for later
            stop_signal.frameNStart = frameN  # exact frame index
            stop_signal.tStart = t  # local t and not account for scr refresh
            stop_signal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stop_signal, 'tStartRefresh')  # time at next scr refresh
            stop_signal.setAutoDraw(True)
        if stop_signal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stop_signal.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                stop_signal.tStop = t  # not accounting for scr refresh
                stop_signal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stop_signal, 'tStopRefresh')  # time at next scr refresh
                stop_signal.setAutoDraw(False)
        
        # *stop_resp* updates
        waitOnFlip = False
        if stop_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stop_resp.frameNStart = frameN  # exact frame index
            stop_resp.tStart = t  # local t and not account for scr refresh
            stop_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stop_resp, 'tStartRefresh')  # time at next scr refresh
            stop_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(stop_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(stop_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if stop_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stop_resp.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                stop_resp.tStop = t  # not accounting for scr refresh
                stop_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stop_resp, 'tStopRefresh')  # time at next scr refresh
                stop_resp.status = FINISHED
        if stop_resp.status == STARTED and not waitOnFlip:
            theseKeys = stop_resp.getKeys(keyList=['z', 'm', ''], waitRelease=False)
            _stop_resp_allKeys.extend(theseKeys)
            if len(_stop_resp_allKeys):
                stop_resp.keys = _stop_resp_allKeys[-1].name  # just the last key pressed
                stop_resp.rt = _stop_resp_allKeys[-1].rt
                # was this correct?
                if (stop_resp.keys == str(answer)) or (stop_resp.keys == answer):
                    stop_resp.corr = 1
                else:
                    stop_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stop_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stop_trial"-------
    for thisComponent in stop_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('stop_image.started', stop_image.tStartRefresh)
    practice.addData('stop_image.stopped', stop_image.tStopRefresh)
    practice.addData('stop_signal.started', stop_signal.tStartRefresh)
    practice.addData('stop_signal.stopped', stop_signal.tStopRefresh)
    # check responses
    if stop_resp.keys in ['', [], None]:  # No response was made
        stop_resp.keys = None
        # was no response the correct answer?!
        if str(answer).lower() == 'none':
           stop_resp.corr = 1;  # correct non-response
        else:
           stop_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for practice (TrialHandler)
    practice.addData('stop_resp.keys',stop_resp.keys)
    practice.addData('stop_resp.corr', stop_resp.corr)
    if stop_resp.keys != None:  # we had a response
        practice.addData('stop_resp.rt', stop_resp.rt)
    practice.addData('stop_resp.started', stop_resp.tStartRefresh)
    practice.addData('stop_resp.stopped', stop_resp.tStopRefresh)
    # the Routine "stop_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if stop_resp.keys==answer:
        feedback = "正确"
    else:
        feedback = "错误"
    practice_feedback.setText(feedback)
    # keep track of which components have finished
    feedbackComponents = [practice_feedback]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_feedback* updates
        if practice_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_feedback.frameNStart = frameN  # exact frame index
            practice_feedback.tStart = t  # local t and not account for scr refresh
            practice_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_feedback, 'tStartRefresh')  # time at next scr refresh
            practice_feedback.setAutoDraw(True)
        if practice_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_feedback.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                practice_feedback.tStop = t  # not accounting for scr refresh
                practice_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practice_feedback, 'tStopRefresh')  # time at next scr refresh
                practice_feedback.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('practice_feedback.started', practice_feedback.tStartRefresh)
    practice.addData('practice_feedback.stopped', practice_feedback.tStopRefresh)
    
    # ------Prepare to start Routine "interval"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    intervalComponents = [signal_interval]
    for thisComponent in intervalComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "interval"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = intervalClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intervalClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *signal_interval* updates
        if signal_interval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            signal_interval.frameNStart = frameN  # exact frame index
            signal_interval.tStart = t  # local t and not account for scr refresh
            signal_interval.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(signal_interval, 'tStartRefresh')  # time at next scr refresh
            signal_interval.setAutoDraw(True)
        if signal_interval.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > signal_interval.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                signal_interval.tStop = t  # not accounting for scr refresh
                signal_interval.frameNStop = frameN  # exact frame index
                win.timeOnFlip(signal_interval, 'tStopRefresh')  # time at next scr refresh
                signal_interval.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intervalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "interval"-------
    for thisComponent in intervalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('signal_interval.started', signal_interval.tStartRefresh)
    practice.addData('signal_interval.stopped', signal_interval.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'practice'


# ------Prepare to start Routine "start"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
startComponents = [stop_start, key_resp]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *stop_start* updates
    if stop_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stop_start.frameNStart = frameN  # exact frame index
        stop_start.tStart = t  # local t and not account for scr refresh
        stop_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stop_start, 'tStartRefresh')  # time at next scr refresh
        stop_start.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('stop_start.started', stop_start.tStartRefresh)
thisExp.addData('stop_start.stopped', stop_start.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block1 = data.TrialHandler(nReps=8.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('signal.xlsx'),
    seed=None, name='block1')
thisExp.addLoop(block1)  # add the loop to the experiment
thisBlock1 = block1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
if thisBlock1 != None:
    for paramName in thisBlock1:
        exec('{} = thisBlock1[paramName]'.format(paramName))

for thisBlock1 in block1:
    currentLoop = block1
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
    if thisBlock1 != None:
        for paramName in thisBlock1:
            exec('{} = thisBlock1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix"-------
    continueRoutine = True
    routineTimer.add(0.250000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [signal_fix]
    for thisComponent in fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *signal_fix* updates
        if signal_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            signal_fix.frameNStart = frameN  # exact frame index
            signal_fix.tStart = t  # local t and not account for scr refresh
            signal_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(signal_fix, 'tStartRefresh')  # time at next scr refresh
            signal_fix.setAutoDraw(True)
        if signal_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > signal_fix.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                signal_fix.tStop = t  # not accounting for scr refresh
                signal_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(signal_fix, 'tStopRefresh')  # time at next scr refresh
                signal_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix"-------
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block1.addData('signal_fix.started', signal_fix.tStartRefresh)
    block1.addData('signal_fix.stopped', signal_fix.tStopRefresh)
    
    # ------Prepare to start Routine "stop_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    stop_image.setImage(name)
    stop_signal.setOpacity(appear)
    stop_signal.setPos((0, 0.3))
    stop_signal.setSize((0.6, 0.4))
    stop_signal.setImage(stop_name)
    stop_resp.keys = []
    stop_resp.rt = []
    _stop_resp_allKeys = []
    if stop_resp.keys==answer:
        IAI = 0.25+0.05
    else:
        IAI = 0.25-0.05
    # keep track of which components have finished
    stop_trialComponents = [stop_image, stop_signal, stop_resp]
    for thisComponent in stop_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stop_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stop_trial"-------
    while continueRoutine:
        # get current time
        t = stop_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stop_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stop_image* updates
        if stop_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stop_image.frameNStart = frameN  # exact frame index
            stop_image.tStart = t  # local t and not account for scr refresh
            stop_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stop_image, 'tStartRefresh')  # time at next scr refresh
            stop_image.setAutoDraw(True)
        if stop_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stop_image.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                stop_image.tStop = t  # not accounting for scr refresh
                stop_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stop_image, 'tStopRefresh')  # time at next scr refresh
                stop_image.setAutoDraw(False)
        
        # *stop_signal* updates
        if stop_signal.status == NOT_STARTED and tThisFlip >= IAI-frameTolerance:
            # keep track of start time/frame for later
            stop_signal.frameNStart = frameN  # exact frame index
            stop_signal.tStart = t  # local t and not account for scr refresh
            stop_signal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stop_signal, 'tStartRefresh')  # time at next scr refresh
            stop_signal.setAutoDraw(True)
        if stop_signal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stop_signal.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                stop_signal.tStop = t  # not accounting for scr refresh
                stop_signal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stop_signal, 'tStopRefresh')  # time at next scr refresh
                stop_signal.setAutoDraw(False)
        
        # *stop_resp* updates
        waitOnFlip = False
        if stop_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stop_resp.frameNStart = frameN  # exact frame index
            stop_resp.tStart = t  # local t and not account for scr refresh
            stop_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stop_resp, 'tStartRefresh')  # time at next scr refresh
            stop_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(stop_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(stop_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if stop_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stop_resp.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                stop_resp.tStop = t  # not accounting for scr refresh
                stop_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stop_resp, 'tStopRefresh')  # time at next scr refresh
                stop_resp.status = FINISHED
        if stop_resp.status == STARTED and not waitOnFlip:
            theseKeys = stop_resp.getKeys(keyList=['z', 'm', ''], waitRelease=False)
            _stop_resp_allKeys.extend(theseKeys)
            if len(_stop_resp_allKeys):
                stop_resp.keys = _stop_resp_allKeys[-1].name  # just the last key pressed
                stop_resp.rt = _stop_resp_allKeys[-1].rt
                # was this correct?
                if (stop_resp.keys == str(answer)) or (stop_resp.keys == answer):
                    stop_resp.corr = 1
                else:
                    stop_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stop_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stop_trial"-------
    for thisComponent in stop_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block1.addData('stop_image.started', stop_image.tStartRefresh)
    block1.addData('stop_image.stopped', stop_image.tStopRefresh)
    block1.addData('stop_signal.started', stop_signal.tStartRefresh)
    block1.addData('stop_signal.stopped', stop_signal.tStopRefresh)
    # check responses
    if stop_resp.keys in ['', [], None]:  # No response was made
        stop_resp.keys = None
        # was no response the correct answer?!
        if str(answer).lower() == 'none':
           stop_resp.corr = 1;  # correct non-response
        else:
           stop_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for block1 (TrialHandler)
    block1.addData('stop_resp.keys',stop_resp.keys)
    block1.addData('stop_resp.corr', stop_resp.corr)
    if stop_resp.keys != None:  # we had a response
        block1.addData('stop_resp.rt', stop_resp.rt)
    block1.addData('stop_resp.started', stop_resp.tStartRefresh)
    block1.addData('stop_resp.stopped', stop_resp.tStopRefresh)
    # the Routine "stop_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "interval"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    intervalComponents = [signal_interval]
    for thisComponent in intervalComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "interval"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = intervalClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intervalClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *signal_interval* updates
        if signal_interval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            signal_interval.frameNStart = frameN  # exact frame index
            signal_interval.tStart = t  # local t and not account for scr refresh
            signal_interval.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(signal_interval, 'tStartRefresh')  # time at next scr refresh
            signal_interval.setAutoDraw(True)
        if signal_interval.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > signal_interval.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                signal_interval.tStop = t  # not accounting for scr refresh
                signal_interval.frameNStop = frameN  # exact frame index
                win.timeOnFlip(signal_interval, 'tStopRefresh')  # time at next scr refresh
                signal_interval.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intervalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "interval"-------
    for thisComponent in intervalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block1.addData('signal_interval.started', signal_interval.tStartRefresh)
    block1.addData('signal_interval.stopped', signal_interval.tStopRefresh)
    thisExp.nextEntry()
    
# completed 8.0 repeats of 'block1'


# ------Prepare to start Routine "rest"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = [stop_rest]
for thisComponent in restComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rest"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=restClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *stop_rest* updates
    if stop_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stop_rest.frameNStart = frameN  # exact frame index
        stop_rest.tStart = t  # local t and not account for scr refresh
        stop_rest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stop_rest, 'tStartRefresh')  # time at next scr refresh
        stop_rest.setAutoDraw(True)
    if stop_rest.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > stop_rest.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            stop_rest.tStop = t  # not accounting for scr refresh
            stop_rest.frameNStop = frameN  # exact frame index
            win.timeOnFlip(stop_rest, 'tStopRefresh')  # time at next scr refresh
            stop_rest.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('stop_rest.started', stop_rest.tStartRefresh)
thisExp.addData('stop_rest.stopped', stop_rest.tStopRefresh)

# set up handler to look after randomisation of conditions etc
block2 = data.TrialHandler(nReps=8.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('signal.xlsx'),
    seed=None, name='block2')
thisExp.addLoop(block2)  # add the loop to the experiment
thisBlock2 = block2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock2.rgb)
if thisBlock2 != None:
    for paramName in thisBlock2:
        exec('{} = thisBlock2[paramName]'.format(paramName))

for thisBlock2 in block2:
    currentLoop = block2
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2.rgb)
    if thisBlock2 != None:
        for paramName in thisBlock2:
            exec('{} = thisBlock2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix"-------
    continueRoutine = True
    routineTimer.add(0.250000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [signal_fix]
    for thisComponent in fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *signal_fix* updates
        if signal_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            signal_fix.frameNStart = frameN  # exact frame index
            signal_fix.tStart = t  # local t and not account for scr refresh
            signal_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(signal_fix, 'tStartRefresh')  # time at next scr refresh
            signal_fix.setAutoDraw(True)
        if signal_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > signal_fix.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                signal_fix.tStop = t  # not accounting for scr refresh
                signal_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(signal_fix, 'tStopRefresh')  # time at next scr refresh
                signal_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix"-------
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block2.addData('signal_fix.started', signal_fix.tStartRefresh)
    block2.addData('signal_fix.stopped', signal_fix.tStopRefresh)
    
    # ------Prepare to start Routine "stop_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    stop_image.setImage(name)
    stop_signal.setOpacity(appear)
    stop_signal.setPos((0, 0.3))
    stop_signal.setSize((0.6, 0.4))
    stop_signal.setImage(stop_name)
    stop_resp.keys = []
    stop_resp.rt = []
    _stop_resp_allKeys = []
    if stop_resp.keys==answer:
        IAI = 0.25+0.05
    else:
        IAI = 0.25-0.05
    # keep track of which components have finished
    stop_trialComponents = [stop_image, stop_signal, stop_resp]
    for thisComponent in stop_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stop_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stop_trial"-------
    while continueRoutine:
        # get current time
        t = stop_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stop_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stop_image* updates
        if stop_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stop_image.frameNStart = frameN  # exact frame index
            stop_image.tStart = t  # local t and not account for scr refresh
            stop_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stop_image, 'tStartRefresh')  # time at next scr refresh
            stop_image.setAutoDraw(True)
        if stop_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stop_image.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                stop_image.tStop = t  # not accounting for scr refresh
                stop_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stop_image, 'tStopRefresh')  # time at next scr refresh
                stop_image.setAutoDraw(False)
        
        # *stop_signal* updates
        if stop_signal.status == NOT_STARTED and tThisFlip >= IAI-frameTolerance:
            # keep track of start time/frame for later
            stop_signal.frameNStart = frameN  # exact frame index
            stop_signal.tStart = t  # local t and not account for scr refresh
            stop_signal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stop_signal, 'tStartRefresh')  # time at next scr refresh
            stop_signal.setAutoDraw(True)
        if stop_signal.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stop_signal.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                stop_signal.tStop = t  # not accounting for scr refresh
                stop_signal.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stop_signal, 'tStopRefresh')  # time at next scr refresh
                stop_signal.setAutoDraw(False)
        
        # *stop_resp* updates
        waitOnFlip = False
        if stop_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stop_resp.frameNStart = frameN  # exact frame index
            stop_resp.tStart = t  # local t and not account for scr refresh
            stop_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stop_resp, 'tStartRefresh')  # time at next scr refresh
            stop_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(stop_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(stop_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if stop_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stop_resp.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                stop_resp.tStop = t  # not accounting for scr refresh
                stop_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stop_resp, 'tStopRefresh')  # time at next scr refresh
                stop_resp.status = FINISHED
        if stop_resp.status == STARTED and not waitOnFlip:
            theseKeys = stop_resp.getKeys(keyList=['z', 'm', ''], waitRelease=False)
            _stop_resp_allKeys.extend(theseKeys)
            if len(_stop_resp_allKeys):
                stop_resp.keys = _stop_resp_allKeys[-1].name  # just the last key pressed
                stop_resp.rt = _stop_resp_allKeys[-1].rt
                # was this correct?
                if (stop_resp.keys == str(answer)) or (stop_resp.keys == answer):
                    stop_resp.corr = 1
                else:
                    stop_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stop_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stop_trial"-------
    for thisComponent in stop_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block2.addData('stop_image.started', stop_image.tStartRefresh)
    block2.addData('stop_image.stopped', stop_image.tStopRefresh)
    block2.addData('stop_signal.started', stop_signal.tStartRefresh)
    block2.addData('stop_signal.stopped', stop_signal.tStopRefresh)
    # check responses
    if stop_resp.keys in ['', [], None]:  # No response was made
        stop_resp.keys = None
        # was no response the correct answer?!
        if str(answer).lower() == 'none':
           stop_resp.corr = 1;  # correct non-response
        else:
           stop_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for block2 (TrialHandler)
    block2.addData('stop_resp.keys',stop_resp.keys)
    block2.addData('stop_resp.corr', stop_resp.corr)
    if stop_resp.keys != None:  # we had a response
        block2.addData('stop_resp.rt', stop_resp.rt)
    block2.addData('stop_resp.started', stop_resp.tStartRefresh)
    block2.addData('stop_resp.stopped', stop_resp.tStopRefresh)
    # the Routine "stop_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "interval"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    intervalComponents = [signal_interval]
    for thisComponent in intervalComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "interval"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = intervalClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intervalClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *signal_interval* updates
        if signal_interval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            signal_interval.frameNStart = frameN  # exact frame index
            signal_interval.tStart = t  # local t and not account for scr refresh
            signal_interval.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(signal_interval, 'tStartRefresh')  # time at next scr refresh
            signal_interval.setAutoDraw(True)
        if signal_interval.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > signal_interval.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                signal_interval.tStop = t  # not accounting for scr refresh
                signal_interval.frameNStop = frameN  # exact frame index
                win.timeOnFlip(signal_interval, 'tStopRefresh')  # time at next scr refresh
                signal_interval.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intervalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "interval"-------
    for thisComponent in intervalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block2.addData('signal_interval.started', signal_interval.tStartRefresh)
    block2.addData('signal_interval.stopped', signal_interval.tStopRefresh)
    thisExp.nextEntry()
    
# completed 8.0 repeats of 'block2'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [stop_end]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *stop_end* updates
    if stop_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stop_end.frameNStart = frameN  # exact frame index
        stop_end.tStart = t  # local t and not account for scr refresh
        stop_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stop_end, 'tStartRefresh')  # time at next scr refresh
        stop_end.setAutoDraw(True)
    if stop_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > stop_end.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            stop_end.tStop = t  # not accounting for scr refresh
            stop_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(stop_end, 'tStopRefresh')  # time at next scr refresh
            stop_end.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('stop_end.started', stop_end.tStartRefresh)
thisExp.addData('stop_end.stopped', stop_end.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')


# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
