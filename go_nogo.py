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


#资源文件目录访问
# def source_path(relative_path):
# 	#是否Bundle Resource
#     if getattr(sys, 'frozen', False): 
#         base_path = sys._MEIPASS
#     else:
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)

class goNogoResponse:
    practice_record=[]
    ex_record=[]

    def __init__(self,practice,ex):
        self.practice_record=practice
        self.ex_record=ex
    def getPracticeAccurate(self):
        return sum(self.practice_record)/len(self.practice_record)
    def getExAccurate(self):
        return sum(self.ex_record)/len(self.ex_record)


# def go_Nogo(admin,participant,gender,session):
def go_Nogo(admin,participant,group,session):
    # Ensure that relative paths start from the same directory as this script
    # _thisDir = os.path.dirname(os.path.abspath(__file__))
    _thisDir="."
    # print(_thisDir)
    # os.chdir(_thisDir)

       # Store info about the experiment session
    expInfo = {}
    expInfo['admin']=admin
    expInfo['participant']=participant
    expInfo['session']=session
    expName="flanker"
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    print(expInfo['date'])
    
    returnValue=goNogoResponse([],[],)

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc

    filename = _thisDir + os.sep + u'data/go_nogo/%s/%s/%s/%s' % (admin,participant,group,session)

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

    # Initialize components for Routine "Instruction"
    InstructionClock = core.Clock()
    textInstr = visual.TextStim(win=win, name='textInstr',
        text='欢迎参加实验\n\n当出现白色三角形和长方形时\n\n请快速且准确的按键盘J键\n\n而当出现紫色三角形和长方形时，请不要按任何键\n\n明白后按空格键进入实验',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instr = keyboard.Keyboard()

    # Initialize components for Routine "corrs"
    corrsClock = core.Clock()
    polygon = visual.ShapeStim(
        win=win, name='polygon', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0),
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    rt1 = 0

    # Initialize components for Routine "Practice"
    PracticeClock = core.Clock()
    image_stims = visual.ImageStim(
        win=win,
        name='image_stims', 
        image='sin', mask=None,
        ori=0.0, pos=(0, 0), size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_stim = keyboard.Keyboard()

    # Initialize components for Routine "Blank"
    BlankClock = core.Clock()
    textBlank = visual.TextStim(win=win, name='textBlank',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "feedback"
    feedbackClock = core.Clock()
    text_fb = visual.TextStim(win=win, name='text_fb',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "Start"
    StartClock = core.Clock()
    textStart = visual.TextStim(win=win, name='textStart',
        text='练习试次已结束，请按空格键开始正式实验',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard()

    # Initialize components for Routine "corrs"
    corrsClock = core.Clock()
    polygon = visual.ShapeStim(
        win=win, name='polygon', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0),
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    rt1 = 0

    # Initialize components for Routine "stim"
    stimClock = core.Clock()
    image_stims_2 = visual.ImageStim(
        win=win,
        name='image_stims_2', 
        image='sin', mask=None,
        ori=0.0, pos=(0, 0), size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_stim_2 = keyboard.Keyboard()

    # Initialize components for Routine "Blank"
    BlankClock = core.Clock()
    textBlank = visual.TextStim(win=win, name='textBlank',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "rest"
    restClock = core.Clock()
    text = visual.TextStim(win=win, name='text',
        text='休息一下，按空格键继续实验',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()

    # Initialize components for Routine "corrs"
    corrsClock = core.Clock()
    polygon = visual.ShapeStim(
        win=win, name='polygon', vertices='cross',
        size=(0.1, 0.1),
        ori=0.0, pos=(0, 0),
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    rt1 = 0

    # Initialize components for Routine "stim"
    stimClock = core.Clock()
    image_stims_2 = visual.ImageStim(
        win=win,
        name='image_stims_2', 
        image='sin', mask=None,
        ori=0.0, pos=(0, 0), size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    key_stim_2 = keyboard.Keyboard()

    # Initialize components for Routine "Blank"
    BlankClock = core.Clock()
    textBlank = visual.TextStim(win=win, name='textBlank',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "End"
    EndClock = core.Clock()
    textEnd = visual.TextStim(win=win, name='textEnd',
        text='实验到此结束！感谢您的参与！',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    # ------Prepare to start Routine "Instruction"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_instr.keys = []
    key_instr.rt = []
    _key_instr_allKeys = []
    # keep track of which components have finished
    InstructionComponents = [textInstr, key_instr]
    for thisComponent in InstructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "Instruction"-------
    while continueRoutine:
        # get current time
        t = InstructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textInstr* updates
        if textInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInstr.frameNStart = frameN  # exact frame index
            textInstr.tStart = t  # local t and not account for scr refresh
            textInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstr, 'tStartRefresh')  # time at next scr refresh
            textInstr.setAutoDraw(True)
        
        # *key_instr* updates
        waitOnFlip = False
        if key_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_instr.frameNStart = frameN  # exact frame index
            key_instr.tStart = t  # local t and not account for scr refresh
            key_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instr, 'tStartRefresh')  # time at next scr refresh
            key_instr.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instr.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instr.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instr.status == STARTED and not waitOnFlip:
            theseKeys = key_instr.getKeys(keyList=['space'], waitRelease=False)
            _key_instr_allKeys.extend(theseKeys)
            if len(_key_instr_allKeys):
                key_instr.keys = _key_instr_allKeys[-1].name  # just the last key pressed
                key_instr.rt = _key_instr_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Instruction"-------
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    PracticeTrials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        # trialList=data.importConditions('tableResource/go_nogo.xlsx'),
        trialList=data.importConditions('tableResource/go_nogo.xlsx'),
        seed=None, name='PracticeTrials')
    thisExp.addLoop(PracticeTrials)  # add the loop to the experiment
    thisPracticeTrial = PracticeTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            exec('{} = thisPracticeTrial[paramName]'.format(paramName))

    for thisPracticeTrial in PracticeTrials:
        currentLoop = PracticeTrials
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
        if thisPracticeTrial != None:
            for paramName in thisPracticeTrial:
                exec('{} = thisPracticeTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "corrs"-------
        continueRoutine = True
        # update component parameters for each repeat
        from numpy.random import shuffle
        
        d=[0.5,0.5,0.7,0.8,0.9,1.0]
        shuffle(d)
        rt1=d.pop()
        
        thisExp.addData("rt1",rt1)
        # keep track of which components have finished
        corrsComponents = [polygon]
        pic=thisPracticeTrial['pic']
        corrAns=thisPracticeTrial['corrAns']
        for thisComponent in corrsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        corrsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "corrs"-------
        while continueRoutine:
            # get current time
            t = corrsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=corrsClock)
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
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + rt1-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in corrsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "corrs"-------
        for thisComponent in corrsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        PracticeTrials.addData('polygon.started', polygon.tStartRefresh)
        PracticeTrials.addData('polygon.stopped', polygon.tStopRefresh)
        # the Routine "corrs" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Practice"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        image_stims.setImage(pic)
        key_stim.keys = []
        key_stim.rt = []
        _key_stim_allKeys = []
        # keep track of which components have finished
        PracticeComponents = [image_stims, key_stim]
        for thisComponent in PracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Practice"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = PracticeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_stims* updates
            if image_stims.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_stims.frameNStart = frameN  # exact frame index
                image_stims.tStart = t  # local t and not account for scr refresh
                image_stims.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_stims, 'tStartRefresh')  # time at next scr refresh
                image_stims.setAutoDraw(True)
            if image_stims.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_stims.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_stims.tStop = t  # not accounting for scr refresh
                    image_stims.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_stims, 'tStopRefresh')  # time at next scr refresh
                    image_stims.setAutoDraw(False)
            
            # *key_stim* updates
            waitOnFlip = False
            if key_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_stim.frameNStart = frameN  # exact frame index
                key_stim.tStart = t  # local t and not account for scr refresh
                key_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_stim, 'tStartRefresh')  # time at next scr refresh
                key_stim.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_stim.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_stim.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_stim.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_stim.tStop = t  # not accounting for scr refresh
                    key_stim.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_stim, 'tStopRefresh')  # time at next scr refresh
                    key_stim.status = FINISHED
            if key_stim.status == STARTED and not waitOnFlip:
                theseKeys = key_stim.getKeys(keyList=['j'], waitRelease=False)
                _key_stim_allKeys.extend(theseKeys)
                if len(_key_stim_allKeys):
                    key_stim.keys = _key_stim_allKeys[-1].name  # just the last key pressed
                    key_stim.rt = _key_stim_allKeys[-1].rt
                    # was this correct?
                    if (key_stim.keys == str(corrAns)) or (key_stim.keys == corrAns):
                        key_stim.corr = 1
                    else:
                        key_stim.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Practice"-------
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_stim.keys in ['', [], None]:  # No response was made
            key_stim.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
                key_stim.corr = 1;  # correct non-response
            else:
                key_stim.corr = 0;  # failed to respond (incorrectly)
        # store data for PracticeTrials (TrialHandler)
        PracticeTrials.addData('key_stim.keys',key_stim.keys)
        PracticeTrials.addData('key_stim.corr', key_stim.corr)
        returnValue.practice_record.append(key_stim.corr)
        if key_stim.keys != None:  # we had a response
            PracticeTrials.addData('key_stim.rt', key_stim.rt)
        PracticeTrials.addData('key_stim.started', key_stim.tStartRefresh)
        PracticeTrials.addData('key_stim.stopped', key_stim.tStopRefresh)
        
        # ------Prepare to start Routine "Blank"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        BlankComponents = [textBlank]
        for thisComponent in BlankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BlankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Blank"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = BlankClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BlankClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textBlank* updates
            if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textBlank.frameNStart = frameN  # exact frame index
                textBlank.tStart = t  # local t and not account for scr refresh
                textBlank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
                textBlank.setAutoDraw(True)
            if textBlank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textBlank.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textBlank.tStop = t  # not accounting for scr refresh
                    textBlank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
                    textBlank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Blank"-------
        for thisComponent in BlankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "feedback"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        if key_stim.corr == 1:
            text_fb.setText('正确')
        else:
            text_fb.setText('错误')
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
        PracticeTrials.addData('text_fb.started', text_fb.tStartRefresh)
        PracticeTrials.addData('text_fb.stopped', text_fb.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'PracticeTrials'


    # ------Prepare to start Routine "Start"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    StartComponents = [textStart, key_resp_2]
    for thisComponent in StartComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    StartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "Start"-------
    while continueRoutine:
        # get current time
        t = StartClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=StartClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textStart* updates
        if textStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textStart.frameNStart = frameN  # exact frame index
            textStart.tStart = t  # local t and not account for scr refresh
            textStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textStart, 'tStartRefresh')  # time at next scr refresh
            textStart.setAutoDraw(True)
        
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
        for thisComponent in StartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Start"-------
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
    thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "Start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    block1 = data.TrialHandler(nReps=20.0, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('tableResource/go_nogo.xlsx'),
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
        
        # ------Prepare to start Routine "corrs"-------
        continueRoutine = True
        # update component parameters for each repeat
        from numpy.random import shuffle
        
        d=[0.5,0.5,0.7,0.8,0.9,1.0]
        shuffle(d)
        rt1=d.pop()
        
        thisExp.addData("rt1",rt1)
        # keep track of which components have finished
        corrsComponents = [polygon]
        pic=thisBlock1['pic']
        corrAns=thisBlock1['corrAns']
        for thisComponent in corrsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        corrsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "corrs"-------
        while continueRoutine:
            # get current time
            t = corrsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=corrsClock)
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
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + rt1-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in corrsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "corrs"-------
        for thisComponent in corrsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block1.addData('polygon.started', polygon.tStartRefresh)
        block1.addData('polygon.stopped', polygon.tStopRefresh)
        # the Routine "corrs" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "stim"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        image_stims_2.setImage(pic)
        key_stim_2.keys = []
        key_stim_2.rt = []
        _key_stim_2_allKeys = []
        # keep track of which components have finished
        stimComponents = [image_stims_2, key_stim_2]
        for thisComponent in stimComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stimClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stim"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stimClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stimClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_stims_2* updates
            if image_stims_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_stims_2.frameNStart = frameN  # exact frame index
                image_stims_2.tStart = t  # local t and not account for scr refresh
                image_stims_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_stims_2, 'tStartRefresh')  # time at next scr refresh
                image_stims_2.setAutoDraw(True)
            if image_stims_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_stims_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_stims_2.tStop = t  # not accounting for scr refresh
                    image_stims_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_stims_2, 'tStopRefresh')  # time at next scr refresh
                    image_stims_2.setAutoDraw(False)
            
            # *key_stim_2* updates
            waitOnFlip = False
            if key_stim_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_stim_2.frameNStart = frameN  # exact frame index
                key_stim_2.tStart = t  # local t and not account for scr refresh
                key_stim_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_stim_2, 'tStartRefresh')  # time at next scr refresh
                key_stim_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_stim_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_stim_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_stim_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_stim_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_stim_2.tStop = t  # not accounting for scr refresh
                    key_stim_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_stim_2, 'tStopRefresh')  # time at next scr refresh
                    key_stim_2.status = FINISHED
            if key_stim_2.status == STARTED and not waitOnFlip:
                theseKeys = key_stim_2.getKeys(keyList=['j'], waitRelease=False)
                _key_stim_2_allKeys.extend(theseKeys)
                if len(_key_stim_2_allKeys):
                    key_stim_2.keys = _key_stim_2_allKeys[-1].name  # just the last key pressed
                    key_stim_2.rt = _key_stim_2_allKeys[-1].rt
                    # was this correct?
                    if (key_stim_2.keys == str(corrAns)) or (key_stim_2.keys == corrAns):
                        key_stim_2.corr = 1
                    else:
                        key_stim_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stim"-------
        for thisComponent in stimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_stim_2.keys in ['', [], None]:  # No response was made
            key_stim_2.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
                key_stim_2.corr = 1;  # correct non-response
            else:
                key_stim_2.corr = 0;  # failed to respond (incorrectly)
        # store data for block1 (TrialHandler)
        block1.addData('key_stim_2.keys',key_stim_2.keys)
        block1.addData('key_stim_2.corr', key_stim_2.corr)
        returnValue.ex_record.append(key_stim_2.corr)
        if key_stim_2.keys != None:  # we had a response
            block1.addData('key_stim_2.rt', key_stim_2.rt)
        block1.addData('key_stim_2.started', key_stim_2.tStartRefresh)
        block1.addData('key_stim_2.stopped', key_stim_2.tStopRefresh)
        
        # ------Prepare to start Routine "Blank"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        BlankComponents = [textBlank]
        for thisComponent in BlankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BlankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Blank"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = BlankClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BlankClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textBlank* updates
            if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textBlank.frameNStart = frameN  # exact frame index
                textBlank.tStart = t  # local t and not account for scr refresh
                textBlank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
                textBlank.setAutoDraw(True)
            if textBlank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textBlank.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textBlank.tStop = t  # not accounting for scr refresh
                    textBlank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
                    textBlank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Blank"-------
        for thisComponent in BlankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 20.0 repeats of 'block1'


    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    restComponents = [text, key_resp]
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
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
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
    thisExp.addData('text.started', text.tStartRefresh)
    thisExp.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
    thisExp.addData('key_resp.started', key_resp.tStartRefresh)
    thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    block2 = data.TrialHandler(nReps=20.0, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        # trialList=data.importConditions('tableResource/go_nogo.xlsx'),
        trialList=data.importConditions('tableResource/go_nogo.xlsx'),
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
        
        # ------Prepare to start Routine "corrs"-------
        continueRoutine = True
        # update component parameters for each repeat
        from numpy.random import shuffle
        
        d=[0.5,0.5,0.7,0.8,0.9,1.0]
        shuffle(d)
        rt1=d.pop()
        
        thisExp.addData("rt1",rt1)
        # keep track of which components have finished
        corrsComponents = [polygon]
        pic=thisBlock2['pic']
        corrAns=thisBlock2['corrAns']
        for thisComponent in corrsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        corrsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "corrs"-------
        while continueRoutine:
            # get current time
            t = corrsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=corrsClock)
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
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + rt1-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in corrsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "corrs"-------
        for thisComponent in corrsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block2.addData('polygon.started', polygon.tStartRefresh)
        block2.addData('polygon.stopped', polygon.tStopRefresh)
        # the Routine "corrs" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "stim"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        image_stims_2.setImage(pic)
        key_stim_2.keys = []
        key_stim_2.rt = []
        _key_stim_2_allKeys = []
        # keep track of which components have finished
        stimComponents = [image_stims_2, key_stim_2]
        for thisComponent in stimComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stimClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stim"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stimClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stimClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_stims_2* updates
            if image_stims_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_stims_2.frameNStart = frameN  # exact frame index
                image_stims_2.tStart = t  # local t and not account for scr refresh
                image_stims_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_stims_2, 'tStartRefresh')  # time at next scr refresh
                image_stims_2.setAutoDraw(True)
            if image_stims_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_stims_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_stims_2.tStop = t  # not accounting for scr refresh
                    image_stims_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_stims_2, 'tStopRefresh')  # time at next scr refresh
                    image_stims_2.setAutoDraw(False)
            
            # *key_stim_2* updates
            waitOnFlip = False
            if key_stim_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_stim_2.frameNStart = frameN  # exact frame index
                key_stim_2.tStart = t  # local t and not account for scr refresh
                key_stim_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_stim_2, 'tStartRefresh')  # time at next scr refresh
                key_stim_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_stim_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_stim_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_stim_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_stim_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_stim_2.tStop = t  # not accounting for scr refresh
                    key_stim_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_stim_2, 'tStopRefresh')  # time at next scr refresh
                    key_stim_2.status = FINISHED
            if key_stim_2.status == STARTED and not waitOnFlip:
                theseKeys = key_stim_2.getKeys(keyList=['j'], waitRelease=False)
                _key_stim_2_allKeys.extend(theseKeys)
                if len(_key_stim_2_allKeys):
                    key_stim_2.keys = _key_stim_2_allKeys[-1].name  # just the last key pressed
                    key_stim_2.rt = _key_stim_2_allKeys[-1].rt
                    # was this correct?
                    if (key_stim_2.keys == str(corrAns)) or (key_stim_2.keys == corrAns):
                        key_stim_2.corr = 1
                    else:
                        key_stim_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stim"-------
        for thisComponent in stimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_stim_2.keys in ['', [], None]:  # No response was made
            key_stim_2.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
                key_stim_2.corr = 1;  # correct non-response
            else:
                key_stim_2.corr = 0;  # failed to respond (incorrectly)
        # store data for block2 (TrialHandler)
        block2.addData('key_stim_2.keys',key_stim_2.keys)
        block2.addData('key_stim_2.corr', key_stim_2.corr)
        returnValue.ex_record.append(key_stim_2.corr)
        if key_stim_2.keys != None:  # we had a response
            block2.addData('key_stim_2.rt', key_stim_2.rt)
        block2.addData('key_stim_2.started', key_stim_2.tStartRefresh)
        block2.addData('key_stim_2.stopped', key_stim_2.tStopRefresh)
        
        # ------Prepare to start Routine "Blank"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        BlankComponents = [textBlank]
        for thisComponent in BlankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BlankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Blank"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = BlankClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BlankClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textBlank* updates
            if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textBlank.frameNStart = frameN  # exact frame index
                textBlank.tStart = t  # local t and not account for scr refresh
                textBlank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
                textBlank.setAutoDraw(True)
            if textBlank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textBlank.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textBlank.tStop = t  # not accounting for scr refresh
                    textBlank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
                    textBlank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                return returnValue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Blank"-------
        for thisComponent in BlankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 20.0 repeats of 'block2'


    # ------Prepare to start Routine "End"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    EndComponents = [textEnd]
    for thisComponent in EndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "End"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EndClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EndClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textEnd* updates
        if textEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textEnd.frameNStart = frameN  # exact frame index
            textEnd.tStart = t  # local t and not account for scr refresh
            textEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textEnd, 'tStartRefresh')  # time at next scr refresh
            textEnd.setAutoDraw(True)
        if textEnd.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textEnd.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                textEnd.tStop = t  # not accounting for scr refresh
                textEnd.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textEnd, 'tStopRefresh')  # time at next scr refresh
                textEnd.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            return returnValue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "End"-------
    for thisComponent in EndComponents:
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


# admin = 'admin'
# participant = 'participant'
# group = 'group'
# session = 'session'
# res=go_Nogo(admin, participant, group, session)
# print(res)