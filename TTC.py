#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on 三月 02, 2023, at 19:03
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

ins_img_path='./picResource/TTC/instruction.png'
class TTCResponse:
    # practice_record = []
    ex_record = []

    def __init__(self, ex):
        # self.practice_record = practice
        self.ex_record = ex

    # def getPracticeAccurate(self):
    #     return sum(self.practice_record) / len(self.practice_record)

    def getExAccurate(self):
        return sum(self.ex_record) / len(self.ex_record)

def TTC(admin, participant, group, session):
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

    returnValue = TTCResponse([])

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data/TTC/%s/%s/%s/%s' % (admin, participant, group, session)

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
                                     extraInfo=expInfo, runtimeInfo=None,
                                     savePickle=False, saveWideText=True,
                                     originPath='./',
                                     dataFileName=filename)
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    frameTolerance = 0.001  # how close to onset before 'same' frame

    # Start Code - component code to be run after the window creation

    # --- Setup the Window ---
    win = visual.Window(
        size=[1360, 768], fullscr=False, screen=0, 
        winType='pyglet', allowStencil=False,
        monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
        blendMode='avg', useFBO=True, 
        units='cm')
    win.mouseVisible = False
    # store frame rate of monitor if we can measure it
    expInfo['frameRate'] = win.getActualFrameRate()
    if expInfo['frameRate'] != None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    # --- Setup input devices ---

    ## Setup eyetracking
    ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard()

    # --- Initialize components for Routine "instruction" ---
    key_ins = keyboard.Keyboard()
    instructionClock = core.Clock()
    image = visual.ImageStim(
        win=win,
        name='image', 
        image=ins_img_path, mask=None,
        ori=0.0, pos=(0, 0), size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)

    trialClock = core.Clock()
    # --- Initialize components for Routine "trial" ---
    circle = visual.ShapeStim(
        win=win, name='circle',
        size=(1, 1), vertices='circle',
        ori=0.0, pos=(0, 0), 
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    arv_line = visual.Line(
        win=win, name='arv_line',
        start=(-(12, 0.5)[0]/2.0, 0), end=(+(12, 0.5)[0]/2.0, 0),
        ori=90.0, pos=(10, 0), 
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-1.0, interpolate=True)
    key_resp = keyboard.Keyboard()
    # Run 'Begin Experiment' code from code
    target_pos=10
    hori_pos=0
    orig_pos=0

    crossClock = core.Clock()
    # --- Initialize components for Routine "cross" ---
    polygon = visual.ShapeStim(
        win=win, name='polygon', vertices='cross',
        size=(1.5, 1.5),
        ori=0.0, pos=(0, 0), 
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "ending" ---
    endingClock = core.Clock()
    text_ending = visual.TextStim(win=win, name='text_ending',
        text='实验结束，感谢参与！',
        font='Open Sans',
        units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (possibly non-slip) routine 

    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True

    # update component parameters for each repeat
    key_ins.keys = []
    key_ins.rt = []
    _key_ins_allKeys = []
    # keep track of which components have finished
    instructionComponents = [key_ins, image]
    for thisComponent in instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionClock.reset(-_timeToFirstFrame)
    frameN = -1

    # --- Run Routine "instruction" ---
    while continueRoutine:
        # get current time
        t = instructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_ins* updates
        waitOnFlip = False
        if key_ins.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_ins.frameNStart = frameN  # exact frame index
            key_ins.tStart = t  # local t and not account for scr refresh
            key_ins.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_ins, 'tStartRefresh')  # time at next scr refresh
            key_ins.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_ins.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_ins.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_ins.status == STARTED and not waitOnFlip:
            theseKeys = key_ins.getKeys(keyList=['space'], waitRelease=False)
            _key_ins_allKeys.extend(theseKeys)
            if len(_key_ins_allKeys):
                key_ins.keys = _key_ins_allKeys[-1].name  # just the last key pressed
                key_ins.rt = _key_ins_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            
            image.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
           
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "instruction" ---
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=20.0, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tableResource/TTC.xlsx'),
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
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        gap_time = thisTrial['gap_time']
        speed = thisTrial['speed']
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # Run 'Begin Routine' code from code
        total_gap = gap_time + 0.8
        orig_pos = target_pos - total_gap * speed
        hori_pos = orig_pos
        circle.pos = (hori_pos,0)
        # keep track of which components have finished
        trialComponents = [circle, arv_line, key_resp]
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
        trialClock.reset(-_timeToFirstFrame) 
        frameN = -1
        
        # --- Run Routine "trial" ---
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *circle* updates
            if circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                circle.frameNStart = frameN  # exact frame index
                circle.tStart = t  # local t and not account for scr refresh
                circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle, 'tStartRefresh')  # time at next scr refresh
                circle.setAutoDraw(True)
            if circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    circle.tStop = t  # not accounting for scr refresh
                    circle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(circle, 'tStopRefresh')
                    circle.setAutoDraw(False)
                     
            # *arv_line* updates
            if arv_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arv_line.frameNStart = frameN  # exact frame index
                arv_line.tStart = t  # local t and not account for scr refresh
                arv_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arv_line, 'tStartRefresh')  # time at next scr refresh
                arv_line.setAutoDraw(True)
            
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
            # Run 'Each Frame' code from code
            hori_pos+=speed/60
            circle.pos=(hori_pos,0)
            
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
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
            returnValue.ex_record.append(key_resp.rt)
        # Run 'End Routine' code from code
        end_pos = orig_pos + speed * key_resp.rt
        err_pos = target_pos - end_pos
        trials.addData('end_pos', end_pos)
        trials.addData('err_distane', err_pos)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "cross" ---
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        crossComponents = [polygon]
        for thisComponent in crossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        crossClock.reset(-_timeToFirstFrame)
        frameN = -1
        
        # --- Run Routine "cross" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = crossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=crossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    win.timeOnFlip(polygon, 'tStopRefresh') 
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "cross" ---
        for thisComponent in crossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        trials.addData('polygon.started', polygon.tStartRefresh)
        trials.addData('polygon.stopped', polygon.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 20.0 repeats of 'trials'


    # --- Prepare to start Routine "ending" ---
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    endingComponents = [text_ending]
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
    endingClock.reset(-_timeToFirstFrame)
    frameN = -1

    # --- Run Routine "ending" ---
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = endingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=endingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_ending* updates
        if text_ending.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_ending.frameNStart = frameN  # exact frame index
            text_ending.tStart = t  # local t and not account for scr refresh
            text_ending.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_ending, 'tStartRefresh')  # time at next scr refresh
            text_ending.setAutoDraw(True)
        if text_ending.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_ending.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_ending.tStop = t  # not accounting for scr refresh
                text_ending.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_ending, 'tStopRefresh')
                text_ending.setAutoDraw(False)
        
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

    # --- Ending Routine "ending" ---
    for thisComponent in endingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
  

    # --- End experiment ---
    # Flip one final time so any remaining win.callOnFlip() 
    # and win.timeOnFlip() tasks get executed before quitting
    win.flip()

    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename+'.csv', delim='auto')
 
    # make sure everything is closed down
 
    thisExp.abort()  # or data files will save again on exit
    win.close()
    return returnValue

# admin = 'admin'
# participant = 'participant'
# group = 'group'
# session = 'session'
# res=TTC(admin, participant, group, session)
# print(res)