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

class posnerResponse:
    practice_record = []
    ex_record = []

    def __init__(self, practice, ex):
        self.practice_record = practice
        self.ex_record = ex

    def getPracticeAccurate(self):
        return sum(self.practice_record) / len(self.practice_record)

    def getExAccurate(self):
        return sum(self.ex_record) / len(self.ex_record)


def posner(admin, participant, group, session):

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

    returnValue = posnerResponse([], [])

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data/posner/%s/%s/%s/%s' % (admin, participant, group, session)

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
        size=[1360, 768], fullscr=False, screen=0,
        winType='pyglet', allowGUI=False, allowStencil=False,
        monitor='testMonitor', color='black', colorSpace='rgb',
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
        image='picResource/posner/幻灯片1.png', mask=None,
        ori=0.0, pos=(0, 0), size=(1.8, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp = keyboard.Keyboard()

    # Initialize components for Routine "practice"
    practiceClock = core.Clock()
    text_cue = visual.TextStim(win=win, name='text_cue',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_line = visual.TextStim(win=win, name='text_line',
        text='|',
        font='Open Sans',
        pos=[0,0], height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_2 = keyboard.Keyboard()

    # Initialize components for Routine "feedback"
    feedbackClock = core.Clock()
    text_fb = visual.TextStim(win=win, name='text_fb',
        text='正确',
        font='Open Sans',
        pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "semi_intro"
    semi_introClock = core.Clock()
    image_semi = visual.ImageStim(
        win=win,
        name='image_semi', 
        image='sin', mask=None,
        ori=0.0, pos=(0, 0), size=(1.8, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_resp_3 = keyboard.Keyboard()

    # Initialize components for Routine "trial"
    trialClock = core.Clock()
    thisCue = visual.TextStim(win=win, name='thisCue',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    thisLine = visual.TextStim(win=win, name='thisLine',
        text='|',
        font='Open Sans',
        pos=[0,0], height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    this_resp = keyboard.Keyboard()

    # Initialize components for Routine "ending"
    endingClock = core.Clock()
    text_end = visual.TextStim(win=win, name='text_end',
        text='实验结束，感谢参与！',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
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
            return returnValue
        
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
    trials_prac = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tableResource/posner_materials.xlsx'),
        seed=None, name='trials_prac')
    thisExp.addLoop(trials_prac)  # add the loop to the experiment
    thisTrials_prac = trials_prac.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_prac.rgb)
    if thisTrials_prac != None:
        for paramName in thisTrials_prac:
            exec('{} = thisTrials_prac[paramName]'.format(paramName))

    for thisTrials_prac in trials_prac:
        currentLoop = trials_prac
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_prac.rgb)
        if thisTrials_prac != None:
            for paramName in thisTrials_prac:
                exec('{} = thisTrials_prac[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practice"-------
        continueRoutine = True
        routineTimer.add(4.700000)
        cue = thisTrials_prac['cue']
        loc = thisTrials_prac['loc']
        ans = thisTrials_prac['ans']
        # update component parameters for each repeat
        text_cue.setText(cue)
        text_line.setPos(loc)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        practiceComponents = [text_cue, text_line, key_resp_2]
        for thisComponent in practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practice"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_cue* updates
            if text_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_cue.frameNStart = frameN  # exact frame index
                text_cue.tStart = t  # local t and not account for scr refresh
                text_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_cue, 'tStartRefresh')  # time at next scr refresh
                text_cue.setAutoDraw(True)
            if text_cue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_cue.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_cue.tStop = t  # not accounting for scr refresh
                    text_cue.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_cue, 'tStopRefresh')  # time at next scr refresh
                    text_cue.setAutoDraw(False)
            
            # *text_line* updates
            if text_line.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                text_line.frameNStart = frameN  # exact frame index
                text_line.tStart = t  # local t and not account for scr refresh
                text_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_line, 'tStartRefresh')  # time at next scr refresh
                text_line.setAutoDraw(True)
            if text_line.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_line.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_line.tStop = t  # not accounting for scr refresh
                    text_line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_line, 'tStopRefresh')  # time at next scr refresh
                    text_line.setAutoDraw(False)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
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
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 3-frameTolerance:
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
                    # was this correct?
                    if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practice"-------
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
                key_resp_2.corr = 1;  # correct non-response
            else:
                key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_prac (TrialHandler)
        trials_prac.addData('key_resp_2.keys',key_resp_2.keys)
        trials_prac.addData('key_resp_2.corr', key_resp_2.corr)
        returnValue.practice_record.append(key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials_prac.addData('key_resp_2.rt', key_resp_2.rt)
        
        # ------Prepare to start Routine "feedback"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        if key_resp_2.corr == 1:
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
                return returnValue
            
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
        
    # completed 1.0 repeats of 'trials_prac'


    # set up handler to look after randomisation of conditions etc
    block = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tableResource/posner_blocks.xlsx'),
        seed=None, name='block')
    thisExp.addLoop(block)  # add the loop to the experiment
    thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))

    for thisBlock in block:
        currentLoop = block
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                exec('{} = thisBlock[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "semi_intro"-------
        continueRoutine = True
        semi = thisBlock['semi']
        # update component parameters for each repeat
        image_semi.setImage(semi)
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
                return returnValue
            
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
        trials = data.TrialHandler(nReps=5.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('tableResource/posner_materials.xlsx'),
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
            
            # ------Prepare to start Routine "trial"-------
            continueRoutine = True
            routineTimer.add(4.700000)

            cue = thisTrial['cue']
            loc = thisTrial['loc']
            ans = thisTrial['ans']
            # update component parameters for each repeat
            thisCue.setText(cue)
            thisLine.setPos(loc)
            this_resp.keys = []
            this_resp.rt = []
            _this_resp_allKeys = []
            # keep track of which components have finished
            trialComponents = [thisCue, thisLine, this_resp]
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
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=trialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *thisCue* updates
                if thisCue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    thisCue.frameNStart = frameN  # exact frame index
                    thisCue.tStart = t  # local t and not account for scr refresh
                    thisCue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(thisCue, 'tStartRefresh')  # time at next scr refresh
                    thisCue.setAutoDraw(True)
                if thisCue.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > thisCue.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        thisCue.tStop = t  # not accounting for scr refresh
                        thisCue.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(thisCue, 'tStopRefresh')  # time at next scr refresh
                        thisCue.setAutoDraw(False)
                
                # *thisLine* updates
                if thisLine.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                    # keep track of start time/frame for later
                    thisLine.frameNStart = frameN  # exact frame index
                    thisLine.tStart = t  # local t and not account for scr refresh
                    thisLine.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(thisLine, 'tStartRefresh')  # time at next scr refresh
                    thisLine.setAutoDraw(True)
                if thisLine.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > thisLine.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        thisLine.tStop = t  # not accounting for scr refresh
                        thisLine.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(thisLine, 'tStopRefresh')  # time at next scr refresh
                        thisLine.setAutoDraw(False)
                
                # *this_resp* updates
                waitOnFlip = False
                if this_resp.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                    # keep track of start time/frame for later
                    this_resp.frameNStart = frameN  # exact frame index
                    this_resp.tStart = t  # local t and not account for scr refresh
                    this_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(this_resp, 'tStartRefresh')  # time at next scr refresh
                    this_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(this_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(this_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if this_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > this_resp.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        this_resp.tStop = t  # not accounting for scr refresh
                        this_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(this_resp, 'tStopRefresh')  # time at next scr refresh
                        this_resp.status = FINISHED
                if this_resp.status == STARTED and not waitOnFlip:
                    theseKeys = this_resp.getKeys(keyList=['right', 'space'], waitRelease=False)
                    _this_resp_allKeys.extend(theseKeys)
                    if len(_this_resp_allKeys):
                        this_resp.keys = _this_resp_allKeys[-1].name  # just the last key pressed
                        this_resp.rt = _this_resp_allKeys[-1].rt
                        # was this correct?
                        if (this_resp.keys == str(ans)) or (this_resp.keys == ans):
                            this_resp.corr = 1
                        else:
                            this_resp.corr = 0
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    return returnValue
                
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
            if this_resp.keys in ['', [], None]:  # No response was made
                this_resp.keys = None
                # was no response the correct answer?!
                if str(ans).lower() == 'none':
                    this_resp.corr = 1;  # correct non-response
                else:
                    this_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for trials (TrialHandler)
            trials.addData('this_resp.keys',this_resp.keys)
            trials.addData('this_resp.corr', this_resp.corr)
            returnValue.ex_record.append(key_resp_2.corr)
            if this_resp.keys != None:  # we had a response
                trials.addData('this_resp.rt', this_resp.rt)
            thisExp.nextEntry()
            
        # completed 5.0 repeats of 'trials'
        
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'block'


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
            return returnValue
        
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

    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    win.close()
    return returnValue
