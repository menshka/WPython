# ---------------------------------------------------------------------
# Copyright (c) Information Builders, Inc.  All rights reserved.
#
# _Name_        ===> wcsmpl01.py
# _Description_ ===>
#
# _History_:
#  Date  Time Who Proj       Project Title
# ====== ==== === ====== ==============================================
# 160314 1441 ias 175587 Testing Selenium tool with python
# 160310 1805 anm 175587 Testing Selenium tool with python
# 160309 1619 ias 175587 Testing Selenium tool with python
# 160304 1646 anm 175587 Testing Selenium tool with python
# 160303 1747 anm 175587 Testing Selenium tool with python
# 160229 1803 anm 175587 Testing Selenium tool with python
# 160225 1459 anm 175587 Testing Selenium tool with python
# 160223 1300 hms 175587 Testing Selenium tool with python
#
# END %&$
# ---------------------------------------------------------------------
print( "*************************************************************" )
print( "Test name: wcsmpl02")
print( "Area: testing py")
print( "Area: split test" )
print( "*************************************************************" )
# =============================================================================
# Importing Libs                           
# =============================================================================
#Lib for taking screen shots and log
import tstlog
#Importing all var from appconfig
from appconfig import *
#from gvar import *
#from xpathvar import *
#Importing appconfig to use closedriver function
import appconfig
#Importing WC action for arrow
import actions
# =============================================================================

# =============================================================================
# Test case                            
# =============================================================================
#Open DMHR synonym, select Join, added a child, Edit Parent link, change parameters and test sample data.
#Deleting output file before test starts. If file is not find suppress errors\
tstlog.logfileibi(__file__)
try:
	#Input User Name and or password
	actions.serverlogin('','','Login Screen','y')
	#Press Sign In button and take a screen shot
	actions.singleclick('','Sign In','rbutton','Main Screen','','y')
	#tstlog.printscreen('Main Screen')
	actions.singleclick('','Filter',regbutton,'Click on Filter','','y')
	#Select advanced option in Filter and take a screen shot
	actions.singleclick('','Advanced',textsel,'Click on the Advanced Filter','','y')
	#input synonym value in File name and take a screen shot
	actions.textinput('File Name',textinput, 'dmhr%', 'Filter Options','y')
	#Click on set Filter button
	actions.singleclick('','Set Filter',regbutton,'Filter Set','','y')
	#Need add wait for the object
	actions.doubleclick('dmhr -',textsel,'Select DMHR','Fields into Measures, Dimensions and Hierarchie','y')
	#Click on add Join button and take a print screen
	actions.singleclick('','Join',regbutton,'Join Button','Application Tree','y')
	#Click insert child button and take a print screen
	actions.singleclick('','Insert Child',regbutton,'Select Child Synonym','Filtering:','y')
	#Selecting DMQCB synonym and take a screen shot
	actions.singleclick('','dmterm',textsel,'Select DHMRTERM','','y')
	#Pressing OK button
	actions.singleclick('','OK',textsel,'OK button was pressed','','y')
	#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wcjoinarrow)))
	actions.RightClickSvgLine('svg01-line', 'y')
	#Selecting Edit Parent Link
	actions.singleclick('','Edit Parent Link',textsel,'Connection Menu','','y')
	#Selecting Right Outer Join
	actions.singleclick('','_right_b',idsel,'Select Join Type','','y')
	#Selecting Advanced option
	actions.singleclick(bottompanelcont,'Advanced',textsel,'Press on Advanced button','','y')
	#Selecting arrow down under from field
	actions.singleclick('','row-0-col-1-object',idsel,'List Select','','y')
	#Selectiong Position, Description item in combo box
	actions.singleclick('','Salary',wclisteitem,'Description','','y')
	#Displaying Sample Data
	actions.singleclick('','wc_test_join_16.png',wcimagesel,'Pressing Sample Data','Sample Data with Parent Key','y')
	#Keeping browser open to see loaded data
	#time.sleep(3)
	tstlog.passfile()
	appconfig.closedriver()
except:
	tstlog.failedfile()
	appconfig.closedriver()
	raise SystemExit
# =============================================================================