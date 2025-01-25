# library import 
from __future__ import division
from psychopy import visual, event, core
from psychopy.visual import ShapeStim
from psychopy import visual, core, data, event, misc, logging, gui
from psychopy.constants import * #things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, pre-pend 'np.'
import numpy
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os #handy system and path functions
from math import *
import random                   
#from psychopy.hardware.emulator import launchScan
#from CIEcolorwheel import CIEwheel, rotate, cart2pol
from psychopy.visual import ShapeStim
import math

# store info about the experiment session
expName = 'vwm_singleton'
expInfo = {'participant':'00'}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName

# setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
fileName='data' + os.path.sep + '%s_%s_%s' %(expName, expInfo['participant'], expInfo['date'])

# make a text file to save data
dataFile = open(fileName+'.txt', 'w')
dataFile.write('sbj\t' 'runidx\t' 'trialidx\t' 'block\t' 'wmload\t' 'trialtype\t' 'tloc\t' 'tid\t' 'tres\t' 'trt\t' 'tacc\t' 'mp\t' 'mprt\t' 'mpacc\n')

#win = visual.Window(allowGUI=False, fullscr=True, size = [1920,1080], color = 'black', colorSpace ='rgb', monitor='testMonitor', units='deg')
win = visual.Window(allowGUI=True, fullscr=False, size = [1200,1000], color = 'black', colorSpace ='rgb', monitor='testMonitor', units='deg')

## text 
readyText=visual.TextStim(win, ori=0, name='instrText',
    text='If you are feeling well and ready,\n\npress space bar to continue',
    font='Arial',
    pos=[0, 0], height=1,wrapWidth=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0)    

okText=visual.TextStim(win, ori=0, name='okText',
    text='Alright!!,\nThe experiment will start soon',
    font='Arial',
    pos=[0, 0], height=1,wrapWidth=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0)    

finishText=visual.TextStim(win, ori=0, name='instrText',
    text='This session is finished.\nPlease see the next experiment',
    font='Arial',
    pos=[0, 0], height=1,wrapWidth=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0) 
    
endText=visual.TextStim(win, ori=0, name='instrText',
    text='The experiment is ended!!!!\nPress ESC key',
    font='Arial',
    pos=[0, 0], height=1,wrapWidth=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0)
    
samediffText=visual.TextStim(win, ori=0, name='instrText',
    text='Same or Different?',
    font='Arial',
    pos=[0, 3.5], height=1,wrapWidth=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0)
    
## fixation
fixation = visual.TextStim(win, ori=0, name='fix_kreuz',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.5,wrapWidth=None,
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0)
    
fixation2 = visual.TextStim(win, ori=0, name='fix_kreuz',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.5,wrapWidth=None,
    color='gray', colorSpace='rgb', opacity=1,
    depth=0.0)

## method
def polarToRect(angleList,radius):
    """Accepts a list of angles and a radius.  Outputs the x,y positions for the angles"""
    coords=[]
    for curAngle in angleList:
        radAngle = (float(curAngle)*2.0*pi)/360.0
        xCoord = round(float(radius)*cos(radAngle),0)
        yCoord = round(float(radius)*sin(radAngle),0)
        coords.append([xCoord,yCoord])
    return coords
coords = polarToRect([0, 60, 120, 180, 240, 300], 5)  


def randomButNot (lst, item, k):
    randItemList = random.sample(lst, k)
    if item in randItemList:
        go = True
        while go:
            randItemList = random.sample(lst, k)
            if not item in randItemList:
                return randItemList
    else:
        return randItemList

## memory shape
square = ShapeStim(win, units='', lineWidth=4, lineColor=None, lineColorSpace='rgb', fillColor=None, fillColorSpace='rgb', 
             vertices=((-1, -1), (1, -1), (1, 1),(-1,1)), windingRule=None, closeShape=True, pos=(0, 0), size=0.64, autoLog=None, autoDraw=False)
             
triangle = ShapeStim(win, units='', lineWidth=4, lineColor=None, lineColorSpace='rgb', fillColor=None, fillColorSpace='rgb', 
             vertices=((-0.7, -0.4), (0, 0.6), (0.7, -0.4)), windingRule=None, closeShape=True, pos=(0, 0), size=1.2, autoLog=None, autoDraw=False)

star = ShapeStim(win, units='', lineWidth=4, lineColor=None, lineColorSpace='rgb', fillColor=None, fillColorSpace='rgb', 
             vertices=((-0.9,-0.4),(-0.3,-0.4),(0,-0.8),(0.3,-0.4),(0.9,-0.4),(0.6,0),(0.9,0.4),(0.3,0.4),(0,0.8),(-0.3,0.4),(-0.9,0.4),(-0.6,0)), windingRule=None, closeShape=True, pos=(0, 0), size=1, autoLog=None, autoDraw=False)

hexagon = ShapeStim(win, units='', lineWidth=4, lineColor=None, lineColorSpace='rgb', fillColor=None, fillColorSpace='rgb', 
             vertices=((-2, 0), (-1, -1.7),(1, -1.7),(2, 0), (1, 1.7), (-1, 1.7)), windingRule=None, closeShape=True, pos=(0, 0), size=0.4, autoLog=None, autoDraw=False)

circle = visual.Circle(win=win, units='',radius=1, fillColor=None, fillColorSpace='rgb', lineColor=None,
             lineWidth=4, pos=(0, 0), size=0.77, autoLog=None, autoDraw=False)
             

keyList = ['period', 'slash', 'escape']
center = (0,0)

##stimuli
tsize = 0.6
linethick = 0.1
greenvertices = [(tsize,tsize),(tsize,tsize-linethick),(linethick/2,tsize-linethick),(linethick/2,-tsize),(-linethick/2,-tsize),(-linethick/2,tsize-linethick),(-tsize,tsize-linethick),(-tsize,tsize)]
targetT = ShapeStim(win, vertices=greenvertices, lineColor=(0,0,0), fillColor='white', lineWidth=1, pos=(0, -4), ori=0, units='deg')
redT = ShapeStim(win, vertices=greenvertices, lineColor=(1, -1, -1), fillColor=(1, -1, -1), lineWidth=1, pos=(0, -4), ori=0, units='deg')
vertice = [(-tsize,tsize),(-tsize+linethick,tsize),(-tsize+linethick,-tsize+linethick),(tsize,-tsize+linethick),(tsize,-tsize),(-tsize,-tsize)]
verticeoffset= [(tsize,tsize),(tsize,tsize-linethick),(tsize/2+linethick/2,tsize-linethick),(tsize/2+linethick/2,-tsize),(tsize/2-linethick/2,-tsize),(tsize/2-linethick/2,tsize-linethick),(-tsize,tsize-linethick),(-tsize,tsize)]

## timing parameters
frameDur=0.1
okText_time = 1
center = (0, 0)


## 실험 인덱싱 만들기 ~ 경우의 수
sbjidx = int(expInfo['participant'])
sbj=0; runidx=1; trialidx=2;
block=3; nooffset=0; offset=1; #search mode는 blocked 처리
wmload=4; low=0; high=1;
trialtype=5; absent=0; present=1;
tloc=6;
tid=7; left=0; right=1;
mp=8; same=0; diff=1;
tres=9;
rt=10;
acc=12; wrong=0; right=1
mprt=12;
mpacc=13;

# trial 엮기 ~ 조건별로 달라지는 조건을 엮어야 함.
wmload = [low] + [high]
trialtype = [absent] + [present] # sigleton distractor
tloclist = [0,1,2,3,4,5]
tid = [left] + [right]
mp = [same] + [diff]
ntrial = (len(wmload)*len(trialtype)*len(tloclist)*len(tid)*len(mp)) # 2*2*6*2*2 = 96 trial

nrun = 6
inittrialidx = tempblock = 0
trial_exp = []
for currun in range(1,nrun+1):
    trialblock = []
    #for nRep in range(3):
    for curwmload in wmload: # low vs high
        for curtrialtype in trialtype: # absent vs present
            for curtloclist in tloclist: # [0,1,2,3,4,5]
                for curtid in tid: # left vs right
                    for curmp in mp: # same vs diff
                        trial = [sbjidx] + [currun] + [inittrialidx] + [tempblock] + [curwmload] + [curtrialtype] + [curtloclist] + [curtid] + [curmp]
                        trialblock.append(trial)
    random.seed()
    random.shuffle(trialblock)
    trial_exp.append(trialblock)

# print(trial_exp)


globalClock=core.Clock()
for currun in range(nrun):
    # similarity block
    if sbjidx % 2 == 0:
        if currun % 2 == 0:
            block = 0
            distvertice = vertice 
        elif currun % 2 == 1: 
            block = 1
            distvertice = verticeoffset
            
    elif sbjidx % 2 == 1:
        if currun % 2 == 0:
            block = 1
            distvertice = verticeoffset
        elif currun % 2 == 1: 
            block = 0
            distvertice = vertice
    
    readyText.draw()
    win.flip()
    event.waitKeys(keyList = ['space']) #remove max wait for behavioral experiment
    okText.draw()
    win.flip()
    core.wait(okText_time)
    fixation.draw()
    win.flip()
    core.wait(0.5)
    
    for curtrial in range(ntrial):
        fixation.draw() # fixation 그리기
        win.flip()
        fixationonset = globalClock.getTime()
        drawn = False
        while globalClock.getTime() - fixationonset <= 0.5:
            if drawn == False:
                fixation2.draw()
                drawn = True
            
            
        a = trial_exp[currun][curtrial]
        curwmload = a[4]
        curtrialtype = a[5]
        curtloc = a[6]
        curtid = a[7]
        curmp = a[8]
        
        
        ## WM task
        mcoords = polarToRect([90, 210, 330], 3); mloclist = [0,1,2];
        shapelist = [square, triangle, star, hexagon, circle]
        colorlist = ['mediumpurple','green','orange','indigo','yellowgreen']
        mshapelist = random.sample(shapelist, 3)
        mcolorlist = random.sample(colorlist, 3)
    
        if curwmload == 0: # low
            curmshape = mshapelist[0]
            curmshape.setPos(center)
            curmshape.setColor(mcolorlist[0])
            curmshape.draw()
            
        elif curwmload == 1: # high
            hmloc = random.sample(mloclist, 1) # mp에 등장할 mshape의 위치가 고정되지 않도록 random sampling
            mloclist.remove(hmloc[0])
            
            curmshape = mshapelist[0] # 나중에 mp로 사용할 mshape를 미리 선정
            curmshape.setPos(mcoords[hmloc[0]])
            curmshape.setColor(mcolorlist[0])
            curmshape.draw()
            for i in range(2):
                mshapelist[i+1].setPos(mcoords[mloclist[i]])
                mshapelist[i+1].setColor(mcolorlist[i+1])
                mshapelist[i+1].draw()
        
        win.flip()
        if curwmload == 0:
            mshapeonset = globalClock.getTime()
            drawn = False
            while globalClock.getTime() - mshapeonset <= 0.5:
                if drawn == False:
                    fixation2.draw()
                drawn = True
                    
        elif curwmload == 1:
            mshapeonset = globalClock.getTime()
            drawn = False
            while globalClock.getTime() - mshapeonset <= 1.5:
                if drawn == False:
                    fixation2.draw()
                drawn = True
        
        
        fixation.draw() # fixation 그리기
        win.flip()
        fixationonset = globalClock.getTime()
        drawn = False
        while globalClock.getTime() - fixationonset <= 0.5:
            if drawn == False:
                fixation2.draw()
            drawn = True


        ## TL task
        tcoords = polarToRect([0, 60, 120, 180, 240, 300], 5); tloclist = [0,1,2,3,4,5];
        distractorL = ShapeStim(win, vertices=distvertice, lineColor=(0,0,0), fillColor='white', lineWidth=1, pos=(0, 0), ori=0, units='deg') #non singleton
        singletonL = ShapeStim(win, vertices=distvertice, lineColor=(0,0,0), fillColor='white', lineWidth=1, pos=(0, 0), ori=0, units='deg') #singleton
        tloc = random.sample(tloclist, 1) # target T의 위치 먼저 sampleing
        tloclist.remove(tloc[0])
        scolorlist = ['cyan', 'magenta', 'yellow', 'red', 'blue']
        
        targetT.setPos(tcoords[tloc[0]]) # target T Orientation 및 Location 지정
        if curtid == 0:
            targetT.setOri(-90)
        elif curtid == 1:
            targetT.setOri(90)
        
        ltextori = [0, 90, -90, 90, -90] 
        if curtrialtype == present: # singleton present 조건에서 distractor L 먼저 그리기
            sloc = random.sample(tloclist, 1)
            scolor = random.sample(scolorlist, 1)
            sori = random.sample(ltextori, 1)
            tloclist.remove(sloc[0])
            singletonL.setPos(tcoords[sloc[0]])
            singletonL.setColor(scolor[0])
            singletonL.setOri(sori[0])
        
        searchonset = globalClock.getTime()
        drawn = False
        while globalClock.getTime() - searchonset <= 0.1:
            if drawn == False:
                targetT.draw()
                
                if curtrialtype == absent:
                    for i in range(5):
                        distractorL.setPos(tcoords[tloclist[i]])
                        distractorL.setOri(ltextori[i])
                        distractorL.draw()
                        
                elif curtrialtype == present:
                    for i in range(4):
                        distractorL.setPos(tcoords[tloclist[i]])
                        distractorL.setOri(ltextori[i])
                        distractorL.draw()
                    singletonL.draw()
                
            drawn == True
        win.flip()


        ## search response
        tres=0; tacc=0; trt=0;
        resptclock=core.Clock() #Clock 설정
        resptclock.reset() #시행마다 Clock 초기화
        event.clearEvents() 
        unresponded = True #반응하지 않은 상태
        while unresponded and resptclock.getTime()<=3: #unresponded가 True이고, 3초 이내에 반응이 일어났을 때 While문 실행
            tkey=event.getKeys(keyList=['period','slash','escape']) #피험자가 누른 key를 tkey에 저장
            if len(tkey) >0: #반응이 있었을 때
                trt=resptclock.getTime() #
                if tkey[0] == 'period': 
                    tres = 0
                elif tkey[0] == 'slash':
                    tres = 1
                elif tkey[0] == 'escape':
                    core.quit()
                unresponded=False #unresponded를 False로 바꾸어 while문 종료
                
        if len(tkey) >0:
            if (tres == 0 and curtid == 0) or (tres == 1 and curtid == 1):
                tacc = 1
              
        fixation.draw() # fixation 그리기
        win.flip()
        fixationonset = globalClock.getTime()
        drawn = False
        while globalClock.getTime() - fixationonset <= 0.5:
            if drawn == False:
                fixation2.draw()
            drawn = True
        
        
        # memory probe
        if curmp == 1: # diff
            random.shuffle(mcolorlist)
            mcolor = random.sample(mcolorlist, 1)
            curmshape.setColor(mcolor[0])
        
        mponset = globalClock.getTime()
        drawn = False
        while globalClock.getTime() - mponset <= 0.1:
            if drawn == False:
                curmshape.setPos(center)
                curmshape.draw()
                samediffText.draw()
                win.flip()
            drawn = True
            
        mpres=0; mpacc=0; mprt=0;
        respmpclock = core.Clock()
        respmpclock.reset()
        event.clearEvents()
        unresponded = True
        while unresponded and respmpclock.getTime() <=2:
            mpkey=event.getKeys(keyList=['period','slash','escape'])
            if len(mpkey) >0:
                mprt=respmpclock.getTime()
                if mpkey[0] == 'period':
                    mpres = 0
                elif mpkey[0] == 'slash':
                    mpres = 1
                elif mpkey[0] == 'escape':
                    core.quit()
                unresponded=False
                
        if len(mpkey) >0:
            if (mpres == 0 and curmp == 0) or (mpres == 1 and curmp == 1):
                mpacc = 1
        
        curtrialdata = [sbjidx] + [currun+1] + [curtrial+1]
        curtrialdata.append(block)
        curtrialdata.append(curwmload)
        curtrialdata.append(curtrialtype) 
        curtrialdata.append(curtloc)
        curtrialdata.append(curtid)
        curtrialdata.append(tres)
        curtrialdata.append(trt) 
        curtrialdata.append(tacc)
        curtrialdata.append(curmp)
        curtrialdata.append(mprt)
        curtrialdata.append(mpacc)
        
        line = '\t'.join(str(i) for i in curtrialdata)
        line += '\n'
        dataFile.write(line)
        dataFile.flush()
        os.fsync(dataFile)
        
ent_text = False
while ent_text == False:
    endText.draw()
    win.flip()
    if event.getKeys(keyList = ['escape']):
        core.quit()
        
core.quit()
