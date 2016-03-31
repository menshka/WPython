# ---------------------------------------------------------------------
# Copyright (c) Information Builders, Inc.  All rights reserved.
#
# _Name_        ===> tstlog.py
# _Description_ ===>
#
# _History_:
#  Date  Time Who Proj       Project Title
# ====== ==== === ====== ==============================================
# 160321 1612 anm 175587 Testing Selenium tool with python
# 160316 1656 anm 175587 Testing Selenium tool with python
# 160315 1812 anm 175587 Testing Selenium tool with python
# 160315 1810 anm 175587 Testing Selenium tool with python
#
# END %&$
# ---------------------------------------------------------------------
# =============================================================================
# Importing Libs and defining global variables                              
# =============================================================================
#OS Module
import os
#Logging Module
import logging
#Import webdriver
from selenium import webdriver
#Defining testfile variable
global testfile
#Defining log
global getdir
#Getting value from env variable pyworkddir
getdir = os.environ.get('pyworkdir')
global br
#Getting value from env variable BrSelect
br = os.environ.get('BrSelect')
#Defining logfiledebug as global
global logfiledebug
#from appconfig import bset
import base64
#Importing date lib
import datetime
#Importing webdriver conf file
import appconfig
#Importing all vars from webdriver conf file
from appconfig import *
#Importing time
from datetime import datetime
global stepNum
stepNum = 0
# =============================================================================	

# =============================================================================
# LogStep: Add steps to log file                                
# =============================================================================	
def logfileibi(scriptfile):
	global logger
	global getdir
	global br
	global testfile
	testfile = os.path.basename(scriptfile[0:-3])
	global logfile
	logfile = os.path.join(getdir, testfile +'_' + br + '.html')
	global logfiledebug
	logfiledebug = os.path.join(getdir, testfile +'_' + br + 'debug' + '.txt')
	#Recording Log
	#When this option is activated initcreatehtml() creates initial html file
	initcreatehtml()
	#Setting logging options using logger as a utility 
	logger = logging.getLogger()
	logger2 = logging.getLogger()
	#Setting logger level
	logger.setLevel(logging.ERROR)
	logger2.setLevel(logging.DEBUG)
	#Setting file handler
	fh = logging.FileHandler(logfile)
	dh = logging.FileHandler(logfiledebug)
	#Defining what format to use
	formatter = logging.Formatter('<b>' + '<p>' + '[%(asctime)s] %(message)s' + '</p>' + '</b>')
	formatterd = logging.Formatter('[%(asctime)s] %(message)s')
	#Setting logging level for new handler
	fh.setLevel(logging.ERROR)
	dh.setLevel(logging.DEBUG)
	#Telling handler what format to use
	fh.setFormatter(formatter)
	dh.setFormatter(formatterd)
	#Intitiating handler
	logger.addHandler(fh)
	logger2.addHandler(dh)
	#First line in output
	logger.error("Test script: " + testfile + ' ' + "output" + ".")
# =============================================================================	


# =============================================================================
# Creating initial html file with the name of the running file                          
# =============================================================================
def initcreatehtml():	
	global logfile
	global testfile
	global getdir
	global br
	#Creating output html and adding tags
	f = open(logfile, 'a')
	tags = """<htlm><head><title>""" + testfile + """</title></head>"""
	f.write(tags)
# =============================================================================

# =============================================================================
# Creating initial html file with the name of the running file                          
# =============================================================================
def initclosehtml():
	global testfile
	global logfile
	f = open(logfile, 'a')
	closetags = """</body></html>"""
	f.write(closetags)
# =============================================================================

# =============================================================================
# Taking print screen                          
# =============================================================================
def printscreen(step):
	global driver
	global testfile
	global logfile
	global br
	logfile = os.path.join(getdir, testfile +'_' + br + '.html')
	savedir2 = os.path.join(getdir, testfile + '_' + br +'_' + step + '_' + '.png')
	driver.save_screenshot(savedir2)
	f = open(logfile, 'a')
	imagedef = base64.b64encode(open(getdir + testfile + '_' + br +'_' + step + '_' + '.png', 'rb').read()).decode('utf-8').replace('\n', '')
	imgtag = '<img src="data:image/png;base64,%s">' % imagedef
	StepNumber()
	logger.error(step)
	f.write(imgtag)
	f.close()
# =============================================================================	

# =============================================================================
# Create file on successfull test execution                         
# =============================================================================
def passfile():
	global getdir
	global testfile
	global br
	statusfile = os.path.join(getdir, testfile +'_' + br + '_passed' '.txt')
	f = open(statusfile, 'w')
	f.close()
	logger.error('Test Passed')
# =============================================================================	

# =============================================================================
# Create file on un-successfull test execution                         
# =============================================================================
def failedfile():
	global getdir
	global testfile
	global br
	f = open(logfile, 'a')
	f.write('<font color="red">')
	printscreen('Following step is failed')
	statusfile = os.path.join(getdir, testfile +'_' + br + '_failed' '.txt')
	f.close
	f = open(statusfile, 'w')
	f.close()
	logging.exception('Error Message: ')
# =============================================================================		

# =============================================================================
# Adding Steps #                        
# =============================================================================
def StepNumber():
	global stepNum
	global logfile
	stepNum += 1
	logger.info('[' 'Step # ' + (str(stepNum)) + ']' + ' ')
	f = open(logfile, 'a')
	f.write('<b><p>')
	f.write('[' 'Step # ' + (str(stepNum)) + ']' + '&nbsp')
	f.write('</b></p>')
	f.close()
# =============================================================================

# =============================================================================
# Adding Steps #                        
# =============================================================================
def noprintscreen(step):
	global logfile
	global stepNUM
	StepNumber()
	logger.error(step +  ' ' + 'Print Screen is not taken' + ' ')
# =============================================================================	