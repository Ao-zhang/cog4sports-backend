#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 一月 29, 2022, at 11:31
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

target1=["←", "→"]
target2=["←←←←←", "→→→→→"]
target3=["←←→←←", "→→←→→"]
distractor_imgs=['materials/up.png','materials/down.png','materials/left.png','materials/right.png']

target1=["←", "→"]
target2=["←←←←←", "→→→→→"]
target3=["←←→←←", "→→←→→"]
distractor_imgs=['materials/up.png','materials/down.png','materials/left.png','materials/right.png']

target1=["←", "→"]
target2=["←←←←←", "→→→→→"]
target3=["←←→←←", "→→←→→"]
distractor_imgs=['materials/up.png','materials/down.png','materials/left.png','materials/right.png']


def ant(admin,participant,session):
    # Ensure that relative paths start from the same directory as this script
    # _thisDir = os.path.dirname(os.path.abspath(__file__))
    # os.chdir(_thisDir)
    _thisDir="."

    # Store info about the experiment session
    psychopyVersion = '2021.2.3'
    expName = 'program'  # from the Builder filename that created this script
    expInfo = {'participant': '', 'session': '001'}
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName
    expInfo['psychopyVersion'] = psychopyVersion

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data/ant/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\yd\\TB\\ANT\\program.py',
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
        size=[1360, 768], fullscr=False, screen=0, 
        winType='pyglet', allowGUI=False, allowStencil=False,
        monitor='testMonitor', color='white', colorSpace='rgb',
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

    # Initialize components for Routine "intro"
    introClock = core.Clock()
    image_intro = visual.ImageStim(
        win=win,
        name='image_intro', 
        image='materials/幻灯片1.png', mask=None,
        ori=0.0, pos=(0, 0), size=(1.8, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp = keyboard.Keyboard()

    # Initialize components for Routine "fixation"
    fixationClock = core.Clock()
    image_fixation = visual.ImageStim(
        win=win,
        name='image_fixation', 
        image='materials/fixation.png', mask=None,
        ori=0.0, pos=(0, 0), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)

    # Initialize components for Routine "trial"
    trialClock = core.Clock()
    image_fix = visual.ImageStim(
        win=win,
        name='image_fix', 
        image='materials/fixation.png', mask=None,
        ori=0.0, pos=(0, 0), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    image_dis1 = visual.ImageStim(
        win=win,
        name='image_dis1', 
        image='sin', mask=None,
        ori=0.0, pos=(0, 0.25), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_dis2 = visual.ImageStim(
        win=win,
        name='image_dis2', 
        image='sin', mask=None,
        ori=0.0, pos=(0, -0.25), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    image_dis3 = visual.ImageStim(
        win=win,
        name='image_dis3', 
        image='sin', mask=None,
        ori=0.0, pos=(0, 0), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    text = visual.TextStim(win=win, name='text',
        text='←←←←←',
        font='Open Sans',
        pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    key_resp_2 = keyboard.Keyboard()

    # Initialize components for Routine "feedback"
    feedbackClock = core.Clock()
    text_fb = visual.TextStim(win=win, name='text_fb',
        text='正确',
        font='Open Sans',
        pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "semi_intro"
    semi_introClock = core.Clock()
    image_semi = visual.ImageStim(
        win=win,
        name='image_semi', 
        image='materials/幻灯片2.png', mask=None,
        ori=0.0, pos=(0, 0), size=(1.8, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_3 = keyboard.Keyboard()

    # Initialize components for Routine "fixation"
    fixationClock = core.Clock()
    image_fixation = visual.ImageStim(
        win=win,
        name='image_fixation', 
        image='materials/fixation.png', mask=None,
        ori=0.0, pos=(0, 0), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)

    # Initialize components for Routine "trial"
    trialClock = core.Clock()
    image_fix = visual.ImageStim(
        win=win,
        name='image_fix', 
        image='materials/fixation.png', mask=None,
        ori=0.0, pos=(0, 0), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    image_dis1 = visual.ImageStim(
        win=win,
        name='image_dis1', 
        image='sin', mask=None,
        ori=0.0, pos=(0, 0.25), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_dis2 = visual.ImageStim(
        win=win,
        name='image_dis2', 
        image='sin', mask=None,
        ori=0.0, pos=(0, -0.25), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    image_dis3 = visual.ImageStim(
        win=win,
        name='image_dis3', 
        image='sin', mask=None,
        ori=0.0, pos=(0, 0), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    text = visual.TextStim(win=win, name='text',
        text='←←←←←',
        font='Open Sans',
        pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    key_resp_2 = keyboard.Keyboard()

    # Initialize components for Routine "rest"
    restClock = core.Clock()
    image_rest = visual.ImageStim(
        win=win,
        name='image_rest', 
        image='materials/幻灯片3.png', mask=None,
        ori=0.0, pos=(0, 0), size=(1.8, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_4 = keyboard.Keyboard()

    # Initialize components for Routine "fixation"
    fixationClock = core.Clock()
    image_fixation = visual.ImageStim(
        win=win,
        name='image_fixation', 
        image='materials/fixation.png', mask=None,
        ori=0.0, pos=(0, 0), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)

    # Initialize components for Routine "trial"
    trialClock = core.Clock()
    image_fix = visual.ImageStim(
        win=win,
        name='image_fix', 
        image='materials/fixation.png', mask=None,
        ori=0.0, pos=(0, 0), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    image_dis1 = visual.ImageStim(
        win=win,
        name='image_dis1', 
        image='sin', mask=None,
        ori=0.0, pos=(0, 0.25), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_dis2 = visual.ImageStim(
        win=win,
        name='image_dis2', 
        image='sin', mask=None,
        ori=0.0, pos=(0, -0.25), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    image_dis3 = visual.ImageStim(
        win=win,
        name='image_dis3', 
        image='sin', mask=None,
        ori=0.0, pos=(0, 0), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    text = visual.TextStim(win=win, name='text',
        text='←←←←←',
        font='Open Sans',
        pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    key_resp_2 = keyboard.Keyboard()

    # Initialize components for Routine "ending"
    endingClock = core.Clock()
    text_end = visual.TextStim(win=win, name='text_end',
        text='实验结束，感谢参与！',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    # ------Prepare to start Routine "intro"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    introComponents = [image_intro, key_resp]
    for thisComponent in introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "intro"-------
    while continueRoutine:
        # get current time
        t = introClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=introClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_intro* updates
        if image_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_intro.frameNStart = frameN  # exact frame index
            image_intro.tStart = t  # local t and not account for scr refresh
            image_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_intro, 'tStartRefresh')  # time at next scr refresh
            image_intro.setAutoDraw(True)
        
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
        for thisComponent in introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "intro"-------
    for thisComponent in introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    practice = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('materials/trialList.xlsx'),
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
        
        # ------Prepare to start Routine "fixation"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [image_fixation]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixation"-------
        while continueRoutine:
            # get current time
            t = fixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_fixation* updates
            if image_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_fixation.frameNStart = frameN  # exact frame index
                image_fixation.tStart = t  # local t and not account for scr refresh
                image_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_fixation, 'tStartRefresh')  # time at next scr refresh
                image_fixation.setAutoDraw(True)
            if image_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_fixation.tStartRefresh + 0.4*(np.random.choice([1,2,3,4]))-frameTolerance:
                    # keep track of stop time/frame for later
                    image_fixation.tStop = t  # not accounting for scr refresh
                    image_fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_fixation, 'tStopRefresh')  # time at next scr refresh
                    image_fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice.addData('image_fixation.started', image_fixation.tStartRefresh)
        practice.addData('image_fixation.stopped', image_fixation.tStopRefresh)
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        image_dis1.setImage('materials/blank.png')
        image_dis2.setImage('materials/blank.png')
        image_dis3.setImage('materials/fixation.png')
        text.setPos(loc)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        if target=="单箭头":
            thisTarget=np.random.choice(target1)
        elif target=="一致":
            thisTarget=np.random.choice(target2)
        elif target=="不一致":
            thisTarget=np.random.choice(target3)
        
        if distractor_type=="中心点":
            thisDistractor=np.random.choice(distractor_imgs)
            image_dis3.setImage(thisDistractor)
        elif distractor_type=="上下同时" or distractor_type=="上下分别":
            thisDistractors=np.random.choice(distractor_imgs,2)
            image_dis1.setImage(thisDistractors[0])
            image_dis2.setImage(thisDistractors[1])
        
        text.setText(thisTarget)
        # keep track of which components have finished
        trialComponents = [image_fix, image_dis1, image_dis2, image_dis3, text, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_fix* updates
            if image_fix.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                image_fix.frameNStart = frameN  # exact frame index
                image_fix.tStart = t  # local t and not account for scr refresh
                image_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_fix, 'tStartRefresh')  # time at next scr refresh
                image_fix.setAutoDraw(True)
            if image_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_fix.tStartRefresh + 2.1-frameTolerance:
                    # keep track of stop time/frame for later
                    image_fix.tStop = t  # not accounting for scr refresh
                    image_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_fix, 'tStopRefresh')  # time at next scr refresh
                    image_fix.setAutoDraw(False)
            
            # *image_dis1* updates
            if image_dis1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_dis1.frameNStart = frameN  # exact frame index
                image_dis1.tStart = t  # local t and not account for scr refresh
                image_dis1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_dis1, 'tStartRefresh')  # time at next scr refresh
                image_dis1.setAutoDraw(True)
            if image_dis1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_dis1.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    image_dis1.tStop = t  # not accounting for scr refresh
                    image_dis1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_dis1, 'tStopRefresh')  # time at next scr refresh
                    image_dis1.setAutoDraw(False)
            
            # *image_dis2* updates
            if image_dis2.status == NOT_STARTED and tThisFlip >= onset-frameTolerance:
                # keep track of start time/frame for later
                image_dis2.frameNStart = frameN  # exact frame index
                image_dis2.tStart = t  # local t and not account for scr refresh
                image_dis2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_dis2, 'tStartRefresh')  # time at next scr refresh
                image_dis2.setAutoDraw(True)
            if image_dis2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_dis2.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    image_dis2.tStop = t  # not accounting for scr refresh
                    image_dis2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_dis2, 'tStopRefresh')  # time at next scr refresh
                    image_dis2.setAutoDraw(False)
            
            # *image_dis3* updates
            if image_dis3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_dis3.frameNStart = frameN  # exact frame index
                image_dis3.tStart = t  # local t and not account for scr refresh
                image_dis3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_dis3, 'tStartRefresh')  # time at next scr refresh
                image_dis3.setAutoDraw(True)
            if image_dis3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_dis3.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    image_dis3.tStop = t  # not accounting for scr refresh
                    image_dis3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_dis3, 'tStopRefresh')  # time at next scr refresh
                    image_dis3.setAutoDraw(False)
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1.7-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 1.7-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        practice.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            practice.addData('key_resp_2.rt', key_resp_2.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedback"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        if thisTarget in ["←","←←←←←","→→←→→"]:
            if key_resp_2.keys == "left":
                text_fb.setText("正确")
                text_fb.setColor("green")
            else:
                text_fb.setText("错误")
                text_fb.setColor("red")
        elif thisTarget in ["→","→→→→→","←←→←←"]:
            if key_resp_2.keys == "right":
                text_fb.setText("正确")
                text_fb.setColor("green")
            else:
                text_fb.setText("错误")
                text_fb.setColor("red")
        # keep track of which components have finished
        feedbackComponents = [text_fb]
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
            
            # *text_fb* updates
            if text_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_fb.frameNStart = frameN  # exact frame index
                text_fb.tStart = t  # local t and not account for scr refresh
                text_fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_fb, 'tStartRefresh')  # time at next scr refresh
                text_fb.setAutoDraw(True)
            if text_fb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_fb.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_fb.tStop = t  # not accounting for scr refresh
                    text_fb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_fb, 'tStopRefresh')  # time at next scr refresh
                    text_fb.setAutoDraw(False)
            
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
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practice'


    # ------Prepare to start Routine "semi_intro"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    semi_introComponents = [image_semi, key_resp_3]
    for thisComponent in semi_introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    semi_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "semi_intro"-------
    while continueRoutine:
        # get current time
        t = semi_introClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=semi_introClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_semi* updates
        if image_semi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_semi.frameNStart = frameN  # exact frame index
            image_semi.tStart = t  # local t and not account for scr refresh
            image_semi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_semi, 'tStartRefresh')  # time at next scr refresh
            image_semi.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in semi_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "semi_intro"-------
    for thisComponent in semi_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "semi_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('materials/trialList.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixation"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [image_fixation]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixation"-------
        while continueRoutine:
            # get current time
            t = fixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_fixation* updates
            if image_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_fixation.frameNStart = frameN  # exact frame index
                image_fixation.tStart = t  # local t and not account for scr refresh
                image_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_fixation, 'tStartRefresh')  # time at next scr refresh
                image_fixation.setAutoDraw(True)
            if image_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_fixation.tStartRefresh + 0.4*(np.random.choice([1,2,3,4]))-frameTolerance:
                    # keep track of stop time/frame for later
                    image_fixation.tStop = t  # not accounting for scr refresh
                    image_fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_fixation, 'tStopRefresh')  # time at next scr refresh
                    image_fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('image_fixation.started', image_fixation.tStartRefresh)
        trials.addData('image_fixation.stopped', image_fixation.tStopRefresh)
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        image_dis1.setImage('materials/blank.png')
        image_dis2.setImage('materials/blank.png')
        image_dis3.setImage('materials/fixation.png')
        text.setPos(loc)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        if target=="单箭头":
            thisTarget=np.random.choice(target1)
        elif target=="一致":
            thisTarget=np.random.choice(target2)
        elif target=="不一致":
            thisTarget=np.random.choice(target3)
        
        if distractor_type=="中心点":
            thisDistractor=np.random.choice(distractor_imgs)
            image_dis3.setImage(thisDistractor)
        elif distractor_type=="上下同时" or distractor_type=="上下分别":
            thisDistractors=np.random.choice(distractor_imgs,2)
            image_dis1.setImage(thisDistractors[0])
            image_dis2.setImage(thisDistractors[1])
        
        text.setText(thisTarget)
        # keep track of which components have finished
        trialComponents = [image_fix, image_dis1, image_dis2, image_dis3, text, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_fix* updates
            if image_fix.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                image_fix.frameNStart = frameN  # exact frame index
                image_fix.tStart = t  # local t and not account for scr refresh
                image_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_fix, 'tStartRefresh')  # time at next scr refresh
                image_fix.setAutoDraw(True)
            if image_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_fix.tStartRefresh + 2.1-frameTolerance:
                    # keep track of stop time/frame for later
                    image_fix.tStop = t  # not accounting for scr refresh
                    image_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_fix, 'tStopRefresh')  # time at next scr refresh
                    image_fix.setAutoDraw(False)
            
            # *image_dis1* updates
            if image_dis1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_dis1.frameNStart = frameN  # exact frame index
                image_dis1.tStart = t  # local t and not account for scr refresh
                image_dis1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_dis1, 'tStartRefresh')  # time at next scr refresh
                image_dis1.setAutoDraw(True)
            if image_dis1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_dis1.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    image_dis1.tStop = t  # not accounting for scr refresh
                    image_dis1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_dis1, 'tStopRefresh')  # time at next scr refresh
                    image_dis1.setAutoDraw(False)
            
            # *image_dis2* updates
            if image_dis2.status == NOT_STARTED and tThisFlip >= onset-frameTolerance:
                # keep track of start time/frame for later
                image_dis2.frameNStart = frameN  # exact frame index
                image_dis2.tStart = t  # local t and not account for scr refresh
                image_dis2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_dis2, 'tStartRefresh')  # time at next scr refresh
                image_dis2.setAutoDraw(True)
            if image_dis2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_dis2.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    image_dis2.tStop = t  # not accounting for scr refresh
                    image_dis2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_dis2, 'tStopRefresh')  # time at next scr refresh
                    image_dis2.setAutoDraw(False)
            
            # *image_dis3* updates
            if image_dis3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_dis3.frameNStart = frameN  # exact frame index
                image_dis3.tStart = t  # local t and not account for scr refresh
                image_dis3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_dis3, 'tStartRefresh')  # time at next scr refresh
                image_dis3.setAutoDraw(True)
            if image_dis3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_dis3.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    image_dis3.tStop = t  # not accounting for scr refresh
                    image_dis3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_dis3, 'tStopRefresh')  # time at next scr refresh
                    image_dis3.setAutoDraw(False)
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1.7-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 1.7-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        trials.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            trials.addData('key_resp_2.rt', key_resp_2.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'


    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    restComponents = [image_rest, key_resp_4]
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
    while continueRoutine:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_rest* updates
        if image_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_rest.frameNStart = frameN  # exact frame index
            image_rest.tStart = t  # local t and not account for scr refresh
            image_rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_rest, 'tStartRefresh')  # time at next scr refresh
            image_rest.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
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
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('materials/trialList.xlsx'),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))

    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixation"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [image_fixation]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixation"-------
        while continueRoutine:
            # get current time
            t = fixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_fixation* updates
            if image_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_fixation.frameNStart = frameN  # exact frame index
                image_fixation.tStart = t  # local t and not account for scr refresh
                image_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_fixation, 'tStartRefresh')  # time at next scr refresh
                image_fixation.setAutoDraw(True)
            if image_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_fixation.tStartRefresh + 0.4*(np.random.choice([1,2,3,4]))-frameTolerance:
                    # keep track of stop time/frame for later
                    image_fixation.tStop = t  # not accounting for scr refresh
                    image_fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_fixation, 'tStopRefresh')  # time at next scr refresh
                    image_fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('image_fixation.started', image_fixation.tStartRefresh)
        trials_2.addData('image_fixation.stopped', image_fixation.tStopRefresh)
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        image_dis1.setImage('materials/blank.png')
        image_dis2.setImage('materials/blank.png')
        image_dis3.setImage('materials/fixation.png')
        text.setPos(loc)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        if target=="单箭头":
            thisTarget=np.random.choice(target1)
        elif target=="一致":
            thisTarget=np.random.choice(target2)
        elif target=="不一致":
            thisTarget=np.random.choice(target3)
        
        if distractor_type=="中心点":
            thisDistractor=np.random.choice(distractor_imgs)
            image_dis3.setImage(thisDistractor)
        elif distractor_type=="上下同时" or distractor_type=="上下分别":
            thisDistractors=np.random.choice(distractor_imgs,2)
            image_dis1.setImage(thisDistractors[0])
            image_dis2.setImage(thisDistractors[1])
        
        text.setText(thisTarget)
        # keep track of which components have finished
        trialComponents = [image_fix, image_dis1, image_dis2, image_dis3, text, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_fix* updates
            if image_fix.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                image_fix.frameNStart = frameN  # exact frame index
                image_fix.tStart = t  # local t and not account for scr refresh
                image_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_fix, 'tStartRefresh')  # time at next scr refresh
                image_fix.setAutoDraw(True)
            if image_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_fix.tStartRefresh + 2.1-frameTolerance:
                    # keep track of stop time/frame for later
                    image_fix.tStop = t  # not accounting for scr refresh
                    image_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_fix, 'tStopRefresh')  # time at next scr refresh
                    image_fix.setAutoDraw(False)
            
            # *image_dis1* updates
            if image_dis1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_dis1.frameNStart = frameN  # exact frame index
                image_dis1.tStart = t  # local t and not account for scr refresh
                image_dis1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_dis1, 'tStartRefresh')  # time at next scr refresh
                image_dis1.setAutoDraw(True)
            if image_dis1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_dis1.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    image_dis1.tStop = t  # not accounting for scr refresh
                    image_dis1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_dis1, 'tStopRefresh')  # time at next scr refresh
                    image_dis1.setAutoDraw(False)
            
            # *image_dis2* updates
            if image_dis2.status == NOT_STARTED and tThisFlip >= onset-frameTolerance:
                # keep track of start time/frame for later
                image_dis2.frameNStart = frameN  # exact frame index
                image_dis2.tStart = t  # local t and not account for scr refresh
                image_dis2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_dis2, 'tStartRefresh')  # time at next scr refresh
                image_dis2.setAutoDraw(True)
            if image_dis2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_dis2.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    image_dis2.tStop = t  # not accounting for scr refresh
                    image_dis2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_dis2, 'tStopRefresh')  # time at next scr refresh
                    image_dis2.setAutoDraw(False)
            
            # *image_dis3* updates
            if image_dis3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_dis3.frameNStart = frameN  # exact frame index
                image_dis3.tStart = t  # local t and not account for scr refresh
                image_dis3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_dis3, 'tStartRefresh')  # time at next scr refresh
                image_dis3.setAutoDraw(True)
            if image_dis3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_dis3.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    image_dis3.tStop = t  # not accounting for scr refresh
                    image_dis3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_dis3, 'tStopRefresh')  # time at next scr refresh
                    image_dis3.setAutoDraw(False)
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1.7-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 1.7-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        trials_2.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            trials_2.addData('key_resp_2.rt', key_resp_2.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_2'


    # ------Prepare to start Routine "ending"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    endingComponents = [text_end]
    for thisComponent in endingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    endingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "ending"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = endingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=endingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_end* updates
        if text_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_end.frameNStart = frameN  # exact frame index
            text_end.tStart = t  # local t and not account for scr refresh
            text_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
            text_end.setAutoDraw(True)
        if text_end.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_end.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                text_end.tStop = t  # not accounting for scr refresh
                text_end.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_end, 'tStopRefresh')  # time at next scr refresh
                text_end.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "ending"-------
    for thisComponent in endingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # Flip one final time so any remaining win.callOnFlip() 
    # and win.timeOnFlip() tasks get executed before quitting
    win.flip()

    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename+'.csv', delim='auto')
    thisExp.saveAsPickle(filename)
    logging.flush()
    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    win.close()
    core.quit()
