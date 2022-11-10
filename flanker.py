#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


class flankerResponse:
    practice_record = []
    ex_record = []

    def __init__(self, practice, ex):
        self.practice_record = practice
        self.ex_record = ex

    def getPracticeAccurate(self):
        return sum(self.practice_record) / len(self.practice_record)

    def getExAccurate(self):
        return sum(self.ex_record) / len(self.ex_record)


def flanker(admin, participant, group, session):
    # Ensure that relative paths start from the same directory as this script
    # _thisDir = os.path.dirname(os.path.abspath(__file__))
    # os.chdir(_thisDir)
    _thisDir="."

    # Store info about the experiment session
    expInfo = {}
    expInfo['admin'] = admin
    expInfo['participant'] = participant
    expInfo['session'] = session
    expName = "flanker"
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    print(expInfo['date'])

    returnValue = flankerResponse([], [])

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data/flanker/%s/%s/%s/%s' % (admin, participant, group, session)

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
        size=[1920, 1080], fullscr=False, screen=0, 
        winType='pyglet', allowGUI=False, allowStencil=False,
        monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
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
    flanker_instruction = visual.TextStim(win=win, name='flanker_instruction',
                                          text='欢迎参加本次实验。\n\n请注意屏幕中所呈现的字母串（共包含5个字母）\n\n判断中间字母（即第3个字母）\n\n如果字母为F，则按F键，如果字母为L，则按L键\n\n在实验开始前将安排您进行练习熟悉实验操作\n\n请按空格键进入练习实验。',
                                          font='Open Sans',
                                          pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                          color='white', colorSpace='rgb', opacity=None,
                                          languageStyle='LTR',
                                          depth=0.0);
    flanker_instruction_resp = keyboard.Keyboard()

    # Initialize components for Routine "fix"
    fixClock = core.Clock()
    flanker_fix = visual.TextStim(win=win, name='flanker_fix',
                                  text='+',
                                  font='Open Sans',
                                  pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
                                  color='white', colorSpace='rgb', opacity=None,
                                  languageStyle='LTR',
                                  depth=0.0);

    # Initialize components for Routine "trial"
    trialClock = core.Clock()
    flanker_stimuli = visual.TextStim(win=win, name='flanker_stimuli',
                                      text='',
                                      font='Open Sans',
                                      pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0,
                                      color='white', colorSpace='rgb', opacity=None,
                                      languageStyle='LTR',
                                      depth=0.0);
    flanker_practice_resp = keyboard.Keyboard()

    # Initialize components for Routine "feedback"
    feedbackClock = core.Clock()
    fb = visual.TextStim(win=win, name='fb',
                         text=None,
                         font='Open Sans',
                         pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
                         color='white', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=0.0);

    # Initialize components for Routine "ex_introduction"
    ex_introductionClock = core.Clock()
    flanker_ex_introduction = visual.TextStim(win=win, name='flanker_ex_introduction',
                                              text='练习结束。\n按空格键进入正式实验。',
                                              font='Open Sans',
                                              pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                              color='white', colorSpace='rgb', opacity=None,
                                              languageStyle='LTR',
                                              depth=0.0);
    flanker_start_resp = keyboard.Keyboard()

    # Initialize components for Routine "fix"
    fixClock = core.Clock()
    flanker_fix = visual.TextStim(win=win, name='flanker_fix',
                                  text='+',
                                  font='Open Sans',
                                  pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
                                  color='white', colorSpace='rgb', opacity=None,
                                  languageStyle='LTR',
                                  depth=0.0);

    # Initialize components for Routine "trial"
    trialClock = core.Clock()
    flanker_stimuli = visual.TextStim(win=win, name='flanker_stimuli',
                                      text='',
                                      font='Open Sans',
                                      pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0,
                                      color='white', colorSpace='rgb', opacity=None,
                                      languageStyle='LTR',
                                      depth=0.0);
    flanker_practice_resp = keyboard.Keyboard()

    # Initialize components for Routine "interval"
    intervalClock = core.Clock()
    flanker_interval = visual.TextStim(win=win, name='flanker_interval',
                                       text=None,
                                       font='Open Sans',
                                       pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
                                       color='white', colorSpace='rgb', opacity=None,
                                       languageStyle='LTR',
                                       depth=0.0);

    # Initialize components for Routine "rest"
    restClock = core.Clock()
    flanker_rest = visual.TextStim(win=win, name='flanker_rest',
                                   text='休息30s',
                                   font='Open Sans',
                                   pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                   color='white', colorSpace='rgb', opacity=None,
                                   languageStyle='LTR',
                                   depth=0.0);

    # Initialize components for Routine "start"
    startClock = core.Clock()
    flanker_start_text = visual.TextStim(win=win, name='flanker_start_text',
                                         text='按空格键开始',
                                         font='Open Sans',
                                         pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                         color='white', colorSpace='rgb', opacity=None,
                                         languageStyle='LTR',
                                         depth=0.0);
    flanker_again_resp = keyboard.Keyboard()

    # Initialize components for Routine "fix"
    fixClock = core.Clock()
    flanker_fix = visual.TextStim(win=win, name='flanker_fix',
                                  text='+',
                                  font='Open Sans',
                                  pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
                                  color='white', colorSpace='rgb', opacity=None,
                                  languageStyle='LTR',
                                  depth=0.0);

    # Initialize components for Routine "trial"
    trialClock = core.Clock()
    flanker_stimuli = visual.TextStim(win=win, name='flanker_stimuli',
                                      text='',
                                      font='Open Sans',
                                      pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0,
                                      color='white', colorSpace='rgb', opacity=None,
                                      languageStyle='LTR',
                                      depth=0.0);
    flanker_practice_resp = keyboard.Keyboard()

    # Initialize components for Routine "interval"
    intervalClock = core.Clock()
    flanker_interval = visual.TextStim(win=win, name='flanker_interval',
                                       text=None,
                                       font='Open Sans',
                                       pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
                                       color='white', colorSpace='rgb', opacity=None,
                                       languageStyle='LTR',
                                       depth=0.0);

    # Initialize components for Routine "end"
    endClock = core.Clock()
    flanker_end = visual.TextStim(win=win, name='flanker_end',
                                  text='实验结束，感谢您的参与！',
                                  font='Open Sans',
                                  pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                  color='white', colorSpace='rgb', opacity=None,
                                  languageStyle='LTR',
                                  depth=0.0);

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    # ------Prepare to start Routine "introduction"-------
    continueRoutine = True
    # update component parameters for each repeat
    flanker_instruction_resp.keys = []
    flanker_instruction_resp.rt = []
    _flanker_instruction_resp_allKeys = []
    # keep track of which components have finished
    introductionComponents = [flanker_instruction, flanker_instruction_resp]
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

        # *flanker_instruction* updates
        if flanker_instruction.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            flanker_instruction.frameNStart = frameN  # exact frame index
            flanker_instruction.tStart = t  # local t and not account for scr refresh
            flanker_instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flanker_instruction, 'tStartRefresh')  # time at next scr refresh
            flanker_instruction.setAutoDraw(True)

        # *flanker_instruction_resp* updates
        waitOnFlip = False
        if flanker_instruction_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            flanker_instruction_resp.frameNStart = frameN  # exact frame index
            flanker_instruction_resp.tStart = t  # local t and not account for scr refresh
            flanker_instruction_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flanker_instruction_resp, 'tStartRefresh')  # time at next scr refresh
            flanker_instruction_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(flanker_instruction_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(flanker_instruction_resp.clearEvents,
                           eventType='keyboard')  # clear events on next screen flip
        if flanker_instruction_resp.status == STARTED and not waitOnFlip:
            theseKeys = flanker_instruction_resp.getKeys(keyList=['space'], waitRelease=False)
            _flanker_instruction_resp_allKeys.extend(theseKeys)
            if len(_flanker_instruction_resp_allKeys):
                flanker_instruction_resp.keys = _flanker_instruction_resp_allKeys[-1].name  # just the last key pressed
                flanker_instruction_resp.rt = _flanker_instruction_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue

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
    thisExp.addData('flanker_instruction.started', flanker_instruction.tStartRefresh)
    thisExp.addData('flanker_instruction.stopped', flanker_instruction.tStopRefresh)
    # check responses
    if flanker_instruction_resp.keys in ['', [], None]:  # No response was made
        flanker_instruction_resp.keys = None
    thisExp.addData('flanker_instruction_resp.keys', flanker_instruction_resp.keys)
    if flanker_instruction_resp.keys != None:  # we had a response
        thisExp.addData('flanker_instruction_resp.rt', flanker_instruction_resp.rt)
    thisExp.addData('flanker_instruction_resp.started', flanker_instruction_resp.tStartRefresh)
    thisExp.addData('flanker_instruction_resp.stopped', flanker_instruction_resp.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    practice = data.TrialHandler(nReps=3.0, method='random',
                                 extraInfo=expInfo, originPath=-1,
                                 trialList=data.importConditions('tableResource/flanker.xlsx'),
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
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixComponents = [flanker_fix]
        name = thisPractice['name']
        canswer = thisPractice['canswer']
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

            # *flanker_fix* updates
            if flanker_fix.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                flanker_fix.frameNStart = frameN  # exact frame index
                flanker_fix.tStart = t  # local t and not account for scr refresh
                flanker_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_fix, 'tStartRefresh')  # time at next scr refresh
                flanker_fix.setAutoDraw(True)
            if flanker_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > flanker_fix.tStartRefresh + 0.5 - frameTolerance:
                    # keep track of stop time/frame for later
                    flanker_fix.tStop = t  # not accounting for scr refresh
                    flanker_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(flanker_fix, 'tStopRefresh')  # time at next scr refresh
                    flanker_fix.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue

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
        practice.addData('flanker_fix.started', flanker_fix.tStartRefresh)
        practice.addData('flanker_fix.stopped', flanker_fix.tStopRefresh)

        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        flanker_stimuli.setText(name)
        flanker_practice_resp.keys = []
        flanker_practice_resp.rt = []
        _flanker_practice_resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [flanker_stimuli, flanker_practice_resp]
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

            # *flanker_stimuli* updates
            if flanker_stimuli.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                flanker_stimuli.frameNStart = frameN  # exact frame index
                flanker_stimuli.tStart = t  # local t and not account for scr refresh
                flanker_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_stimuli, 'tStartRefresh')  # time at next scr refresh
                flanker_stimuli.setAutoDraw(True)
            if flanker_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > flanker_stimuli.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    flanker_stimuli.tStop = t  # not accounting for scr refresh
                    flanker_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(flanker_stimuli, 'tStopRefresh')  # time at next scr refresh
                    flanker_stimuli.setAutoDraw(False)

            # *flanker_practice_resp* updates
            waitOnFlip = False
            if flanker_practice_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                flanker_practice_resp.frameNStart = frameN  # exact frame index
                flanker_practice_resp.tStart = t  # local t and not account for scr refresh
                flanker_practice_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_practice_resp, 'tStartRefresh')  # time at next scr refresh
                flanker_practice_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(flanker_practice_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(flanker_practice_resp.clearEvents,
                               eventType='keyboard')  # clear events on next screen flip
            if flanker_practice_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > flanker_practice_resp.tStartRefresh + 1 - frameTolerance:
                    # keep track of stop time/frame for later
                    flanker_practice_resp.tStop = t  # not accounting for scr refresh
                    flanker_practice_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(flanker_practice_resp, 'tStopRefresh')  # time at next scr refresh
                    flanker_practice_resp.status = FINISHED
            if flanker_practice_resp.status == STARTED and not waitOnFlip:
                theseKeys = flanker_practice_resp.getKeys(keyList=['l', 'f'], waitRelease=False)
                _flanker_practice_resp_allKeys.extend(theseKeys)
                if len(_flanker_practice_resp_allKeys):
                    flanker_practice_resp.keys = _flanker_practice_resp_allKeys[-1].name  # just the last key pressed
                    flanker_practice_resp.rt = _flanker_practice_resp_allKeys[-1].rt
                    # was this correct?
                    if (flanker_practice_resp.keys == str(canswer)) or (flanker_practice_resp.keys == canswer):
                        flanker_practice_resp.corr = 1
                    else:
                        flanker_practice_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False

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
        practice.addData('flanker_stimuli.started', flanker_stimuli.tStartRefresh)
        practice.addData('flanker_stimuli.stopped', flanker_stimuli.tStopRefresh)
        # check responses
        if flanker_practice_resp.keys in ['', [], None]:  # No response was made
            flanker_practice_resp.keys = None
            # was no response the correct answer?!
            if str(canswer).lower() == 'none':
                flanker_practice_resp.corr = 1;  # correct non-response
            else:
                flanker_practice_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for practice (TrialHandler)
        practice.addData('flanker_practice_resp.keys', flanker_practice_resp.keys)
        practice.addData('flanker_practice_resp.corr', flanker_practice_resp.corr)
        returnValue.practice_record.append(flanker_practice_resp.corr)
        if flanker_practice_resp.keys != None:  # we had a response
            practice.addData('flanker_practice_resp.rt', flanker_practice_resp.rt)
        practice.addData('flanker_practice_resp.started', flanker_practice_resp.tStartRefresh)
        practice.addData('flanker_practice_resp.stopped', flanker_practice_resp.tStopRefresh)

        # ------Prepare to start Routine "feedback"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        if flanker_practice_resp.corr == 1:
            fb.setText('正确')
        else:
            fb.setText('错误')
        # keep track of which components have finished
        feedbackComponents = [fb]
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

            # *fb* updates
            if fb.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                fb.frameNStart = frameN  # exact frame index
                fb.tStart = t  # local t and not account for scr refresh
                fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fb, 'tStartRefresh')  # time at next scr refresh
                fb.setAutoDraw(True)
            if fb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fb.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    fb.tStop = t  # not accounting for scr refresh
                    fb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fb, 'tStopRefresh')  # time at next scr refresh
                    fb.setAutoDraw(False)

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
        practice.addData('fb.started', fb.tStartRefresh)
        practice.addData('fb.stopped', fb.tStopRefresh)
        thisExp.nextEntry()

    # completed 3.0 repeats of 'practice'

    # ------Prepare to start Routine "ex_introduction"-------
    continueRoutine = True
    # update component parameters for each repeat
    flanker_start_resp.keys = []
    flanker_start_resp.rt = []
    _flanker_start_resp_allKeys = []
    # keep track of which components have finished
    ex_introductionComponents = [flanker_ex_introduction, flanker_start_resp]
    for thisComponent in ex_introductionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ex_introductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "ex_introduction"-------
    while continueRoutine:
        # get current time
        t = ex_introductionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ex_introductionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *flanker_ex_introduction* updates
        if flanker_ex_introduction.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            flanker_ex_introduction.frameNStart = frameN  # exact frame index
            flanker_ex_introduction.tStart = t  # local t and not account for scr refresh
            flanker_ex_introduction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flanker_ex_introduction, 'tStartRefresh')  # time at next scr refresh
            flanker_ex_introduction.setAutoDraw(True)

        # *flanker_start_resp* updates
        waitOnFlip = False
        if flanker_start_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            flanker_start_resp.frameNStart = frameN  # exact frame index
            flanker_start_resp.tStart = t  # local t and not account for scr refresh
            flanker_start_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flanker_start_resp, 'tStartRefresh')  # time at next scr refresh
            flanker_start_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(flanker_start_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(flanker_start_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if flanker_start_resp.status == STARTED and not waitOnFlip:
            theseKeys = flanker_start_resp.getKeys(keyList=['space'], waitRelease=False)
            _flanker_start_resp_allKeys.extend(theseKeys)
            if len(_flanker_start_resp_allKeys):
                flanker_start_resp.keys = _flanker_start_resp_allKeys[-1].name  # just the last key pressed
                flanker_start_resp.rt = _flanker_start_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ex_introductionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "ex_introduction"-------
    for thisComponent in ex_introductionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('flanker_ex_introduction.started', flanker_ex_introduction.tStartRefresh)
    thisExp.addData('flanker_ex_introduction.stopped', flanker_ex_introduction.tStopRefresh)
    # check responses
    if flanker_start_resp.keys in ['', [], None]:  # No response was made
        flanker_start_resp.keys = None
    thisExp.addData('flanker_start_resp.keys', flanker_start_resp.keys)
    if flanker_start_resp.keys != None:  # we had a response
        thisExp.addData('flanker_start_resp.rt', flanker_start_resp.rt)
    thisExp.addData('flanker_start_resp.started', flanker_start_resp.tStartRefresh)
    thisExp.addData('flanker_start_resp.stopped', flanker_start_resp.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "ex_introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    flanker_ex1 = data.TrialHandler(nReps=12.0, method='random',
                                    extraInfo=expInfo, originPath=-1,
                                    trialList=data.importConditions('tableResource/flanker.xlsx'),
                                    seed=None, name='flanker_ex1')
    thisExp.addLoop(flanker_ex1)  # add the loop to the experiment
    thisFlanker_ex1 = flanker_ex1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFlanker_ex1.rgb)
    if thisFlanker_ex1 != None:
        for paramName in thisFlanker_ex1:
            exec('{} = thisFlanker_ex1[paramName]'.format(paramName))

    for thisFlanker_ex1 in flanker_ex1:
        currentLoop = flanker_ex1
        # abbreviate parameter names if possible (e.g. rgb = thisFlanker_ex1.rgb)
        if thisFlanker_ex1 != None:
            for paramName in thisFlanker_ex1:
                exec('{} = thisFlanker_ex1[paramName]'.format(paramName))

        # ------Prepare to start Routine "fix"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixComponents = [flanker_fix]
        name = thisFlanker_ex1['name']
        canswer = thisFlanker_ex1['canswer']
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

            # *flanker_fix* updates
            if flanker_fix.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                flanker_fix.frameNStart = frameN  # exact frame index
                flanker_fix.tStart = t  # local t and not account for scr refresh
                flanker_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_fix, 'tStartRefresh')  # time at next scr refresh
                flanker_fix.setAutoDraw(True)
            if flanker_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > flanker_fix.tStartRefresh + 0.5 - frameTolerance:
                    # keep track of stop time/frame for later
                    flanker_fix.tStop = t  # not accounting for scr refresh
                    flanker_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(flanker_fix, 'tStopRefresh')  # time at next scr refresh
                    flanker_fix.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue

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
        flanker_ex1.addData('flanker_fix.started', flanker_fix.tStartRefresh)
        flanker_ex1.addData('flanker_fix.stopped', flanker_fix.tStopRefresh)

        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        flanker_stimuli.setText(name)
        flanker_practice_resp.keys = []
        flanker_practice_resp.rt = []
        _flanker_practice_resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [flanker_stimuli, flanker_practice_resp]
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

            # *flanker_stimuli* updates
            if flanker_stimuli.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                flanker_stimuli.frameNStart = frameN  # exact frame index
                flanker_stimuli.tStart = t  # local t and not account for scr refresh
                flanker_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_stimuli, 'tStartRefresh')  # time at next scr refresh
                flanker_stimuli.setAutoDraw(True)
            if flanker_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > flanker_stimuli.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    flanker_stimuli.tStop = t  # not accounting for scr refresh
                    flanker_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(flanker_stimuli, 'tStopRefresh')  # time at next scr refresh
                    flanker_stimuli.setAutoDraw(False)

            # *flanker_practice_resp* updates
            waitOnFlip = False
            if flanker_practice_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                flanker_practice_resp.frameNStart = frameN  # exact frame index
                flanker_practice_resp.tStart = t  # local t and not account for scr refresh
                flanker_practice_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_practice_resp, 'tStartRefresh')  # time at next scr refresh
                flanker_practice_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(flanker_practice_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(flanker_practice_resp.clearEvents,
                               eventType='keyboard')  # clear events on next screen flip
            if flanker_practice_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > flanker_practice_resp.tStartRefresh + 1 - frameTolerance:
                    # keep track of stop time/frame for later
                    flanker_practice_resp.tStop = t  # not accounting for scr refresh
                    flanker_practice_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(flanker_practice_resp, 'tStopRefresh')  # time at next scr refresh
                    flanker_practice_resp.status = FINISHED
            if flanker_practice_resp.status == STARTED and not waitOnFlip:
                theseKeys = flanker_practice_resp.getKeys(keyList=['l', 'f'], waitRelease=False)
                _flanker_practice_resp_allKeys.extend(theseKeys)
                if len(_flanker_practice_resp_allKeys):
                    flanker_practice_resp.keys = _flanker_practice_resp_allKeys[-1].name  # just the last key pressed
                    flanker_practice_resp.rt = _flanker_practice_resp_allKeys[-1].rt
                    # was this correct?
                    if (flanker_practice_resp.keys == str(canswer)) or (flanker_practice_resp.keys == canswer):
                        flanker_practice_resp.corr = 1
                    else:
                        flanker_practice_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False

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
        flanker_ex1.addData('flanker_stimuli.started', flanker_stimuli.tStartRefresh)
        flanker_ex1.addData('flanker_stimuli.stopped', flanker_stimuli.tStopRefresh)
        # check responses
        if flanker_practice_resp.keys in ['', [], None]:  # No response was made
            flanker_practice_resp.keys = None
            # was no response the correct answer?!
            if str(canswer).lower() == 'none':
                flanker_practice_resp.corr = 1;  # correct non-response
            else:
                flanker_practice_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for flanker_ex1 (TrialHandler)
        flanker_ex1.addData('flanker_practice_resp.keys', flanker_practice_resp.keys)
        flanker_ex1.addData('flanker_practice_resp.corr', flanker_practice_resp.corr)
        returnValue.ex_record.append(flanker_practice_resp.corr)
        if flanker_practice_resp.keys != None:  # we had a response
            flanker_ex1.addData('flanker_practice_resp.rt', flanker_practice_resp.rt)
        flanker_ex1.addData('flanker_practice_resp.started', flanker_practice_resp.tStartRefresh)
        flanker_ex1.addData('flanker_practice_resp.stopped', flanker_practice_resp.tStopRefresh)

        # ------Prepare to start Routine "interval"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        intervalComponents = [flanker_interval]
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

            # *flanker_interval* updates
            if flanker_interval.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                flanker_interval.frameNStart = frameN  # exact frame index
                flanker_interval.tStart = t  # local t and not account for scr refresh
                flanker_interval.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_interval, 'tStartRefresh')  # time at next scr refresh
                flanker_interval.setAutoDraw(True)
            if flanker_interval.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > flanker_interval.tStartRefresh + 2 - frameTolerance:
                    # keep track of stop time/frame for later
                    flanker_interval.tStop = t  # not accounting for scr refresh
                    flanker_interval.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(flanker_interval, 'tStopRefresh')  # time at next scr refresh
                    flanker_interval.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue

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
        flanker_ex1.addData('flanker_interval.started', flanker_interval.tStartRefresh)
        flanker_ex1.addData('flanker_interval.stopped', flanker_interval.tStopRefresh)
        thisExp.nextEntry()

    # completed 12.0 repeats of 'flanker_ex1'

    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    routineTimer.add(30.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    restComponents = [flanker_rest]
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

        # *flanker_rest* updates
        if flanker_rest.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            flanker_rest.frameNStart = frameN  # exact frame index
            flanker_rest.tStart = t  # local t and not account for scr refresh
            flanker_rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flanker_rest, 'tStartRefresh')  # time at next scr refresh
            flanker_rest.setAutoDraw(True)
        if flanker_rest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > flanker_rest.tStartRefresh + 30 - frameTolerance:
                # keep track of stop time/frame for later
                flanker_rest.tStop = t  # not accounting for scr refresh
                flanker_rest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(flanker_rest, 'tStopRefresh')  # time at next scr refresh
                flanker_rest.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue

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
    thisExp.addData('flanker_rest.started', flanker_rest.tStartRefresh)
    thisExp.addData('flanker_rest.stopped', flanker_rest.tStopRefresh)

    # ------Prepare to start Routine "start"-------
    continueRoutine = True
    # update component parameters for each repeat
    flanker_again_resp.keys = []
    flanker_again_resp.rt = []
    _flanker_again_resp_allKeys = []
    # keep track of which components have finished
    startComponents = [flanker_start_text, flanker_again_resp]
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

        # *flanker_start_text* updates
        if flanker_start_text.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            flanker_start_text.frameNStart = frameN  # exact frame index
            flanker_start_text.tStart = t  # local t and not account for scr refresh
            flanker_start_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flanker_start_text, 'tStartRefresh')  # time at next scr refresh
            flanker_start_text.setAutoDraw(True)

        # *flanker_again_resp* updates
        waitOnFlip = False
        if flanker_again_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            flanker_again_resp.frameNStart = frameN  # exact frame index
            flanker_again_resp.tStart = t  # local t and not account for scr refresh
            flanker_again_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flanker_again_resp, 'tStartRefresh')  # time at next scr refresh
            flanker_again_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(flanker_again_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(flanker_again_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if flanker_again_resp.status == STARTED and not waitOnFlip:
            theseKeys = flanker_again_resp.getKeys(keyList=['space'], waitRelease=False)
            _flanker_again_resp_allKeys.extend(theseKeys)
            if len(_flanker_again_resp_allKeys):
                flanker_again_resp.keys = _flanker_again_resp_allKeys[-1].name  # just the last key pressed
                flanker_again_resp.rt = _flanker_again_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue

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
    thisExp.addData('flanker_start_text.started', flanker_start_text.tStartRefresh)
    thisExp.addData('flanker_start_text.stopped', flanker_start_text.tStopRefresh)
    # check responses
    if flanker_again_resp.keys in ['', [], None]:  # No response was made
        flanker_again_resp.keys = None
    thisExp.addData('flanker_again_resp.keys', flanker_again_resp.keys)
    if flanker_again_resp.keys != None:  # we had a response
        thisExp.addData('flanker_again_resp.rt', flanker_again_resp.rt)
    thisExp.addData('flanker_again_resp.started', flanker_again_resp.tStartRefresh)
    thisExp.addData('flanker_again_resp.stopped', flanker_again_resp.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    flanker_ex2 = data.TrialHandler(nReps=12.0, method='random',
                                    extraInfo=expInfo, originPath=-1,
                                    trialList=data.importConditions('tableResource/flanker.xlsx'),
                                    seed=None, name='flanker_ex2')
    thisExp.addLoop(flanker_ex2)  # add the loop to the experiment
    thisFlanker_ex2 = flanker_ex2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFlanker_ex2.rgb)
    if thisFlanker_ex2 != None:
        for paramName in thisFlanker_ex2:
            exec('{} = thisFlanker_ex2[paramName]'.format(paramName))

    for thisFlanker_ex2 in flanker_ex2:
        currentLoop = flanker_ex2
        # abbreviate parameter names if possible (e.g. rgb = thisFlanker_ex2.rgb)
        if thisFlanker_ex2 != None:
            for paramName in thisFlanker_ex2:
                exec('{} = thisFlanker_ex2[paramName]'.format(paramName))

        # ------Prepare to start Routine "fix"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixComponents = [flanker_fix]
        name = thisFlanker_ex2['name']
        canswer = thisFlanker_ex2['canswer']
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

            # *flanker_fix* updates
            if flanker_fix.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                flanker_fix.frameNStart = frameN  # exact frame index
                flanker_fix.tStart = t  # local t and not account for scr refresh
                flanker_fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_fix, 'tStartRefresh')  # time at next scr refresh
                flanker_fix.setAutoDraw(True)
            if flanker_fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > flanker_fix.tStartRefresh + 0.5 - frameTolerance:
                    # keep track of stop time/frame for later
                    flanker_fix.tStop = t  # not accounting for scr refresh
                    flanker_fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(flanker_fix, 'tStopRefresh')  # time at next scr refresh
                    flanker_fix.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue

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
        flanker_ex2.addData('flanker_fix.started', flanker_fix.tStartRefresh)
        flanker_ex2.addData('flanker_fix.stopped', flanker_fix.tStopRefresh)

        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        flanker_stimuli.setText(name)
        flanker_practice_resp.keys = []
        flanker_practice_resp.rt = []
        _flanker_practice_resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [flanker_stimuli, flanker_practice_resp]
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

            # *flanker_stimuli* updates
            if flanker_stimuli.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                flanker_stimuli.frameNStart = frameN  # exact frame index
                flanker_stimuli.tStart = t  # local t and not account for scr refresh
                flanker_stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_stimuli, 'tStartRefresh')  # time at next scr refresh
                flanker_stimuli.setAutoDraw(True)
            if flanker_stimuli.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > flanker_stimuli.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    flanker_stimuli.tStop = t  # not accounting for scr refresh
                    flanker_stimuli.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(flanker_stimuli, 'tStopRefresh')  # time at next scr refresh
                    flanker_stimuli.setAutoDraw(False)

            # *flanker_practice_resp* updates
            waitOnFlip = False
            if flanker_practice_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                flanker_practice_resp.frameNStart = frameN  # exact frame index
                flanker_practice_resp.tStart = t  # local t and not account for scr refresh
                flanker_practice_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_practice_resp, 'tStartRefresh')  # time at next scr refresh
                flanker_practice_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(flanker_practice_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(flanker_practice_resp.clearEvents,
                               eventType='keyboard')  # clear events on next screen flip
            if flanker_practice_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > flanker_practice_resp.tStartRefresh + 1 - frameTolerance:
                    # keep track of stop time/frame for later
                    flanker_practice_resp.tStop = t  # not accounting for scr refresh
                    flanker_practice_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(flanker_practice_resp, 'tStopRefresh')  # time at next scr refresh
                    flanker_practice_resp.status = FINISHED
            if flanker_practice_resp.status == STARTED and not waitOnFlip:
                theseKeys = flanker_practice_resp.getKeys(keyList=['l', 'f'], waitRelease=False)
                _flanker_practice_resp_allKeys.extend(theseKeys)
                if len(_flanker_practice_resp_allKeys):
                    flanker_practice_resp.keys = _flanker_practice_resp_allKeys[-1].name  # just the last key pressed
                    flanker_practice_resp.rt = _flanker_practice_resp_allKeys[-1].rt
                    # was this correct?
                    if (flanker_practice_resp.keys == str(canswer)) or (flanker_practice_resp.keys == canswer):
                        flanker_practice_resp.corr = 1
                    else:
                        flanker_practice_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False

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
        flanker_ex2.addData('flanker_stimuli.started', flanker_stimuli.tStartRefresh)
        flanker_ex2.addData('flanker_stimuli.stopped', flanker_stimuli.tStopRefresh)
        # check responses
        if flanker_practice_resp.keys in ['', [], None]:  # No response was made
            flanker_practice_resp.keys = None
            # was no response the correct answer?!
            if str(canswer).lower() == 'none':
                flanker_practice_resp.corr = 1;  # correct non-response
            else:
                flanker_practice_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for flanker_ex2 (TrialHandler)
        flanker_ex2.addData('flanker_practice_resp.keys', flanker_practice_resp.keys)
        flanker_ex2.addData('flanker_practice_resp.corr', flanker_practice_resp.corr)
        returnValue.ex_record.append(flanker_practice_resp.corr)
        if flanker_practice_resp.keys != None:  # we had a response
            flanker_ex2.addData('flanker_practice_resp.rt', flanker_practice_resp.rt)
        flanker_ex2.addData('flanker_practice_resp.started', flanker_practice_resp.tStartRefresh)
        flanker_ex2.addData('flanker_practice_resp.stopped', flanker_practice_resp.tStopRefresh)

        # ------Prepare to start Routine "interval"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        intervalComponents = [flanker_interval]
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

            # *flanker_interval* updates
            if flanker_interval.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                # keep track of start time/frame for later
                flanker_interval.frameNStart = frameN  # exact frame index
                flanker_interval.tStart = t  # local t and not account for scr refresh
                flanker_interval.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_interval, 'tStartRefresh')  # time at next scr refresh
                flanker_interval.setAutoDraw(True)
            if flanker_interval.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > flanker_interval.tStartRefresh + 2 - frameTolerance:
                    # keep track of stop time/frame for later
                    flanker_interval.tStop = t  # not accounting for scr refresh
                    flanker_interval.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(flanker_interval, 'tStopRefresh')  # time at next scr refresh
                    flanker_interval.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue

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
        flanker_ex2.addData('flanker_interval.started', flanker_interval.tStartRefresh)
        flanker_ex2.addData('flanker_interval.stopped', flanker_interval.tStopRefresh)
        thisExp.nextEntry()

    # completed 12.0 repeats of 'flanker_ex2'

    # ------Prepare to start Routine "end"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    endComponents = [flanker_end]
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

        # *flanker_end* updates
        if flanker_end.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            flanker_end.frameNStart = frameN  # exact frame index
            flanker_end.tStart = t  # local t and not account for scr refresh
            flanker_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(flanker_end, 'tStartRefresh')  # time at next scr refresh
            flanker_end.setAutoDraw(True)
        if flanker_end.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > flanker_end.tStartRefresh + 2 - frameTolerance:
                # keep track of stop time/frame for later
                flanker_end.tStop = t  # not accounting for scr refresh
                flanker_end.frameNStop = frameN  # exact frame index
                win.timeOnFlip(flanker_end, 'tStopRefresh')  # time at next scr refresh
                flanker_end.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue

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
    thisExp.addData('flanker_end.started', flanker_end.tStartRefresh)
    thisExp.addData('flanker_end.stopped', flanker_end.tStopRefresh)

    # Flip one final time so any remaining win.callOnFlip() 
    # and win.timeOnFlip() tasks get executed before quitting
    win.flip()

    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    win.close()
    return returnValue

# admin = 'admin'
# participant = 'participant'
# group = 'group'
# session = 'session'
# res=flanker(admin, participant, group, session)
# print(res)
