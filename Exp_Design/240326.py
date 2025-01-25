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
from psychopy.visual import ShapeStim
import math 

#win = visual.Window(allowGUI=False, fullscr=True, size = [1920,1080], color = 'black', colorSpace ='rgb', monitor='testMonitor', units='deg')
win = visual.Window(allowGUI=True, fullscr=False, size = [1400,1000], color = 'gray', colorSpace ='rgb', monitor='testMonitor', units='deg')

tsize = 0.6
linethick = 0.1

greenvertices = [(tsize,tsize),(tsize,tsize-linethick),(linethick/2,tsize-linethick),(linethick/2,-tsize),(-linethick/2,-tsize),(-linethick/2,tsize-linethick),(-tsize,tsize-linethick),(-tsize,tsize)]
greenT1 = ShapeStim(win, vertices=greenvertices, lineColor=(0,0,0), fillColor='green', lineWidth=1, pos=(0, -4), ori=0, units='deg')
redT = ShapeStim(win, vertices=greenvertices, lineColor=(1, -1, -1), fillColor=(1, -1, -1), lineWidth=1, pos=(0, -4), ori=0, units='deg')

distractorVertice = [(-tsize,tsize),(-tsize+linethick,tsize),(-tsize+linethick,-tsize+linethick),(tsize,-tsize+linethick),(tsize,-tsize),(-tsize,-tsize)]
distractorL = ShapeStim(win, vertices=distractorVertice, lineColor=(0,0,0), fillColor='red', lineWidth=1, pos=(0, 0), ori=0, units='deg')

## polarToRect
def polarToRect(angleList,radius):
    """Accepts a list of angles and a radius.  Outputs the x,y positions for the angles"""
    coords=[]
    for curAngle in angleList:
        radAngle = (float(curAngle)*2.0*pi)/360.0
        xCoord = round(float(radius)*cos(radAngle),0)
        yCoord = round(float(radius)*sin(radAngle),0)
        coords.append([xCoord,yCoord])
    return coords
coords = polarToRect([45, 135, 225, 315], 4)   

greenT1.setPos(coords[0])
greenT1.draw()
distractorL.setPos(coords[3])
distractorL.draw()
win.flip()
core.wait(2)

