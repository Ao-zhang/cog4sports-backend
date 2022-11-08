#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 四月 07, 2022, at 18:29
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

class stroopResponse:
    practice_record=[]
    ex_record=[]

    def __init__(self,practice,ex):
        self.practice_record=practice
        self.ex_record=ex
    def getPracticeAccurate(self):
        return sum(self.practice_record)/len(self.practice_record)
    def getExAccurate(self):
        return sum(self.ex_record)/len(self.ex_record)
  


def stroop(admin,participant,group,session):
    # Ensure that relative paths start from the same directory as this script
    # _thisDir = os.path.dirname(os.path.abspath(__file__))
    # os.chdir(_thisDir)
    _thisDir="."
    
    # modify part 1
    # Store info about the experiment session
    expInfo = {}
    expInfo['admin']=admin
    expInfo['participant']=participant
    expInfo['session']=session
    expName="stroop"
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    print(expInfo['date'])
   
    returnValue=stroopResponse([],[])
    # modify part2
    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data/stroop/%s/%s/%s/%s' % (admin,participant,group,session)

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        savePickle=False, saveWideText=True,
        dataFileName=filename)
    # save a log file for detail verbose info

    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    frameTolerance = 0.001  # how close to onset before 'same' frame

    # Start Code - component code to be run after the window creation

    # Setup the Window
    win = visual.Window(
        size=(1024, 768), fullscr=False, screen=0, 
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

    # Initialize components for Routine "stroop_instruction"
    stroop_instructionClock = core.Clock()
    instruction = visual.TextStim(win=win, name='instruction',
        text='欢迎参加本次实验\n请注意屏幕中所出现的汉字，\n并请对屏幕上出现的四种颜色的汉字进行判断\n并忽略汉字的意义仅对字的颜色做出反应。\n如果字的颜色是——\n红色按“D”键，绿色按“F”键，\n蓝色按“J”键，黄色按“K”键。\n在实验开始前，将安排您进行练习实验熟悉实验操作\n请按空格键进入练习实验。\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    instruction_resp = keyboard.Keyboard()

    # Initialize components for Routine "stroop_fix"
    stroop_fixClock = core.Clock()
    cross = visual.TextStim(win=win, name='cross',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "stroop_blank1"
    stroop_blank1Clock = core.Clock()
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    from random import uniform

    t = uniform(0.5,0.8)

    clock.wait(t)


    # Initialize components for Routine "stroop_practice"
    stroop_practiceClock = core.Clock()
    practize = visual.TextStim(win=win, name='practize',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    feedback='0'

    # Initialize components for Routine "stroop_feedback"
    stroop_feedbackClock = core.Clock()
    text1 = visual.TextStim(win=win, name='text1',
        text='',
        font='Arial',
        pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "stroop_blank2"
    stroop_blank2Clock = core.Clock()
    black = visual.TextStim(win=win, name='black',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    from random import uniform

    t = uniform(1.0,1.5)

    clock.wait(t)


    # Initialize components for Routine "pra_fin"
    pra_finClock = core.Clock()
    text_2 = visual.TextStim(win=win, name='text_2',
        text='练习结束。\n按空格键进入正式实验。',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_3 = keyboard.Keyboard()

    # Initialize components for Routine "stroop_fix"
    stroop_fixClock = core.Clock()
    cross = visual.TextStim(win=win, name='cross',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "stroop_blank1"
    stroop_blank1Clock = core.Clock()
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    from random import uniform

    t = uniform(0.5,0.8)

    clock.wait(t)


    # Initialize components for Routine "stroop_trial"
    stroop_trialClock = core.Clock()
    prastim = visual.TextStim(win=win, name='prastim',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    resp = keyboard.Keyboard()

    # Initialize components for Routine "stroop_blank2"
    stroop_blank2Clock = core.Clock()
    black = visual.TextStim(win=win, name='black',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    from random import uniform

    t = uniform(1.0,1.5)

    clock.wait(t)


    # Initialize components for Routine "stroop_reset"
    stroop_resetClock = core.Clock()
    text_3 = visual.TextStim(win=win, name='text_3',
        text='休息30s',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "stroop_again"
    stroop_againClock = core.Clock()
    text_4 = visual.TextStim(win=win, name='text_4',
        text='按空格键开始',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard()

    # Initialize components for Routine "stroop_fix"
    stroop_fixClock = core.Clock()
    cross = visual.TextStim(win=win, name='cross',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "stroop_blank1"
    stroop_blank1Clock = core.Clock()
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    from random import uniform

    t = uniform(0.5,0.8)

    clock.wait(t)


    # Initialize components for Routine "stroop_trial"
    stroop_trialClock = core.Clock()
    prastim = visual.TextStim(win=win, name='prastim',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    resp = keyboard.Keyboard()

    # Initialize components for Routine "stroop_blank2"
    stroop_blank2Clock = core.Clock()
    black = visual.TextStim(win=win, name='black',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    from random import uniform

    t = uniform(1.0,1.5)

    clock.wait(t)



    # Initialize components for Routine "stroop_end"
    stroop_endClock = core.Clock()
    text_5 = visual.TextStim(win=win, name='text_5',
        text='实验结束，感谢您的参与！',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    # ------Prepare to start Routine "stroop_instruction"-------
    continueRoutine = True
    # update component parameters for each repeat
    instruction_resp.keys = []
    instruction_resp.rt = []
    _instruction_resp_allKeys = []
    # keep track of which components have finished
    stroop_instructionComponents = [instruction, instruction_resp]
    for thisComponent in stroop_instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stroop_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "stroop_instruction"-------
    while continueRoutine:
        # get current time
        t = stroop_instructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stroop_instructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction* updates
        if instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction.frameNStart = frameN  # exact frame index
            instruction.tStart = t  # local t and not account for scr refresh
            instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
            instruction.setAutoDraw(True)
        
        # *instruction_resp* updates
        waitOnFlip = False
        if instruction_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_resp.frameNStart = frameN  # exact frame index
            instruction_resp.tStart = t  # local t and not account for scr refresh
            instruction_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_resp, 'tStartRefresh')  # time at next scr refresh
            instruction_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instruction_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instruction_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instruction_resp.status == STARTED and not waitOnFlip:
            theseKeys = instruction_resp.getKeys(keyList=['space'], waitRelease=False)
            _instruction_resp_allKeys.extend(theseKeys)
            if len(_instruction_resp_allKeys):
                instruction_resp.keys = _instruction_resp_allKeys[-1].name  # just the last key pressed
                instruction_resp.rt = _instruction_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stroop_instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "stroop_instruction"-------
    for thisComponent in stroop_instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instruction.started', instruction.tStartRefresh)
    thisExp.addData('instruction.stopped', instruction.tStopRefresh)
    # check responses
    if instruction_resp.keys in ['', [], None]:  # No response was made
        instruction_resp.keys = None
    thisExp.addData('instruction_resp.keys',instruction_resp.keys)
    if instruction_resp.keys != None:  # we had a response
        thisExp.addData('instruction_resp.rt', instruction_resp.rt)
    thisExp.addData('instruction_resp.started', instruction_resp.tStartRefresh)
    thisExp.addData('instruction_resp.stopped', instruction_resp.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "stroop_instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    practice = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tableResource/stroop.xlsx'),
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
        
        # ------Prepare to start Routine "stroop_fix"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        stroop_fixComponents = [cross]
        colour=thisPractice['colour']
        answer=thisPractice['answer']
        word=thisPractice['word']
        for thisComponent in stroop_fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stroop_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stroop_fix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stroop_fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                cross.setAutoDraw(True)
            if cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                    cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_fix"-------
        for thisComponent in stroop_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice.addData('cross.started', cross.tStartRefresh)
        practice.addData('cross.stopped', cross.tStopRefresh)
        
        # ------Prepare to start Routine "stroop_blank1"-------
        continueRoutine = True
        routineTimer.add(0.800000)
        # update component parameters for each repeat
        # keep track of which components have finished
        stroop_blank1Components = [text]
        for thisComponent in stroop_blank1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stroop_blank1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stroop_blank1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_blank1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stroop_blank1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_blank1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_blank1"-------
        for thisComponent in stroop_blank1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice.addData('text.started', text.tStartRefresh)
        practice.addData('text.stopped', text.tStopRefresh)
        
        # ------Prepare to start Routine "stroop_practice"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        practize.setColor(colour, colorSpace='rgb')
        practize.setText(word)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        stroop_practiceComponents = [practize, key_resp]
        for thisComponent in stroop_practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stroop_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stroop_practice"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_practiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stroop_practiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practize* updates
            if practize.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practize.frameNStart = frameN  # exact frame index
                practize.tStart = t  # local t and not account for scr refresh
                practize.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practize, 'tStartRefresh')  # time at next scr refresh
                practize.setAutoDraw(True)
            if practize.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practize.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    practize.tStop = t  # not accounting for scr refresh
                    practize.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(practize, 'tStopRefresh')  # time at next scr refresh
                    practize.setAutoDraw(False)
            
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
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['d', 'f', 'j', 'k'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # was this correct?
                    if (key_resp.keys == str(answer)) or (key_resp.keys == answer):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_practice"-------
        for thisComponent in stroop_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice.addData('practize.started', practize.tStartRefresh)
        practice.addData('practize.stopped', practize.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(answer).lower() == 'none':
                key_resp.corr = 1;  # correct non-response
            else:
                key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for practice (TrialHandler)
        practice.addData('key_resp.keys',key_resp.keys)
        practice.addData('key_resp.corr', key_resp.corr)
        returnValue.practice_record.append(key_resp.corr)
        if key_resp.keys != None:  # we had a response
            practice.addData('key_resp.rt', key_resp.rt)
        practice.addData('key_resp.started', key_resp.tStartRefresh)
        practice.addData('key_resp.stopped', key_resp.tStopRefresh)
        if key_resp.keys==answer:
            feedback = "正确"
        else:
            feedback = "错误"
        
        # ------Prepare to start Routine "stroop_feedback"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        text1.setText(feedback)
        # keep track of which components have finished
        stroop_feedbackComponents = [text1]
        for thisComponent in stroop_feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stroop_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stroop_feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stroop_feedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text1* updates
            if text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text1.frameNStart = frameN  # exact frame index
                text1.tStart = t  # local t and not account for scr refresh
                text1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text1, 'tStartRefresh')  # time at next scr refresh
                text1.setAutoDraw(True)
            if text1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text1.tStop = t  # not accounting for scr refresh
                    text1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text1, 'tStopRefresh')  # time at next scr refresh
                    text1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_feedback"-------
        for thisComponent in stroop_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice.addData('text1.started', text1.tStartRefresh)
        practice.addData('text1.stopped', text1.tStopRefresh)
        
        # ------Prepare to start Routine "stroop_blank2"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        stroop_blank2Components = [black]
        for thisComponent in stroop_blank2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stroop_blank2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stroop_blank2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_blank2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stroop_blank2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *black* updates
            if black.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                black.frameNStart = frameN  # exact frame index
                black.tStart = t  # local t and not account for scr refresh
                black.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(black, 'tStartRefresh')  # time at next scr refresh
                black.setAutoDraw(True)
            if black.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > black.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    black.tStop = t  # not accounting for scr refresh
                    black.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(black, 'tStopRefresh')  # time at next scr refresh
                    black.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_blank2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_blank2"-------
        for thisComponent in stroop_blank2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice.addData('black.started', black.tStartRefresh)
        practice.addData('black.stopped', black.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'practice'

 
    # ------Prepare to start Routine "pra_fin"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    pra_finComponents = [text_2, key_resp_3]
    for thisComponent in pra_finComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pra_finClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "pra_fin"-------
    while continueRoutine:
        # get current time
        t = pra_finClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pra_finClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
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
        for thisComponent in pra_finComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "pra_fin"-------
    for thisComponent in pra_finComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text_2.started', text_2.tStartRefresh)
    thisExp.addData('text_2.stopped', text_2.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
    thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "pra_fin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    block1 = data.TrialHandler(nReps=5, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tableResource/stroop.xlsx'),
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
        
        # ------Prepare to start Routine "stroop_fix"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        stroop_fixComponents = [cross]
        colour=thisBlock1['colour']
        word=thisBlock1['word']
        answer=thisBlock1['answer']
        for thisComponent in stroop_fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stroop_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stroop_fix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stroop_fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                cross.setAutoDraw(True)
            if cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                    cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_fix"-------
        for thisComponent in stroop_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block1.addData('cross.started', cross.tStartRefresh)
        block1.addData('cross.stopped', cross.tStopRefresh)
        
        # ------Prepare to start Routine "stroop_blank1"-------
        continueRoutine = True
        routineTimer.add(0.800000)
        # update component parameters for each repeat
        # keep track of which components have finished
        stroop_blank1Components = [text]
        for thisComponent in stroop_blank1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stroop_blank1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stroop_blank1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_blank1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stroop_blank1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_blank1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_blank1"-------
        for thisComponent in stroop_blank1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block1.addData('text.started', text.tStartRefresh)
        block1.addData('text.stopped', text.tStopRefresh)
        
        # ------Prepare to start Routine "stroop_trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        prastim.setColor(colour, colorSpace='rgb')
        prastim.setText(word)
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        # keep track of which components have finished
        stroop_trialComponents = [prastim, resp]
        for thisComponent in stroop_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stroop_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stroop_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stroop_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prastim* updates
            if prastim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prastim.frameNStart = frameN  # exact frame index
                prastim.tStart = t  # local t and not account for scr refresh
                prastim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prastim, 'tStartRefresh')  # time at next scr refresh
                prastim.setAutoDraw(True)
            if prastim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prastim.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    prastim.tStop = t  # not accounting for scr refresh
                    prastim.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(prastim, 'tStopRefresh')  # time at next scr refresh
                    prastim.setAutoDraw(False)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                    resp.status = FINISHED
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['d', 'f', 'j', 'k'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                    resp.rt = _resp_allKeys[-1].rt
                    # was this correct?
                    if (resp.keys == str(answer)) or (resp.keys == answer):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_trial"-------
        for thisComponent in stroop_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block1.addData('prastim.started', prastim.tStartRefresh)
        block1.addData('prastim.stopped', prastim.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(answer).lower() == 'none':
                resp.corr = 1;  # correct non-response
            else:
                resp.corr = 0;  # failed to respond (incorrectly)
        # store data for block1 (TrialHandler)
        block1.addData('resp.keys',resp.keys)
        block1.addData('resp.corr', resp.corr)
        returnValue.ex_record.append(resp.corr)
        if resp.keys != None:  # we had a response
            block1.addData('resp.rt', resp.rt)
        block1.addData('resp.started', resp.tStartRefresh)
        block1.addData('resp.stopped', resp.tStopRefresh)
        
        # ------Prepare to start Routine "stroop_blank2"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        stroop_blank2Components = [black]
        for thisComponent in stroop_blank2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stroop_blank2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stroop_blank2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_blank2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stroop_blank2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *black* updates
            if black.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                black.frameNStart = frameN  # exact frame index
                black.tStart = t  # local t and not account for scr refresh
                black.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(black, 'tStartRefresh')  # time at next scr refresh
                black.setAutoDraw(True)
            if black.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > black.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    black.tStop = t  # not accounting for scr refresh
                    black.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(black, 'tStopRefresh')  # time at next scr refresh
                    black.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_blank2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_blank2"-------
        for thisComponent in stroop_blank2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block1.addData('black.started', black.tStartRefresh)
        block1.addData('black.stopped', black.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 5 repeats of 'block1'


    # ------Prepare to start Routine "stroop_reset"-------
    continueRoutine = True
    routineTimer.add(30.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    stroop_resetComponents = [text_3]
    for thisComponent in stroop_resetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stroop_resetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "stroop_reset"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stroop_resetClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stroop_resetClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stroop_resetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "stroop_reset"-------
    for thisComponent in stroop_resetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text_3.started', text_3.tStartRefresh)
    thisExp.addData('text_3.stopped', text_3.tStopRefresh)

    # ------Prepare to start Routine "stroop_again"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    stroop_againComponents = [text_4, key_resp_2]
    for thisComponent in stroop_againComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stroop_againClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "stroop_again"-------
    while continueRoutine:
        # get current time
        t = stroop_againClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stroop_againClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stroop_againComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "stroop_again"-------
    for thisComponent in stroop_againComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text_4.started', text_4.tStartRefresh)
    thisExp.addData('text_4.stopped', text_4.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
    thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "stroop_again" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    block2 = data.TrialHandler(nReps=5, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tableResource/stroop.xlsx'),
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
        
        # ------Prepare to start Routine "stroop_fix"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        stroop_fixComponents = [cross]
        colour=thisBlock2['colour']
        word=thisBlock2['word']
        answer=thisBlock2['answer']
        for thisComponent in stroop_fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stroop_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stroop_fix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stroop_fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                cross.setAutoDraw(True)
            if cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                    cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_fix"-------
        for thisComponent in stroop_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block2.addData('cross.started', cross.tStartRefresh)
        block2.addData('cross.stopped', cross.tStopRefresh)
        
        # ------Prepare to start Routine "stroop_blank1"-------
        continueRoutine = True
        routineTimer.add(0.800000)
        # update component parameters for each repeat
        # keep track of which components have finished
        stroop_blank1Components = [text]
        for thisComponent in stroop_blank1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stroop_blank1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stroop_blank1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_blank1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stroop_blank1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_blank1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_blank1"-------
        for thisComponent in stroop_blank1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block2.addData('text.started', text.tStartRefresh)
        block2.addData('text.stopped', text.tStopRefresh)
        
        # ------Prepare to start Routine "stroop_trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        prastim.setColor(colour, colorSpace='rgb')
        prastim.setText(word)
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        # keep track of which components have finished
        stroop_trialComponents = [prastim, resp]
        for thisComponent in stroop_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stroop_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stroop_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stroop_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prastim* updates
            if prastim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prastim.frameNStart = frameN  # exact frame index
                prastim.tStart = t  # local t and not account for scr refresh
                prastim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prastim, 'tStartRefresh')  # time at next scr refresh
                prastim.setAutoDraw(True)
            if prastim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prastim.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    prastim.tStop = t  # not accounting for scr refresh
                    prastim.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(prastim, 'tStopRefresh')  # time at next scr refresh
                    prastim.setAutoDraw(False)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                    resp.status = FINISHED
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['d', 'f', 'j', 'k'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                    resp.rt = _resp_allKeys[-1].rt
                    # was this correct?
                    if (resp.keys == str(answer)) or (resp.keys == answer):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_trial"-------
        for thisComponent in stroop_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block2.addData('prastim.started', prastim.tStartRefresh)
        block2.addData('prastim.stopped', prastim.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(answer).lower() == 'none':
                resp.corr = 1;  # correct non-response
            else:
                resp.corr = 0;  # failed to respond (incorrectly)
        # store data for block2 (TrialHandler)
        block2.addData('resp.keys',resp.keys)
        block2.addData('resp.corr', resp.corr)
        returnValue.ex_record.append(resp.corr)
        if resp.keys != None:  # we had a response
            block2.addData('resp.rt', resp.rt)
        block2.addData('resp.started', resp.tStartRefresh)
        block2.addData('resp.stopped', resp.tStopRefresh)
        
        # ------Prepare to start Routine "stroop_blank2"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        stroop_blank2Components = [black]
        for thisComponent in stroop_blank2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stroop_blank2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stroop_blank2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stroop_blank2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stroop_blank2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *black* updates
            if black.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                black.frameNStart = frameN  # exact frame index
                black.tStart = t  # local t and not account for scr refresh
                black.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(black, 'tStartRefresh')  # time at next scr refresh
                black.setAutoDraw(True)
            if black.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > black.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    black.tStop = t  # not accounting for scr refresh
                    black.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(black, 'tStopRefresh')  # time at next scr refresh
                    black.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stroop_blank2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stroop_blank2"-------
        for thisComponent in stroop_blank2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block2.addData('black.started', black.tStartRefresh)
        block2.addData('black.stopped', black.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 5 repeats of 'block2'


    # ------Prepare to start Routine "stroop_end"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    stroop_endComponents = [text_5]
    for thisComponent in stroop_endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stroop_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "stroop_end"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stroop_endClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stroop_endClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stroop_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "stroop_end"-------
    for thisComponent in stroop_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text_5.started', text_5.tStartRefresh)
    thisExp.addData('text_5.stopped', text_5.tStopRefresh)
    
    # Flip one final time so any remaining win.callOnFlip() 
    # and win.timeOnFlip() tasks get executed before quitting
    win.flip()

    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename+'.csv', delim='auto',appendFile=True,sortColumns=True)
    # thisExp.saveAsPickle(filename)

    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    win.close()
    return returnValue
    # print("stroop finished")
    
