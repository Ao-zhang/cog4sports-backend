#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 十一月 09, 2022, at 23:52
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

class moreOddResponse:
    practice_record = []
    ex_record = []

    def __init__(self, practice, ex):
        self.practice_record = practice
        self.ex_record = ex

    def getPracticeAccurate(self):
        return sum(self.practice_record) / len(self.practice_record)

    def getExAccurate(self):
        return sum(self.ex_record) / len(self.ex_record)

def moreOdd(admin, participant, group, session):
    # Ensure that relative paths start from the same directory as this script
    _thisDir = "."

    # Store info about the experiment session
    expInfo = {}
    expInfo['admin'] = admin
    expInfo['participant'] = participant
    expInfo['session'] = session
    expName = "flanker"
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    print(expInfo['date'])

    returnValue = moreOddResponse([], [])

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data/moreOdd/%s/%s/%s/%s' % (admin, participant, group, session)

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
                                     extraInfo=expInfo, runtimeInfo=None,
                                     savePickle=False, saveWideText=True,
                                     originPath='./',
                                     dataFileName=filename)

    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    frameTolerance = 0.001  # how close to onset before 'same' frame

    # Start Code - component code to be run after the window creation

    # Setup the Window
    win = visual.Window(
        size=[1280, 720], fullscr=False, screen=0,
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

    # Initialize components for Routine "odd_introduction"
    odd_introductionClock = core.Clock()
    odd_practice_introduction = visual.TextStim(win=win, name='odd_practice_introduction',
        text='欢迎参加本次实验!\n屏幕上将呈现两种颜色的数字：\n如果呈现数字是黑色的,\n则需要对数字的“大/小“进行判断，\n若比“5”小请按F，比“5”大请按L；\n如果呈现的数字是绿色的，\n则对数字的“奇/偶”进行判断，\n若是“奇数”请按F，“偶数”请按L。\n请您在保证正确率的情况下尽可能的做出判断。\n接下来将进行练习实验\n按空格键开始练习。\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    introduction_resp = keyboard.Keyboard()

    # Initialize components for Routine "odd_practice_fix"
    odd_practice_fixClock = core.Clock()
    odd_pra_fix = visual.TextStim(win=win, name='odd_pra_fix',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_practice_trial"
    odd_practice_trialClock = core.Clock()
    odd_practice_stimuli = visual.TextStim(win=win, name='odd_practice_stimuli',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    odd_practice_resp = keyboard.Keyboard()
    feedback = '0'

    # Initialize components for Routine "odd_feedback"
    odd_feedbackClock = core.Clock()
    odd_text = visual.TextStim(win=win, name='odd_text',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_soa"
    odd_soaClock = core.Clock()
    odd_inerval = visual.TextStim(win=win, name='odd_inerval',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_ex_introduction"
    odd_ex_introductionClock = core.Clock()
    odd_ex_text = visual.TextStim(win=win, name='odd_ex_text',
        text='练习结束\n现在进入正式实验\n按空格键开始',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    odd_text_resp = keyboard.Keyboard()

    # Initialize components for Routine "odd_ex_fix"
    odd_ex_fixClock = core.Clock()
    odd_task_fix = visual.TextStim(win=win, name='odd_task_fix',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_task1_trial"
    odd_task1_trialClock = core.Clock()
    odd_task1_stimuli = visual.TextStim(win=win, name='odd_task1_stimuli',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    odd_task1_resp = keyboard.Keyboard()

    # Initialize components for Routine "odd_soa"
    odd_soaClock = core.Clock()
    odd_inerval = visual.TextStim(win=win, name='odd_inerval',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_rest"
    odd_restClock = core.Clock()
    odd_ex_rest = visual.TextStim(win=win, name='odd_ex_rest',
        text='休息20s',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    odd_restend = visual.TextStim(win=win, name='odd_restend',
        text='按空格键开始',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    odd_rest_resp = keyboard.Keyboard()

    # Initialize components for Routine "odd_ex_fix"
    odd_ex_fixClock = core.Clock()
    odd_task_fix = visual.TextStim(win=win, name='odd_task_fix',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_task2_trial"
    odd_task2_trialClock = core.Clock()
    odd_task2_stimuli = visual.TextStim(win=win, name='odd_task2_stimuli',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    odd_task2_resp = keyboard.Keyboard()

    # Initialize components for Routine "odd_soa"
    odd_soaClock = core.Clock()
    odd_inerval = visual.TextStim(win=win, name='odd_inerval',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_rest"
    odd_restClock = core.Clock()
    odd_ex_rest = visual.TextStim(win=win, name='odd_ex_rest',
        text='休息20s',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    odd_restend = visual.TextStim(win=win, name='odd_restend',
        text='按空格键开始',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    odd_rest_resp = keyboard.Keyboard()

    # Initialize components for Routine "odd_ex_fix"
    odd_ex_fixClock = core.Clock()
    odd_task_fix = visual.TextStim(win=win, name='odd_task_fix',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_task3_trial"
    odd_task3_trialClock = core.Clock()
    odd_task3_stimuli = visual.TextStim(win=win, name='odd_task3_stimuli',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    odd_task3_resp = keyboard.Keyboard()

    # Initialize components for Routine "odd_soa"
    odd_soaClock = core.Clock()
    odd_inerval = visual.TextStim(win=win, name='odd_inerval',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_rest"
    odd_restClock = core.Clock()
    odd_ex_rest = visual.TextStim(win=win, name='odd_ex_rest',
        text='休息20s',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    odd_restend = visual.TextStim(win=win, name='odd_restend',
        text='按空格键开始',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    odd_rest_resp = keyboard.Keyboard()

    # Initialize components for Routine "odd_ex_fix"
    odd_ex_fixClock = core.Clock()
    odd_task_fix = visual.TextStim(win=win, name='odd_task_fix',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_task3_trial"
    odd_task3_trialClock = core.Clock()
    odd_task3_stimuli = visual.TextStim(win=win, name='odd_task3_stimuli',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    odd_task3_resp = keyboard.Keyboard()

    # Initialize components for Routine "odd_soa"
    odd_soaClock = core.Clock()
    odd_inerval = visual.TextStim(win=win, name='odd_inerval',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_rest"
    odd_restClock = core.Clock()
    odd_ex_rest = visual.TextStim(win=win, name='odd_ex_rest',
        text='休息20s',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    odd_restend = visual.TextStim(win=win, name='odd_restend',
        text='按空格键开始',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    odd_rest_resp = keyboard.Keyboard()

    # Initialize components for Routine "odd_ex_fix"
    odd_ex_fixClock = core.Clock()
    odd_task_fix = visual.TextStim(win=win, name='odd_task_fix',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_task2_trial"
    odd_task2_trialClock = core.Clock()
    odd_task2_stimuli = visual.TextStim(win=win, name='odd_task2_stimuli',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    odd_task2_resp = keyboard.Keyboard()

    # Initialize components for Routine "odd_soa"
    odd_soaClock = core.Clock()
    odd_inerval = visual.TextStim(win=win, name='odd_inerval',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_ex_fix"
    odd_ex_fixClock = core.Clock()
    odd_task_fix = visual.TextStim(win=win, name='odd_task_fix',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_task1_trial"
    odd_task1_trialClock = core.Clock()
    odd_task1_stimuli = visual.TextStim(win=win, name='odd_task1_stimuli',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    odd_task1_resp = keyboard.Keyboard()

    # Initialize components for Routine "odd_soa"
    odd_soaClock = core.Clock()
    odd_inerval = visual.TextStim(win=win, name='odd_inerval',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "odd_end"
    odd_endClock = core.Clock()
    odd_endtext = visual.TextStim(win=win, name='odd_endtext',
        text='实验结束',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    # ------Prepare to start Routine "odd_introduction"-------
    continueRoutine = True
    # update component parameters for each repeat
    introduction_resp.keys = []
    introduction_resp.rt = []
    _introduction_resp_allKeys = []
    # keep track of which components have finished
    odd_introductionComponents = [odd_practice_introduction, introduction_resp]
    for thisComponent in odd_introductionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    odd_introductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "odd_introduction"-------
    while continueRoutine:
        # get current time
        t = odd_introductionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=odd_introductionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *odd_practice_introduction* updates
        if odd_practice_introduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            odd_practice_introduction.frameNStart = frameN  # exact frame index
            odd_practice_introduction.tStart = t  # local t and not account for scr refresh
            odd_practice_introduction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_practice_introduction, 'tStartRefresh')  # time at next scr refresh
            odd_practice_introduction.setAutoDraw(True)
        
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
            return returnValue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in odd_introductionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "odd_introduction"-------
    for thisComponent in odd_introductionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('odd_practice_introduction.started', odd_practice_introduction.tStartRefresh)
    thisExp.addData('odd_practice_introduction.stopped', odd_practice_introduction.tStopRefresh)
    # check responses
    if introduction_resp.keys in ['', [], None]:  # No response was made
        introduction_resp.keys = None
    thisExp.addData('introduction_resp.keys',introduction_resp.keys)
    if introduction_resp.keys != None:  # we had a response
        thisExp.addData('introduction_resp.rt', introduction_resp.rt)
    thisExp.addData('introduction_resp.started', introduction_resp.tStartRefresh)
    thisExp.addData('introduction_resp.stopped', introduction_resp.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "odd_introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    odd_practice = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tableResource/odd_practice.xlsx'),
        seed=None, name='odd_practice')
    thisExp.addLoop(odd_practice)  # add the loop to the experiment
    thisOdd_practice = odd_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOdd_practice.rgb)
    if thisOdd_practice != None:
        for paramName in thisOdd_practice:
            exec('{} = thisOdd_practice[paramName]'.format(paramName))

    for thisOdd_practice in odd_practice:
        currentLoop = odd_practice
        # abbreviate parameter names if possible (e.g. rgb = thisOdd_practice.rgb)
        if thisOdd_practice != None:
            for paramName in thisOdd_practice:
                exec('{} = thisOdd_practice[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "odd_practice_fix"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        odd_practice_fixComponents = [odd_pra_fix]
        for thisComponent in odd_practice_fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_practice_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        odd_practice_color = thisOdd_practice['odd_practice_color']
        odd_practice_name = thisOdd_practice['odd_practice_name']
        odd_practice_answer = thisOdd_practice['odd_practice_answer']
        # -------Run Routine "odd_practice_fix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_practice_fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_practice_fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_pra_fix* updates
            if odd_pra_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_pra_fix.frameNStart = frameN  # exact frame index
                odd_pra_fix.tStart = t  # local t and not account for scr refresh
                odd_pra_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_pra_fix, 'tStartRefresh')  # time at next scr refresh
                odd_pra_fix.setAutoDraw(True)
            if odd_pra_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_pra_fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_pra_fix.tStop = t  # not accounting for scr refresh
                    odd_pra_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_pra_fix, 'tStopRefresh')  # time at next scr refresh
                    odd_pra_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_practice_fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_practice_fix"-------
        for thisComponent in odd_practice_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd_practice.addData('odd_pra_fix.started', odd_pra_fix.tStartRefresh)
        odd_practice.addData('odd_pra_fix.stopped', odd_pra_fix.tStopRefresh)

        # ------Prepare to start Routine "odd_practice_trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        odd_practice_stimuli.setColor(odd_practice_color, colorSpace='rgb')
        odd_practice_stimuli.setText(odd_practice_name)
        odd_practice_resp.keys = []
        odd_practice_resp.rt = []
        _odd_practice_resp_allKeys = []
        # keep track of which components have finished
        odd_practice_trialComponents = [odd_practice_stimuli, odd_practice_resp]
        for thisComponent in odd_practice_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_practice_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_practice_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_practice_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_practice_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_practice_stimuli* updates
            if odd_practice_stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_practice_stimuli.frameNStart = frameN  # exact frame index
                odd_practice_stimuli.tStart = t  # local t and not account for scr refresh
                odd_practice_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_practice_stimuli, 'tStartRefresh')  # time at next scr refresh
                odd_practice_stimuli.setAutoDraw(True)
            if odd_practice_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_practice_stimuli.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_practice_stimuli.tStop = t  # not accounting for scr refresh
                    odd_practice_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_practice_stimuli, 'tStopRefresh')  # time at next scr refresh
                    odd_practice_stimuli.setAutoDraw(False)
            
            # *odd_practice_resp* updates
            waitOnFlip = False
            if odd_practice_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_practice_resp.frameNStart = frameN  # exact frame index
                odd_practice_resp.tStart = t  # local t and not account for scr refresh
                odd_practice_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_practice_resp, 'tStartRefresh')  # time at next scr refresh
                odd_practice_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(odd_practice_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(odd_practice_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if odd_practice_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_practice_resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_practice_resp.tStop = t  # not accounting for scr refresh
                    odd_practice_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_practice_resp, 'tStopRefresh')  # time at next scr refresh
                    odd_practice_resp.status = FINISHED
            if odd_practice_resp.status == STARTED and not waitOnFlip:
                theseKeys = odd_practice_resp.getKeys(keyList=['f', 'l'], waitRelease=False)
                _odd_practice_resp_allKeys.extend(theseKeys)
                if len(_odd_practice_resp_allKeys):
                    odd_practice_resp.keys = _odd_practice_resp_allKeys[-1].name  # just the last key pressed
                    odd_practice_resp.rt = _odd_practice_resp_allKeys[-1].rt
                    # was this correct?
                    if (odd_practice_resp.keys == str(odd_practice_answer)) or (odd_practice_resp.keys == odd_practice_answer):
                        odd_practice_resp.corr = 1
                    else:
                        odd_practice_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_practice_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_practice_trial"-------
        for thisComponent in odd_practice_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd_practice.addData('odd_practice_stimuli.started', odd_practice_stimuli.tStartRefresh)
        odd_practice.addData('odd_practice_stimuli.stopped', odd_practice_stimuli.tStopRefresh)
        # check responses
        if odd_practice_resp.keys in ['', [], None]:  # No response was made
            odd_practice_resp.keys = None
            # was no response the correct answer?!
            if str(odd_practice_answer).lower() == 'none':
                odd_practice_resp.corr = 1;  # correct non-response
            else:
                odd_practice_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for odd_practice (TrialHandler)
        odd_practice.addData('odd_practice_resp.keys',odd_practice_resp.keys)
        odd_practice.addData('odd_practice_resp.corr', odd_practice_resp.corr)
        returnValue.practice_record.append(odd_practice_resp.corr)
        if odd_practice_resp.keys != None:  # we had a response
            odd_practice.addData('odd_practice_resp.rt', odd_practice_resp.rt)
        odd_practice.addData('odd_practice_resp.started', odd_practice_resp.tStartRefresh)
        odd_practice.addData('odd_practice_resp.stopped', odd_practice_resp.tStopRefresh)
        if odd_practice_resp.keys==odd_practice_answer:
            feedback='正确'
        else:
            feedback='错误'
        
        # ------Prepare to start Routine "odd_feedback"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        odd_text.setText(feedback)
        # keep track of which components have finished
        odd_feedbackComponents = [odd_text]
        for thisComponent in odd_feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_feedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_text* updates
            if odd_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_text.frameNStart = frameN  # exact frame index
                odd_text.tStart = t  # local t and not account for scr refresh
                odd_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_text, 'tStartRefresh')  # time at next scr refresh
                odd_text.setAutoDraw(True)
            if odd_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_text.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_text.tStop = t  # not accounting for scr refresh
                    odd_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_text, 'tStopRefresh')  # time at next scr refresh
                    odd_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_feedback"-------
        for thisComponent in odd_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd_practice.addData('odd_text.started', odd_text.tStartRefresh)
        odd_practice.addData('odd_text.stopped', odd_text.tStopRefresh)
        
        # ------Prepare to start Routine "odd_soa"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        odd_soaComponents = [odd_inerval]
        for thisComponent in odd_soaComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_soaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_soa"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_soaClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_soaClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_inerval* updates
            if odd_inerval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_inerval.frameNStart = frameN  # exact frame index
                odd_inerval.tStart = t  # local t and not account for scr refresh
                odd_inerval.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_inerval, 'tStartRefresh')  # time at next scr refresh
                odd_inerval.setAutoDraw(True)
            if odd_inerval.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_inerval.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_inerval.tStop = t  # not accounting for scr refresh
                    odd_inerval.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_inerval, 'tStopRefresh')  # time at next scr refresh
                    odd_inerval.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_soaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_soa"-------
        for thisComponent in odd_soaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd_practice.addData('odd_inerval.started', odd_inerval.tStartRefresh)
        odd_practice.addData('odd_inerval.stopped', odd_inerval.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'odd_practice'


    # ------Prepare to start Routine "odd_ex_introduction"-------
    continueRoutine = True
    # update component parameters for each repeat
    odd_text_resp.keys = []
    odd_text_resp.rt = []
    _odd_text_resp_allKeys = []
    # keep track of which components have finished
    odd_ex_introductionComponents = [odd_ex_text, odd_text_resp]
    for thisComponent in odd_ex_introductionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    odd_ex_introductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "odd_ex_introduction"-------
    while continueRoutine:
        # get current time
        t = odd_ex_introductionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=odd_ex_introductionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *odd_ex_text* updates
        if odd_ex_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            odd_ex_text.frameNStart = frameN  # exact frame index
            odd_ex_text.tStart = t  # local t and not account for scr refresh
            odd_ex_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_ex_text, 'tStartRefresh')  # time at next scr refresh
            odd_ex_text.setAutoDraw(True)
        
        # *odd_text_resp* updates
        waitOnFlip = False
        if odd_text_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            odd_text_resp.frameNStart = frameN  # exact frame index
            odd_text_resp.tStart = t  # local t and not account for scr refresh
            odd_text_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_text_resp, 'tStartRefresh')  # time at next scr refresh
            odd_text_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(odd_text_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(odd_text_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if odd_text_resp.status == STARTED and not waitOnFlip:
            theseKeys = odd_text_resp.getKeys(keyList=['space'], waitRelease=False)
            _odd_text_resp_allKeys.extend(theseKeys)
            if len(_odd_text_resp_allKeys):
                odd_text_resp.keys = _odd_text_resp_allKeys[-1].name  # just the last key pressed
                odd_text_resp.rt = _odd_text_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in odd_ex_introductionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "odd_ex_introduction"-------
    for thisComponent in odd_ex_introductionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('odd_ex_text.started', odd_ex_text.tStartRefresh)
    thisExp.addData('odd_ex_text.stopped', odd_ex_text.tStopRefresh)
    # check responses
    if odd_text_resp.keys in ['', [], None]:  # No response was made
        odd_text_resp.keys = None
    thisExp.addData('odd_text_resp.keys',odd_text_resp.keys)
    if odd_text_resp.keys != None:  # we had a response
        thisExp.addData('odd_text_resp.rt', odd_text_resp.rt)
    thisExp.addData('odd_text_resp.started', odd_text_resp.tStartRefresh)
    thisExp.addData('odd_text_resp.stopped', odd_text_resp.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "odd_ex_introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    odd1_task1 = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tableResource/odd_task1.xlsx'),
        seed=None, name='odd1_task1')
    thisExp.addLoop(odd1_task1)  # add the loop to the experiment
    thisOdd1_task1 = odd1_task1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOdd1_task1.rgb)
    if thisOdd1_task1 != None:
        for paramName in thisOdd1_task1:
            exec('{} = thisOdd1_task1[paramName]'.format(paramName))

    for thisOdd1_task1 in odd1_task1:
        currentLoop = odd1_task1
        # abbreviate parameter names if possible (e.g. rgb = thisOdd1_task1.rgb)
        if thisOdd1_task1 != None:
            for paramName in thisOdd1_task1:
                exec('{} = thisOdd1_task1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "odd_ex_fix"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        odd_ex_fixComponents = [odd_task_fix]
        for thisComponent in odd_ex_fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_ex_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        odd_task1_color = thisOdd1_task1['odd_task1_color']
        odd_task1_name = thisOdd1_task1['odd_task1_name']
        odd_task1_answer = thisOdd1_task1['odd_task1_answer']
        
        # -------Run Routine "odd_ex_fix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_ex_fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_ex_fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_task_fix* updates
            if odd_task_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task_fix.frameNStart = frameN  # exact frame index
                odd_task_fix.tStart = t  # local t and not account for scr refresh
                odd_task_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task_fix, 'tStartRefresh')  # time at next scr refresh
                odd_task_fix.setAutoDraw(True)
            if odd_task_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task_fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task_fix.tStop = t  # not accounting for scr refresh
                    odd_task_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task_fix, 'tStopRefresh')  # time at next scr refresh
                    odd_task_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_ex_fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_ex_fix"-------
        for thisComponent in odd_ex_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd1_task1.addData('odd_task_fix.started', odd_task_fix.tStartRefresh)
        odd1_task1.addData('odd_task_fix.stopped', odd_task_fix.tStopRefresh)

        # ------Prepare to start Routine "odd_task1_trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        odd_task1_stimuli.setColor(odd_task1_color, colorSpace='rgb')
        odd_task1_stimuli.setText(odd_task1_name)
        odd_task1_resp.keys = []
        odd_task1_resp.rt = []
        _odd_task1_resp_allKeys = []
        # keep track of which components have finished
        odd_task1_trialComponents = [odd_task1_stimuli, odd_task1_resp]
        for thisComponent in odd_task1_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_task1_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_task1_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_task1_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_task1_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_task1_stimuli* updates
            if odd_task1_stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task1_stimuli.frameNStart = frameN  # exact frame index
                odd_task1_stimuli.tStart = t  # local t and not account for scr refresh
                odd_task1_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task1_stimuli, 'tStartRefresh')  # time at next scr refresh
                odd_task1_stimuli.setAutoDraw(True)
            if odd_task1_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task1_stimuli.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task1_stimuli.tStop = t  # not accounting for scr refresh
                    odd_task1_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task1_stimuli, 'tStopRefresh')  # time at next scr refresh
                    odd_task1_stimuli.setAutoDraw(False)
            
            # *odd_task1_resp* updates
            waitOnFlip = False
            if odd_task1_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                odd_task1_resp.frameNStart = frameN  # exact frame index
                odd_task1_resp.tStart = t  # local t and not account for scr refresh
                odd_task1_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task1_resp, 'tStartRefresh')  # time at next scr refresh
                odd_task1_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(odd_task1_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(odd_task1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if odd_task1_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task1_resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task1_resp.tStop = t  # not accounting for scr refresh
                    odd_task1_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task1_resp, 'tStopRefresh')  # time at next scr refresh
                    odd_task1_resp.status = FINISHED
            if odd_task1_resp.status == STARTED and not waitOnFlip:
                theseKeys = odd_task1_resp.getKeys(keyList=['f', 'l'], waitRelease=False)
                _odd_task1_resp_allKeys.extend(theseKeys)
                if len(_odd_task1_resp_allKeys):
                    odd_task1_resp.keys = _odd_task1_resp_allKeys[-1].name  # just the last key pressed
                    odd_task1_resp.rt = _odd_task1_resp_allKeys[-1].rt
                    # was this correct?
                    if (odd_task1_resp.keys == str(odd_task1_answer)) or (odd_task1_resp.keys == odd_task1_answer):
                        odd_task1_resp.corr = 1
                    else:
                        odd_task1_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_task1_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_task1_trial"-------
        for thisComponent in odd_task1_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd1_task1.addData('odd_task1_stimuli.started', odd_task1_stimuli.tStartRefresh)
        odd1_task1.addData('odd_task1_stimuli.stopped', odd_task1_stimuli.tStopRefresh)
        # check responses
        if odd_task1_resp.keys in ['', [], None]:  # No response was made
            odd_task1_resp.keys = None
            # was no response the correct answer?!
            if str(odd_task1_answer).lower() == 'none':
                odd_task1_resp.corr = 1;  # correct non-response
            else:
                odd_task1_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for odd1_task1 (TrialHandler)
        odd1_task1.addData('odd_task1_resp.keys',odd_task1_resp.keys)
        odd1_task1.addData('odd_task1_resp.corr', odd_task1_resp.corr)
        returnValue.ex_record.append(odd_task1_resp.corr)
        if odd_task1_resp.keys != None:  # we had a response
            odd1_task1.addData('odd_task1_resp.rt', odd_task1_resp.rt)
        odd1_task1.addData('odd_task1_resp.started', odd_task1_resp.tStartRefresh)
        odd1_task1.addData('odd_task1_resp.stopped', odd_task1_resp.tStopRefresh)
        
        # ------Prepare to start Routine "odd_soa"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        odd_soaComponents = [odd_inerval]
        for thisComponent in odd_soaComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_soaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_soa"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_soaClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_soaClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_inerval* updates
            if odd_inerval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_inerval.frameNStart = frameN  # exact frame index
                odd_inerval.tStart = t  # local t and not account for scr refresh
                odd_inerval.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_inerval, 'tStartRefresh')  # time at next scr refresh
                odd_inerval.setAutoDraw(True)
            if odd_inerval.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_inerval.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_inerval.tStop = t  # not accounting for scr refresh
                    odd_inerval.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_inerval, 'tStopRefresh')  # time at next scr refresh
                    odd_inerval.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_soaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_soa"-------
        for thisComponent in odd_soaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd1_task1.addData('odd_inerval.started', odd_inerval.tStartRefresh)
        odd1_task1.addData('odd_inerval.stopped', odd_inerval.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'odd1_task1'


    # ------Prepare to start Routine "odd_rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    odd_rest_resp.keys = []
    odd_rest_resp.rt = []
    _odd_rest_resp_allKeys = []
    # keep track of which components have finished
    odd_restComponents = [odd_ex_rest, odd_restend, odd_rest_resp]
    for thisComponent in odd_restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    odd_restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "odd_rest"-------
    while continueRoutine:
        # get current time
        t = odd_restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=odd_restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *odd_ex_rest* updates
        if odd_ex_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            odd_ex_rest.frameNStart = frameN  # exact frame index
            odd_ex_rest.tStart = t  # local t and not account for scr refresh
            odd_ex_rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_ex_rest, 'tStartRefresh')  # time at next scr refresh
            odd_ex_rest.setAutoDraw(True)
        if odd_ex_rest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > odd_ex_rest.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                odd_ex_rest.tStop = t  # not accounting for scr refresh
                odd_ex_rest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(odd_ex_rest, 'tStopRefresh')  # time at next scr refresh
                odd_ex_rest.setAutoDraw(False)
        
        # *odd_restend* updates
        if odd_restend.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            odd_restend.frameNStart = frameN  # exact frame index
            odd_restend.tStart = t  # local t and not account for scr refresh
            odd_restend.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_restend, 'tStartRefresh')  # time at next scr refresh
            odd_restend.setAutoDraw(True)
        
        # *odd_rest_resp* updates
        waitOnFlip = False
        if odd_rest_resp.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            odd_rest_resp.frameNStart = frameN  # exact frame index
            odd_rest_resp.tStart = t  # local t and not account for scr refresh
            odd_rest_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_rest_resp, 'tStartRefresh')  # time at next scr refresh
            odd_rest_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(odd_rest_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(odd_rest_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if odd_rest_resp.status == STARTED and not waitOnFlip:
            theseKeys = odd_rest_resp.getKeys(keyList=['space'], waitRelease=False)
            _odd_rest_resp_allKeys.extend(theseKeys)
            if len(_odd_rest_resp_allKeys):
                odd_rest_resp.keys = _odd_rest_resp_allKeys[-1].name  # just the last key pressed
                odd_rest_resp.rt = _odd_rest_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in odd_restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "odd_rest"-------
    for thisComponent in odd_restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('odd_ex_rest.started', odd_ex_rest.tStartRefresh)
    thisExp.addData('odd_ex_rest.stopped', odd_ex_rest.tStopRefresh)
    thisExp.addData('odd_restend.started', odd_restend.tStartRefresh)
    thisExp.addData('odd_restend.stopped', odd_restend.tStopRefresh)
    # check responses
    if odd_rest_resp.keys in ['', [], None]:  # No response was made
        odd_rest_resp.keys = None
    thisExp.addData('odd_rest_resp.keys',odd_rest_resp.keys)
    if odd_rest_resp.keys != None:  # we had a response
        thisExp.addData('odd_rest_resp.rt', odd_rest_resp.rt)
    thisExp.addData('odd_rest_resp.started', odd_rest_resp.tStartRefresh)
    thisExp.addData('odd_rest_resp.stopped', odd_rest_resp.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "odd_rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    odd1_task2 = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tableResource/odd_task2.xlsx'),
        seed=None, name='odd1_task2')
    thisExp.addLoop(odd1_task2)  # add the loop to the experiment
    thisOdd1_task2 = odd1_task2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOdd1_task2.rgb)
    if thisOdd1_task2 != None:
        for paramName in thisOdd1_task2:
            exec('{} = thisOdd1_task2[paramName]'.format(paramName))

    for thisOdd1_task2 in odd1_task2:
        currentLoop = odd1_task2
        # abbreviate parameter names if possible (e.g. rgb = thisOdd1_task2.rgb)
        if thisOdd1_task2 != None:
            for paramName in thisOdd1_task2:
                exec('{} = thisOdd1_task2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "odd_ex_fix"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        odd_ex_fixComponents = [odd_task_fix]
        for thisComponent in odd_ex_fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_ex_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        odd_task2_color = thisOdd1_task2['odd_task2_color']
        odd_task2_name = thisOdd1_task2['odd_task2_name']
        odd_task2_answer = thisOdd1_task1['odd_task2_answer']
        # -------Run Routine "odd_ex_fix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_ex_fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_ex_fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_task_fix* updates
            if odd_task_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task_fix.frameNStart = frameN  # exact frame index
                odd_task_fix.tStart = t  # local t and not account for scr refresh
                odd_task_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task_fix, 'tStartRefresh')  # time at next scr refresh
                odd_task_fix.setAutoDraw(True)
            if odd_task_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task_fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task_fix.tStop = t  # not accounting for scr refresh
                    odd_task_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task_fix, 'tStopRefresh')  # time at next scr refresh
                    odd_task_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_ex_fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_ex_fix"-------
        for thisComponent in odd_ex_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd1_task2.addData('odd_task_fix.started', odd_task_fix.tStartRefresh)
        odd1_task2.addData('odd_task_fix.stopped', odd_task_fix.tStopRefresh)
        
        # ------Prepare to start Routine "odd_task2_trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        odd_task2_stimuli.setColor(odd_task2_color, colorSpace='rgb')
        odd_task2_stimuli.setText(odd_task2_name)
        odd_task2_resp.keys = []
        odd_task2_resp.rt = []
        _odd_task2_resp_allKeys = []
        # keep track of which components have finished
        odd_task2_trialComponents = [odd_task2_stimuli, odd_task2_resp]
        for thisComponent in odd_task2_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_task2_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_task2_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_task2_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_task2_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_task2_stimuli* updates
            if odd_task2_stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task2_stimuli.frameNStart = frameN  # exact frame index
                odd_task2_stimuli.tStart = t  # local t and not account for scr refresh
                odd_task2_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task2_stimuli, 'tStartRefresh')  # time at next scr refresh
                odd_task2_stimuli.setAutoDraw(True)
            if odd_task2_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task2_stimuli.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task2_stimuli.tStop = t  # not accounting for scr refresh
                    odd_task2_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task2_stimuli, 'tStopRefresh')  # time at next scr refresh
                    odd_task2_stimuli.setAutoDraw(False)
            
            # *odd_task2_resp* updates
            waitOnFlip = False
            if odd_task2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task2_resp.frameNStart = frameN  # exact frame index
                odd_task2_resp.tStart = t  # local t and not account for scr refresh
                odd_task2_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task2_resp, 'tStartRefresh')  # time at next scr refresh
                odd_task2_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(odd_task2_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(odd_task2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if odd_task2_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task2_resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task2_resp.tStop = t  # not accounting for scr refresh
                    odd_task2_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task2_resp, 'tStopRefresh')  # time at next scr refresh
                    odd_task2_resp.status = FINISHED
            if odd_task2_resp.status == STARTED and not waitOnFlip:
                theseKeys = odd_task2_resp.getKeys(keyList=['f', 'l'], waitRelease=False)
                _odd_task2_resp_allKeys.extend(theseKeys)
                if len(_odd_task2_resp_allKeys):
                    odd_task2_resp.keys = _odd_task2_resp_allKeys[-1].name  # just the last key pressed
                    odd_task2_resp.rt = _odd_task2_resp_allKeys[-1].rt
                    # was this correct?
                    if (odd_task2_resp.keys == str(odd_task2_answer)) or (odd_task2_resp.keys == odd_task2_answer):
                        odd_task2_resp.corr = 1
                    else:
                        odd_task2_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_task2_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_task2_trial"-------
        for thisComponent in odd_task2_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd1_task2.addData('odd_task2_stimuli.started', odd_task2_stimuli.tStartRefresh)
        odd1_task2.addData('odd_task2_stimuli.stopped', odd_task2_stimuli.tStopRefresh)
        # check responses
        if odd_task2_resp.keys in ['', [], None]:  # No response was made
            odd_task2_resp.keys = None
            # was no response the correct answer?!
            if str(odd_task2_answer).lower() == 'none':
                odd_task2_resp.corr = 1;  # correct non-response
            else:
                odd_task2_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for odd1_task2 (TrialHandler)
        odd1_task2.addData('odd_task2_resp.keys',odd_task2_resp.keys)
        odd1_task2.addData('odd_task2_resp.corr', odd_task2_resp.corr)
        returnValue.ex_record.append(odd_task2_resp.corr)
        if odd_task2_resp.keys != None:  # we had a response
            odd1_task2.addData('odd_task2_resp.rt', odd_task2_resp.rt)
        odd1_task2.addData('odd_task2_resp.started', odd_task2_resp.tStartRefresh)
        odd1_task2.addData('odd_task2_resp.stopped', odd_task2_resp.tStopRefresh)
        
        # ------Prepare to start Routine "odd_soa"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        odd_soaComponents = [odd_inerval]
        for thisComponent in odd_soaComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_soaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_soa"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_soaClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_soaClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_inerval* updates
            if odd_inerval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_inerval.frameNStart = frameN  # exact frame index
                odd_inerval.tStart = t  # local t and not account for scr refresh
                odd_inerval.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_inerval, 'tStartRefresh')  # time at next scr refresh
                odd_inerval.setAutoDraw(True)
            if odd_inerval.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_inerval.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_inerval.tStop = t  # not accounting for scr refresh
                    odd_inerval.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_inerval, 'tStopRefresh')  # time at next scr refresh
                    odd_inerval.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_soaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_soa"-------
        for thisComponent in odd_soaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd1_task2.addData('odd_inerval.started', odd_inerval.tStartRefresh)
        odd1_task2.addData('odd_inerval.stopped', odd_inerval.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'odd1_task2'


    # ------Prepare to start Routine "odd_rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    odd_rest_resp.keys = []
    odd_rest_resp.rt = []
    _odd_rest_resp_allKeys = []
    # keep track of which components have finished
    odd_restComponents = [odd_ex_rest, odd_restend, odd_rest_resp]
    for thisComponent in odd_restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    odd_restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "odd_rest"-------
    while continueRoutine:
        # get current time
        t = odd_restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=odd_restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *odd_ex_rest* updates
        if odd_ex_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            odd_ex_rest.frameNStart = frameN  # exact frame index
            odd_ex_rest.tStart = t  # local t and not account for scr refresh
            odd_ex_rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_ex_rest, 'tStartRefresh')  # time at next scr refresh
            odd_ex_rest.setAutoDraw(True)
        if odd_ex_rest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > odd_ex_rest.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                odd_ex_rest.tStop = t  # not accounting for scr refresh
                odd_ex_rest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(odd_ex_rest, 'tStopRefresh')  # time at next scr refresh
                odd_ex_rest.setAutoDraw(False)
        
        # *odd_restend* updates
        if odd_restend.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            odd_restend.frameNStart = frameN  # exact frame index
            odd_restend.tStart = t  # local t and not account for scr refresh
            odd_restend.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_restend, 'tStartRefresh')  # time at next scr refresh
            odd_restend.setAutoDraw(True)
        
        # *odd_rest_resp* updates
        waitOnFlip = False
        if odd_rest_resp.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            odd_rest_resp.frameNStart = frameN  # exact frame index
            odd_rest_resp.tStart = t  # local t and not account for scr refresh
            odd_rest_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_rest_resp, 'tStartRefresh')  # time at next scr refresh
            odd_rest_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(odd_rest_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(odd_rest_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if odd_rest_resp.status == STARTED and not waitOnFlip:
            theseKeys = odd_rest_resp.getKeys(keyList=['space'], waitRelease=False)
            _odd_rest_resp_allKeys.extend(theseKeys)
            if len(_odd_rest_resp_allKeys):
                odd_rest_resp.keys = _odd_rest_resp_allKeys[-1].name  # just the last key pressed
                odd_rest_resp.rt = _odd_rest_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in odd_restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "odd_rest"-------
    for thisComponent in odd_restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('odd_ex_rest.started', odd_ex_rest.tStartRefresh)
    thisExp.addData('odd_ex_rest.stopped', odd_ex_rest.tStopRefresh)
    thisExp.addData('odd_restend.started', odd_restend.tStartRefresh)
    thisExp.addData('odd_restend.stopped', odd_restend.tStopRefresh)
    # check responses
    if odd_rest_resp.keys in ['', [], None]:  # No response was made
        odd_rest_resp.keys = None
    thisExp.addData('odd_rest_resp.keys',odd_rest_resp.keys)
    if odd_rest_resp.keys != None:  # we had a response
        thisExp.addData('odd_rest_resp.rt', odd_rest_resp.rt)
    thisExp.addData('odd_rest_resp.started', odd_rest_resp.tStartRefresh)
    thisExp.addData('odd_rest_resp.stopped', odd_rest_resp.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "odd_rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    odd1_task3 = data.TrialHandler(nReps=2.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tableResource/odd_task3.xlsx'),
        seed=None, name='odd1_task3')
    thisExp.addLoop(odd1_task3)  # add the loop to the experiment
    thisOdd1_task3 = odd1_task3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOdd1_task3.rgb)
    if thisOdd1_task3 != None:
        for paramName in thisOdd1_task3:
            exec('{} = thisOdd1_task3[paramName]'.format(paramName))

    for thisOdd1_task3 in odd1_task3:
        currentLoop = odd1_task3
        # abbreviate parameter names if possible (e.g. rgb = thisOdd1_task3.rgb)
        if thisOdd1_task3 != None:
            for paramName in thisOdd1_task3:
                exec('{} = thisOdd1_task3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "odd_ex_fix"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        odd_ex_fixComponents = [odd_task_fix]
        for thisComponent in odd_ex_fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_ex_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        odd_task3_color = thisOdd1_task3['odd_task3_color']
        odd_task3_name = thisOdd1_task3['odd_task3_name']
        odd_task3_answer = thisOdd1_task3['odd_task3_answer']

        # -------Run Routine "odd_ex_fix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_ex_fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_ex_fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_task_fix* updates
            if odd_task_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task_fix.frameNStart = frameN  # exact frame index
                odd_task_fix.tStart = t  # local t and not account for scr refresh
                odd_task_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task_fix, 'tStartRefresh')  # time at next scr refresh
                odd_task_fix.setAutoDraw(True)
            if odd_task_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task_fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task_fix.tStop = t  # not accounting for scr refresh
                    odd_task_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task_fix, 'tStopRefresh')  # time at next scr refresh
                    odd_task_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_ex_fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_ex_fix"-------
        for thisComponent in odd_ex_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd1_task3.addData('odd_task_fix.started', odd_task_fix.tStartRefresh)
        odd1_task3.addData('odd_task_fix.stopped', odd_task_fix.tStopRefresh)
        
        # ------Prepare to start Routine "odd_task3_trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        odd_task3_stimuli.setColor(odd_task3_color, colorSpace='rgb')
        odd_task3_stimuli.setText(odd_task3_name)
        odd_task3_resp.keys = []
        odd_task3_resp.rt = []
        _odd_task3_resp_allKeys = []
        # keep track of which components have finished
        odd_task3_trialComponents = [odd_task3_stimuli, odd_task3_resp]
        for thisComponent in odd_task3_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_task3_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_task3_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_task3_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_task3_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_task3_stimuli* updates
            if odd_task3_stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task3_stimuli.frameNStart = frameN  # exact frame index
                odd_task3_stimuli.tStart = t  # local t and not account for scr refresh
                odd_task3_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task3_stimuli, 'tStartRefresh')  # time at next scr refresh
                odd_task3_stimuli.setAutoDraw(True)
            if odd_task3_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task3_stimuli.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task3_stimuli.tStop = t  # not accounting for scr refresh
                    odd_task3_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task3_stimuli, 'tStopRefresh')  # time at next scr refresh
                    odd_task3_stimuli.setAutoDraw(False)
            
            # *odd_task3_resp* updates
            waitOnFlip = False
            if odd_task3_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task3_resp.frameNStart = frameN  # exact frame index
                odd_task3_resp.tStart = t  # local t and not account for scr refresh
                odd_task3_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task3_resp, 'tStartRefresh')  # time at next scr refresh
                odd_task3_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(odd_task3_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(odd_task3_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if odd_task3_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task3_resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task3_resp.tStop = t  # not accounting for scr refresh
                    odd_task3_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task3_resp, 'tStopRefresh')  # time at next scr refresh
                    odd_task3_resp.status = FINISHED
            if odd_task3_resp.status == STARTED and not waitOnFlip:
                theseKeys = odd_task3_resp.getKeys(keyList=['f', 'l'], waitRelease=False)
                _odd_task3_resp_allKeys.extend(theseKeys)
                if len(_odd_task3_resp_allKeys):
                    odd_task3_resp.keys = _odd_task3_resp_allKeys[-1].name  # just the last key pressed
                    odd_task3_resp.rt = _odd_task3_resp_allKeys[-1].rt
                    # was this correct?
                    if (odd_task3_resp.keys == str(odd_task3_answer)) or (odd_task3_resp.keys == odd_task3_answer):
                        odd_task3_resp.corr = 1
                    else:
                        odd_task3_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_task3_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_task3_trial"-------
        for thisComponent in odd_task3_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd1_task3.addData('odd_task3_stimuli.started', odd_task3_stimuli.tStartRefresh)
        odd1_task3.addData('odd_task3_stimuli.stopped', odd_task3_stimuli.tStopRefresh)
        # check responses
        if odd_task3_resp.keys in ['', [], None]:  # No response was made
            odd_task3_resp.keys = None
            # was no response the correct answer?!
            if str(odd_task3_answer).lower() == 'none':
                odd_task3_resp.corr = 1;  # correct non-response
            else:
                odd_task3_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for odd1_task3 (TrialHandler)
        odd1_task3.addData('odd_task3_resp.keys',odd_task3_resp.keys)
        odd1_task3.addData('odd_task3_resp.corr', odd_task3_resp.corr)
        returnValue.ex_record.append(odd_task3_resp.corr)
        if odd_task3_resp.keys != None:  # we had a response
            odd1_task3.addData('odd_task3_resp.rt', odd_task3_resp.rt)
        odd1_task3.addData('odd_task3_resp.started', odd_task3_resp.tStartRefresh)
        odd1_task3.addData('odd_task3_resp.stopped', odd_task3_resp.tStopRefresh)
        
        # ------Prepare to start Routine "odd_soa"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        odd_soaComponents = [odd_inerval]
        for thisComponent in odd_soaComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_soaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_soa"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_soaClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_soaClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_inerval* updates
            if odd_inerval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_inerval.frameNStart = frameN  # exact frame index
                odd_inerval.tStart = t  # local t and not account for scr refresh
                odd_inerval.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_inerval, 'tStartRefresh')  # time at next scr refresh
                odd_inerval.setAutoDraw(True)
            if odd_inerval.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_inerval.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_inerval.tStop = t  # not accounting for scr refresh
                    odd_inerval.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_inerval, 'tStopRefresh')  # time at next scr refresh
                    odd_inerval.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_soaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_soa"-------
        for thisComponent in odd_soaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd1_task3.addData('odd_inerval.started', odd_inerval.tStartRefresh)
        odd1_task3.addData('odd_inerval.stopped', odd_inerval.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'odd1_task3'


    # ------Prepare to start Routine "odd_rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    odd_rest_resp.keys = []
    odd_rest_resp.rt = []
    _odd_rest_resp_allKeys = []
    # keep track of which components have finished
    odd_restComponents = [odd_ex_rest, odd_restend, odd_rest_resp]
    for thisComponent in odd_restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    odd_restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "odd_rest"-------
    while continueRoutine:
        # get current time
        t = odd_restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=odd_restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *odd_ex_rest* updates
        if odd_ex_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            odd_ex_rest.frameNStart = frameN  # exact frame index
            odd_ex_rest.tStart = t  # local t and not account for scr refresh
            odd_ex_rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_ex_rest, 'tStartRefresh')  # time at next scr refresh
            odd_ex_rest.setAutoDraw(True)
        if odd_ex_rest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > odd_ex_rest.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                odd_ex_rest.tStop = t  # not accounting for scr refresh
                odd_ex_rest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(odd_ex_rest, 'tStopRefresh')  # time at next scr refresh
                odd_ex_rest.setAutoDraw(False)
        
        # *odd_restend* updates
        if odd_restend.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            odd_restend.frameNStart = frameN  # exact frame index
            odd_restend.tStart = t  # local t and not account for scr refresh
            odd_restend.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_restend, 'tStartRefresh')  # time at next scr refresh
            odd_restend.setAutoDraw(True)
        
        # *odd_rest_resp* updates
        waitOnFlip = False
        if odd_rest_resp.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            odd_rest_resp.frameNStart = frameN  # exact frame index
            odd_rest_resp.tStart = t  # local t and not account for scr refresh
            odd_rest_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_rest_resp, 'tStartRefresh')  # time at next scr refresh
            odd_rest_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(odd_rest_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(odd_rest_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if odd_rest_resp.status == STARTED and not waitOnFlip:
            theseKeys = odd_rest_resp.getKeys(keyList=['space'], waitRelease=False)
            _odd_rest_resp_allKeys.extend(theseKeys)
            if len(_odd_rest_resp_allKeys):
                odd_rest_resp.keys = _odd_rest_resp_allKeys[-1].name  # just the last key pressed
                odd_rest_resp.rt = _odd_rest_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in odd_restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "odd_rest"-------
    for thisComponent in odd_restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('odd_ex_rest.started', odd_ex_rest.tStartRefresh)
    thisExp.addData('odd_ex_rest.stopped', odd_ex_rest.tStopRefresh)
    thisExp.addData('odd_restend.started', odd_restend.tStartRefresh)
    thisExp.addData('odd_restend.stopped', odd_restend.tStopRefresh)
    # check responses
    if odd_rest_resp.keys in ['', [], None]:  # No response was made
        odd_rest_resp.keys = None
    thisExp.addData('odd_rest_resp.keys',odd_rest_resp.keys)
    if odd_rest_resp.keys != None:  # we had a response
        thisExp.addData('odd_rest_resp.rt', odd_rest_resp.rt)
    thisExp.addData('odd_rest_resp.started', odd_rest_resp.tStartRefresh)
    thisExp.addData('odd_rest_resp.stopped', odd_rest_resp.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "odd_rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    odd2_task3 = data.TrialHandler(nReps=2.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tableResource/odd_task3.xlsx'),
        seed=None, name='odd2_task3')
    thisExp.addLoop(odd2_task3)  # add the loop to the experiment
    thisOdd2_task3 = odd2_task3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOdd2_task3.rgb)
    if thisOdd2_task3 != None:
        for paramName in thisOdd2_task3:
            exec('{} = thisOdd2_task3[paramName]'.format(paramName))

    for thisOdd2_task3 in odd2_task3:
        currentLoop = odd2_task3
        # abbreviate parameter names if possible (e.g. rgb = thisOdd2_task3.rgb)
        if thisOdd2_task3 != None:
            for paramName in thisOdd2_task3:
                exec('{} = thisOdd2_task3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "odd_ex_fix"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        odd_ex_fixComponents = [odd_task_fix]
        for thisComponent in odd_ex_fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_ex_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        odd_task3_color = thisOdd2_task3['odd_task3_color']
        odd_task3_name = thisOdd2_task3['odd_task3_name']
        odd_task3_answer = thisOdd2_task3['odd_task3_answer']
        
        # -------Run Routine "odd_ex_fix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_ex_fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_ex_fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_task_fix* updates
            if odd_task_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task_fix.frameNStart = frameN  # exact frame index
                odd_task_fix.tStart = t  # local t and not account for scr refresh
                odd_task_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task_fix, 'tStartRefresh')  # time at next scr refresh
                odd_task_fix.setAutoDraw(True)
            if odd_task_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task_fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task_fix.tStop = t  # not accounting for scr refresh
                    odd_task_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task_fix, 'tStopRefresh')  # time at next scr refresh
                    odd_task_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_ex_fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_ex_fix"-------
        for thisComponent in odd_ex_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd2_task3.addData('odd_task_fix.started', odd_task_fix.tStartRefresh)
        odd2_task3.addData('odd_task_fix.stopped', odd_task_fix.tStopRefresh)
        
        # ------Prepare to start Routine "odd_task3_trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        odd_task3_stimuli.setColor(odd_task3_color, colorSpace='rgb')
        odd_task3_stimuli.setText(odd_task3_name)
        odd_task3_resp.keys = []
        odd_task3_resp.rt = []
        _odd_task3_resp_allKeys = []
        # keep track of which components have finished
        odd_task3_trialComponents = [odd_task3_stimuli, odd_task3_resp]
        for thisComponent in odd_task3_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_task3_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_task3_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_task3_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_task3_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_task3_stimuli* updates
            if odd_task3_stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task3_stimuli.frameNStart = frameN  # exact frame index
                odd_task3_stimuli.tStart = t  # local t and not account for scr refresh
                odd_task3_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task3_stimuli, 'tStartRefresh')  # time at next scr refresh
                odd_task3_stimuli.setAutoDraw(True)
            if odd_task3_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task3_stimuli.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task3_stimuli.tStop = t  # not accounting for scr refresh
                    odd_task3_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task3_stimuli, 'tStopRefresh')  # time at next scr refresh
                    odd_task3_stimuli.setAutoDraw(False)
            
            # *odd_task3_resp* updates
            waitOnFlip = False
            if odd_task3_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task3_resp.frameNStart = frameN  # exact frame index
                odd_task3_resp.tStart = t  # local t and not account for scr refresh
                odd_task3_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task3_resp, 'tStartRefresh')  # time at next scr refresh
                odd_task3_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(odd_task3_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(odd_task3_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if odd_task3_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task3_resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task3_resp.tStop = t  # not accounting for scr refresh
                    odd_task3_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task3_resp, 'tStopRefresh')  # time at next scr refresh
                    odd_task3_resp.status = FINISHED
            if odd_task3_resp.status == STARTED and not waitOnFlip:
                theseKeys = odd_task3_resp.getKeys(keyList=['f', 'l'], waitRelease=False)
                _odd_task3_resp_allKeys.extend(theseKeys)
                if len(_odd_task3_resp_allKeys):
                    odd_task3_resp.keys = _odd_task3_resp_allKeys[-1].name  # just the last key pressed
                    odd_task3_resp.rt = _odd_task3_resp_allKeys[-1].rt
                    # was this correct?
                    if (odd_task3_resp.keys == str(odd_task3_answer)) or (odd_task3_resp.keys == odd_task3_answer):
                        odd_task3_resp.corr = 1
                    else:
                        odd_task3_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_task3_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_task3_trial"-------
        for thisComponent in odd_task3_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd2_task3.addData('odd_task3_stimuli.started', odd_task3_stimuli.tStartRefresh)
        odd2_task3.addData('odd_task3_stimuli.stopped', odd_task3_stimuli.tStopRefresh)
        # check responses
        if odd_task3_resp.keys in ['', [], None]:  # No response was made
            odd_task3_resp.keys = None
            # was no response the correct answer?!
            if str(odd_task3_answer).lower() == 'none':
                odd_task3_resp.corr = 1;  # correct non-response
            else:
                odd_task3_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for odd2_task3 (TrialHandler)
        odd2_task3.addData('odd_task3_resp.keys',odd_task3_resp.keys)
        odd2_task3.addData('odd_task3_resp.corr', odd_task3_resp.corr)
        returnValue.ex_record.append(odd_task3_resp.corr)
        if odd_task3_resp.keys != None:  # we had a response
            odd2_task3.addData('odd_task3_resp.rt', odd_task3_resp.rt)
        odd2_task3.addData('odd_task3_resp.started', odd_task3_resp.tStartRefresh)
        odd2_task3.addData('odd_task3_resp.stopped', odd_task3_resp.tStopRefresh)
        
        # ------Prepare to start Routine "odd_soa"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        odd_soaComponents = [odd_inerval]
        for thisComponent in odd_soaComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_soaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_soa"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_soaClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_soaClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_inerval* updates
            if odd_inerval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_inerval.frameNStart = frameN  # exact frame index
                odd_inerval.tStart = t  # local t and not account for scr refresh
                odd_inerval.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_inerval, 'tStartRefresh')  # time at next scr refresh
                odd_inerval.setAutoDraw(True)
            if odd_inerval.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_inerval.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_inerval.tStop = t  # not accounting for scr refresh
                    odd_inerval.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_inerval, 'tStopRefresh')  # time at next scr refresh
                    odd_inerval.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_soaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_soa"-------
        for thisComponent in odd_soaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd2_task3.addData('odd_inerval.started', odd_inerval.tStartRefresh)
        odd2_task3.addData('odd_inerval.stopped', odd_inerval.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'odd2_task3'


    # ------Prepare to start Routine "odd_rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    odd_rest_resp.keys = []
    odd_rest_resp.rt = []
    _odd_rest_resp_allKeys = []
    # keep track of which components have finished
    odd_restComponents = [odd_ex_rest, odd_restend, odd_rest_resp]
    for thisComponent in odd_restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    odd_restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "odd_rest"-------
    while continueRoutine:
        # get current time
        t = odd_restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=odd_restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *odd_ex_rest* updates
        if odd_ex_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            odd_ex_rest.frameNStart = frameN  # exact frame index
            odd_ex_rest.tStart = t  # local t and not account for scr refresh
            odd_ex_rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_ex_rest, 'tStartRefresh')  # time at next scr refresh
            odd_ex_rest.setAutoDraw(True)
        if odd_ex_rest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > odd_ex_rest.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                odd_ex_rest.tStop = t  # not accounting for scr refresh
                odd_ex_rest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(odd_ex_rest, 'tStopRefresh')  # time at next scr refresh
                odd_ex_rest.setAutoDraw(False)
        
        # *odd_restend* updates
        if odd_restend.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            odd_restend.frameNStart = frameN  # exact frame index
            odd_restend.tStart = t  # local t and not account for scr refresh
            odd_restend.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_restend, 'tStartRefresh')  # time at next scr refresh
            odd_restend.setAutoDraw(True)
        
        # *odd_rest_resp* updates
        waitOnFlip = False
        if odd_rest_resp.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            odd_rest_resp.frameNStart = frameN  # exact frame index
            odd_rest_resp.tStart = t  # local t and not account for scr refresh
            odd_rest_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_rest_resp, 'tStartRefresh')  # time at next scr refresh
            odd_rest_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(odd_rest_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(odd_rest_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if odd_rest_resp.status == STARTED and not waitOnFlip:
            theseKeys = odd_rest_resp.getKeys(keyList=['space'], waitRelease=False)
            _odd_rest_resp_allKeys.extend(theseKeys)
            if len(_odd_rest_resp_allKeys):
                odd_rest_resp.keys = _odd_rest_resp_allKeys[-1].name  # just the last key pressed
                odd_rest_resp.rt = _odd_rest_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in odd_restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "odd_rest"-------
    for thisComponent in odd_restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('odd_ex_rest.started', odd_ex_rest.tStartRefresh)
    thisExp.addData('odd_ex_rest.stopped', odd_ex_rest.tStopRefresh)
    thisExp.addData('odd_restend.started', odd_restend.tStartRefresh)
    thisExp.addData('odd_restend.stopped', odd_restend.tStopRefresh)
    # check responses
    if odd_rest_resp.keys in ['', [], None]:  # No response was made
        odd_rest_resp.keys = None
    thisExp.addData('odd_rest_resp.keys',odd_rest_resp.keys)
    if odd_rest_resp.keys != None:  # we had a response
        thisExp.addData('odd_rest_resp.rt', odd_rest_resp.rt)
    thisExp.addData('odd_rest_resp.started', odd_rest_resp.tStartRefresh)
    thisExp.addData('odd_rest_resp.stopped', odd_rest_resp.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "odd_rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    odd2_task2 = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tableResource/odd_task2.xlsx'),
        seed=None, name='odd2_task2')
    thisExp.addLoop(odd2_task2)  # add the loop to the experiment
    thisOdd2_task2 = odd2_task2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOdd2_task2.rgb)
    if thisOdd2_task2 != None:
        for paramName in thisOdd2_task2:
            exec('{} = thisOdd2_task2[paramName]'.format(paramName))

    for thisOdd2_task2 in odd2_task2:
        currentLoop = odd2_task2
        # abbreviate parameter names if possible (e.g. rgb = thisOdd2_task2.rgb)
        if thisOdd2_task2 != None:
            for paramName in thisOdd2_task2:
                exec('{} = thisOdd2_task2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "odd_ex_fix"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        odd_ex_fixComponents = [odd_task_fix]
        for thisComponent in odd_ex_fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_ex_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        odd_task2_color = thisOdd2_task2['odd_task2_color']
        odd_task2_name = thisOdd2_task2['odd_task2_name']
        odd_task2_answer = thisOdd2_task2['odd_task2_answer']
        # -------Run Routine "odd_ex_fix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_ex_fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_ex_fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_task_fix* updates
            if odd_task_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task_fix.frameNStart = frameN  # exact frame index
                odd_task_fix.tStart = t  # local t and not account for scr refresh
                odd_task_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task_fix, 'tStartRefresh')  # time at next scr refresh
                odd_task_fix.setAutoDraw(True)
            if odd_task_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task_fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task_fix.tStop = t  # not accounting for scr refresh
                    odd_task_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task_fix, 'tStopRefresh')  # time at next scr refresh
                    odd_task_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_ex_fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_ex_fix"-------
        for thisComponent in odd_ex_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd2_task2.addData('odd_task_fix.started', odd_task_fix.tStartRefresh)
        odd2_task2.addData('odd_task_fix.stopped', odd_task_fix.tStopRefresh)
        
        # ------Prepare to start Routine "odd_task2_trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        odd_task2_stimuli.setColor(odd_task2_color, colorSpace='rgb')
        odd_task2_stimuli.setText(odd_task2_name)
        odd_task2_resp.keys = []
        odd_task2_resp.rt = []
        _odd_task2_resp_allKeys = []
        # keep track of which components have finished
        odd_task2_trialComponents = [odd_task2_stimuli, odd_task2_resp]
        for thisComponent in odd_task2_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_task2_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_task2_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_task2_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_task2_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_task2_stimuli* updates
            if odd_task2_stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task2_stimuli.frameNStart = frameN  # exact frame index
                odd_task2_stimuli.tStart = t  # local t and not account for scr refresh
                odd_task2_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task2_stimuli, 'tStartRefresh')  # time at next scr refresh
                odd_task2_stimuli.setAutoDraw(True)
            if odd_task2_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task2_stimuli.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task2_stimuli.tStop = t  # not accounting for scr refresh
                    odd_task2_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task2_stimuli, 'tStopRefresh')  # time at next scr refresh
                    odd_task2_stimuli.setAutoDraw(False)
            
            # *odd_task2_resp* updates
            waitOnFlip = False
            if odd_task2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task2_resp.frameNStart = frameN  # exact frame index
                odd_task2_resp.tStart = t  # local t and not account for scr refresh
                odd_task2_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task2_resp, 'tStartRefresh')  # time at next scr refresh
                odd_task2_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(odd_task2_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(odd_task2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if odd_task2_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task2_resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task2_resp.tStop = t  # not accounting for scr refresh
                    odd_task2_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task2_resp, 'tStopRefresh')  # time at next scr refresh
                    odd_task2_resp.status = FINISHED
            if odd_task2_resp.status == STARTED and not waitOnFlip:
                theseKeys = odd_task2_resp.getKeys(keyList=['f', 'l'], waitRelease=False)
                _odd_task2_resp_allKeys.extend(theseKeys)
                if len(_odd_task2_resp_allKeys):
                    odd_task2_resp.keys = _odd_task2_resp_allKeys[-1].name  # just the last key pressed
                    odd_task2_resp.rt = _odd_task2_resp_allKeys[-1].rt
                    # was this correct?
                    if (odd_task2_resp.keys == str(odd_task2_answer)) or (odd_task2_resp.keys == odd_task2_answer):
                        odd_task2_resp.corr = 1
                    else:
                        odd_task2_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_task2_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_task2_trial"-------
        for thisComponent in odd_task2_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd2_task2.addData('odd_task2_stimuli.started', odd_task2_stimuli.tStartRefresh)
        odd2_task2.addData('odd_task2_stimuli.stopped', odd_task2_stimuli.tStopRefresh)
        # check responses
        if odd_task2_resp.keys in ['', [], None]:  # No response was made
            odd_task2_resp.keys = None
            # was no response the correct answer?!
            if str(odd_task2_answer).lower() == 'none':
                odd_task2_resp.corr = 1;  # correct non-response
            else:
                odd_task2_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for odd2_task2 (TrialHandler)
        odd2_task2.addData('odd_task2_resp.keys',odd_task2_resp.keys)
        odd2_task2.addData('odd_task2_resp.corr', odd_task2_resp.corr)
        returnValue.ex_record.append(odd_task2_resp.corr)
        if odd_task2_resp.keys != None:  # we had a response
            odd2_task2.addData('odd_task2_resp.rt', odd_task2_resp.rt)
        odd2_task2.addData('odd_task2_resp.started', odd_task2_resp.tStartRefresh)
        odd2_task2.addData('odd_task2_resp.stopped', odd_task2_resp.tStopRefresh)
        
        # ------Prepare to start Routine "odd_soa"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        odd_soaComponents = [odd_inerval]
        for thisComponent in odd_soaComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_soaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_soa"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_soaClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_soaClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_inerval* updates
            if odd_inerval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_inerval.frameNStart = frameN  # exact frame index
                odd_inerval.tStart = t  # local t and not account for scr refresh
                odd_inerval.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_inerval, 'tStartRefresh')  # time at next scr refresh
                odd_inerval.setAutoDraw(True)
            if odd_inerval.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_inerval.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_inerval.tStop = t  # not accounting for scr refresh
                    odd_inerval.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_inerval, 'tStopRefresh')  # time at next scr refresh
                    odd_inerval.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_soaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_soa"-------
        for thisComponent in odd_soaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd2_task2.addData('odd_inerval.started', odd_inerval.tStartRefresh)
        odd2_task2.addData('odd_inerval.stopped', odd_inerval.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'odd2_task2'


    # set up handler to look after randomisation of conditions etc
    odd2_task1 = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tableResource/odd_task1.xlsx'),
        seed=None, name='odd2_task1')
    thisExp.addLoop(odd2_task1)  # add the loop to the experiment
    thisOdd2_task1 = odd2_task1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOdd2_task1.rgb)
    if thisOdd2_task1 != None:
        for paramName in thisOdd2_task1:
            exec('{} = thisOdd2_task1[paramName]'.format(paramName))

    for thisOdd2_task1 in odd2_task1:
        currentLoop = odd2_task1
        # abbreviate parameter names if possible (e.g. rgb = thisOdd2_task1.rgb)
        if thisOdd2_task1 != None:
            for paramName in thisOdd2_task1:
                exec('{} = thisOdd2_task1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "odd_ex_fix"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        odd_ex_fixComponents = [odd_task_fix]
        for thisComponent in odd_ex_fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_ex_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        odd_task1_color = thisOdd2_task1['odd_task1_color']
        odd_task1_name = thisOdd2_task1['odd_task1_name']
        odd_task1_answer = thisOdd2_task1['odd_task1_answer']
        # -------Run Routine "odd_ex_fix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_ex_fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_ex_fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_task_fix* updates
            if odd_task_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task_fix.frameNStart = frameN  # exact frame index
                odd_task_fix.tStart = t  # local t and not account for scr refresh
                odd_task_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task_fix, 'tStartRefresh')  # time at next scr refresh
                odd_task_fix.setAutoDraw(True)
            if odd_task_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task_fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task_fix.tStop = t  # not accounting for scr refresh
                    odd_task_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task_fix, 'tStopRefresh')  # time at next scr refresh
                    odd_task_fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_ex_fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_ex_fix"-------
        for thisComponent in odd_ex_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd2_task1.addData('odd_task_fix.started', odd_task_fix.tStartRefresh)
        odd2_task1.addData('odd_task_fix.stopped', odd_task_fix.tStopRefresh)
        
        # ------Prepare to start Routine "odd_task1_trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        odd_task1_stimuli.setColor(odd_task1_color, colorSpace='rgb')
        odd_task1_stimuli.setText(odd_task1_name)
        odd_task1_resp.keys = []
        odd_task1_resp.rt = []
        _odd_task1_resp_allKeys = []
        # keep track of which components have finished
        odd_task1_trialComponents = [odd_task1_stimuli, odd_task1_resp]
        for thisComponent in odd_task1_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_task1_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_task1_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_task1_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_task1_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_task1_stimuli* updates
            if odd_task1_stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_task1_stimuli.frameNStart = frameN  # exact frame index
                odd_task1_stimuli.tStart = t  # local t and not account for scr refresh
                odd_task1_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task1_stimuli, 'tStartRefresh')  # time at next scr refresh
                odd_task1_stimuli.setAutoDraw(True)
            if odd_task1_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task1_stimuli.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task1_stimuli.tStop = t  # not accounting for scr refresh
                    odd_task1_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task1_stimuli, 'tStopRefresh')  # time at next scr refresh
                    odd_task1_stimuli.setAutoDraw(False)
            
            # *odd_task1_resp* updates
            waitOnFlip = False
            if odd_task1_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                odd_task1_resp.frameNStart = frameN  # exact frame index
                odd_task1_resp.tStart = t  # local t and not account for scr refresh
                odd_task1_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_task1_resp, 'tStartRefresh')  # time at next scr refresh
                odd_task1_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(odd_task1_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(odd_task1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if odd_task1_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_task1_resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_task1_resp.tStop = t  # not accounting for scr refresh
                    odd_task1_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_task1_resp, 'tStopRefresh')  # time at next scr refresh
                    odd_task1_resp.status = FINISHED
            if odd_task1_resp.status == STARTED and not waitOnFlip:
                theseKeys = odd_task1_resp.getKeys(keyList=['f', 'l'], waitRelease=False)
                _odd_task1_resp_allKeys.extend(theseKeys)
                if len(_odd_task1_resp_allKeys):
                    odd_task1_resp.keys = _odd_task1_resp_allKeys[-1].name  # just the last key pressed
                    odd_task1_resp.rt = _odd_task1_resp_allKeys[-1].rt
                    # was this correct?
                    if (odd_task1_resp.keys == str(odd_task1_answer)) or (odd_task1_resp.keys == odd_task1_answer):
                        odd_task1_resp.corr = 1
                    else:
                        odd_task1_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_task1_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_task1_trial"-------
        for thisComponent in odd_task1_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd2_task1.addData('odd_task1_stimuli.started', odd_task1_stimuli.tStartRefresh)
        odd2_task1.addData('odd_task1_stimuli.stopped', odd_task1_stimuli.tStopRefresh)
        # check responses
        if odd_task1_resp.keys in ['', [], None]:  # No response was made
            odd_task1_resp.keys = None
            # was no response the correct answer?!
            if str(odd_task1_answer).lower() == 'none':
                odd_task1_resp.corr = 1;  # correct non-response
            else:
                odd_task1_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for odd2_task1 (TrialHandler)
        odd2_task1.addData('odd_task1_resp.keys',odd_task1_resp.keys)
        odd2_task1.addData('odd_task1_resp.corr', odd_task1_resp.corr)
        returnValue.ex_record.append(odd_task1_resp.corr)
        if odd_task1_resp.keys != None:  # we had a response
            odd2_task1.addData('odd_task1_resp.rt', odd_task1_resp.rt)
        odd2_task1.addData('odd_task1_resp.started', odd_task1_resp.tStartRefresh)
        odd2_task1.addData('odd_task1_resp.stopped', odd_task1_resp.tStopRefresh)
        
        # ------Prepare to start Routine "odd_soa"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        odd_soaComponents = [odd_inerval]
        for thisComponent in odd_soaComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        odd_soaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "odd_soa"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = odd_soaClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=odd_soaClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *odd_inerval* updates
            if odd_inerval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                odd_inerval.frameNStart = frameN  # exact frame index
                odd_inerval.tStart = t  # local t and not account for scr refresh
                odd_inerval.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(odd_inerval, 'tStartRefresh')  # time at next scr refresh
                odd_inerval.setAutoDraw(True)
            if odd_inerval.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > odd_inerval.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    odd_inerval.tStop = t  # not accounting for scr refresh
                    odd_inerval.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(odd_inerval, 'tStopRefresh')  # time at next scr refresh
                    odd_inerval.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in odd_soaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "odd_soa"-------
        for thisComponent in odd_soaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        odd2_task1.addData('odd_inerval.started', odd_inerval.tStartRefresh)
        odd2_task1.addData('odd_inerval.stopped', odd_inerval.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'odd2_task1'


    # ------Prepare to start Routine "odd_end"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    odd_endComponents = [odd_endtext]
    for thisComponent in odd_endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    odd_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "odd_end"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = odd_endClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=odd_endClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *odd_endtext* updates
        if odd_endtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            odd_endtext.frameNStart = frameN  # exact frame index
            odd_endtext.tStart = t  # local t and not account for scr refresh
            odd_endtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(odd_endtext, 'tStartRefresh')  # time at next scr refresh
            odd_endtext.setAutoDraw(True)
        if odd_endtext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > odd_endtext.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                odd_endtext.tStop = t  # not accounting for scr refresh
                odd_endtext.frameNStop = frameN  # exact frame index
                win.timeOnFlip(odd_endtext, 'tStopRefresh')  # time at next scr refresh
                odd_endtext.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in odd_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "odd_end"-------
    for thisComponent in odd_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('odd_endtext.started', odd_endtext.tStartRefresh)
    thisExp.addData('odd_endtext.stopped', odd_endtext.tStopRefresh)

    # Flip one final time so any remaining win.callOnFlip() 
    # and win.timeOnFlip() tasks get executed before quitting
    win.flip()

    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename+'.csv', delim='auto')
    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    win.close()
    return returnValue
