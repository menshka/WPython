# ---------------------------------------------------------------------
# Copyright (c) Information Builders, Inc.  All rights reserved.
#
# _Name_        ===> wcsmpl01.py
# _Description_ ===>
#
# _History_:
#  Date  Time Who Proj       Project Title
# ====== ==== === ====== ==============================================
#             anm 175587 Testing Selenium tool with python
# 160329 1357 anm 175587 Testing Selenium tool with python
# 160324 1516 anm 175587 Testing Selenium tool with python
# 160323 1535 anm 175587 Testing Selenium tool with python
# 160318 1445 anm 175587 Testing Selenium tool with python
# 160317 1324 anm 175587 Testing Selenium tool with python
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
print( "Test name: wcsmpl01")
print( "Area: testing py")
print( "Area: the first time" )
print( "*************************************************************" )

#Select browser type
#For Firefox set driver to webdriver.Firefox()
#For Chrome set driver to webdriver.Chrome()
#For Chrome donwload chromedriver.exe and add to the directory where this script is ran from
#For IE set driver to webdriver.Ie('C:\'Your Directory'\iedriverserver.exe')
#For IE read download webdriver tool for IE11, iedriverserver.exe, set path and regedit
#See how to set up on https://www.microsoft.com/en-us/download/details.aspx?id=44069
#More explanation on https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver	
#Import lib  for python test
import unittest
#Imporitng time so page doesn't close for some time
import time
#Inmport system options
import sys
#Import lib to use regular expression Perl styler
from selenium import webdriver
#Import lib to use browswer commons keys, return, up, down etc...
from selenium.webdriver.common.keys import Keys
#Import expected conditions to check existence of items on the pages
from selenium.webdriver.support import expected_conditions as EC
#Import wait option
from selenium.webdriver.support.ui import WebDriverWait
#Import option to chain actions
from selenium.webdriver.common.action_chains import ActionChains
#Import lib to supress errors
import contextlib
#Import lib to use system commands like delete files, modify etc
import os
#Import lib to create logs and work with logging errors
import logging
#Import lib for regular expressions
import re
#Import lib to remove directory
import shutil
#Import lib to use by
from selenium.webdriver.common.by import By
#Lib for taking screen shots
import base64
#Lib for using date
import datetime
#Import options for the IE
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#Making driver global variable
global driver


#Defining a class where we retrive based on env variable what browser we use
class bset:
    def getdriver():
    	bdrive = os.environ.get('BrSelect')
    	if bdrive == 'chrome':
    		return webdriver.Chrome()
    	elif bdrive == 'firefox':
    		return webdriver.Firefox()
    	elif bdrive == 'ie':
    		os.system('RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 2')
    		caps = DesiredCapabilities.INTERNETEXPLORER
    		caps['ignoreProtectedModeSettings'] = True
    		return webdriver.Ie('iedriverserver.exe', caps)

#Defining a class to use different logging output format for different levels
class FormatterNotFormattingInfo(logging.Formatter):
    def __init__(self, fmt = '<p>[%(asctime)s] %(message)s</p>'):
        logging.Formatter.__init__(self, fmt)

    def format(self, record):
        if record.levelno == logging.INFO:
            return record.getMessage()
        return logging.Formatter.format(self, record)

#Defining all of the connection variables from env variables
def getinfo():
	#Server name from env variable
	global server
	server = os.environ.get('wcinputserver')
	#Port name from env variable
	global port
	port = os.environ.get('wcinputport')
	#User name from env variable
	global user
	user = os.environ.get('wcusername')
	#Password name from env variable
	global password
	password = os.environ.get('wcuserpassword')
	#Start of server string
	global http
	http = 'http://'
	#Seprator of server and port
	global sep
	sep = ':'
	#File output directory from env variable
	global getdir
	getdir = os.environ.get('pyworkdir')
	#File
	global br
	br = os.environ.get('BrSelect')

#Defining all parameters as global variables in function so they can be re-used and values changed
def wcglobalitems():
	#Login field
	global wclogin
	wclogin = "//*[contains(@id, 'BiTextField')]"
	#Password field
	global wcloginpass
	wcloginpass = "//*[contains(@id, 'BiPasswordField')]"
	#Sign In button
	global wcsingin
	wcsingin = "//*[contains(@id, 'BiLabel') and contains(text(), 'Sign In')]"
	#Filter button
	global wcfilterbutton
	wcfilterbutton = "//*[contains(@id, 'BiLabel') and contains(text(), 'Filter')]"
	#Advanced filter option
	global wcadvancedselect
	wcadvancedselect = "//*[contains(text(), 'Advanced')]"
	#File Name input field
	global wcvaluetextfield
	wcvaluetextfield = '//div[2]/input'
	#Input value in File Name field
	global wcinputvalue
	wcinputvalue = 'dmhr%'
	#Set Filter button
	global wcsetfilter
	wcsetfilter = "//*[contains(@id, 'BiLabel') and contains(text(), 'Set Filter')]"
	#Select ' ' Synonym
	global wcselectsyn
	wcselectsyn = "//*[contains(text(), 'dmhr - ')]"
	#Join button
	global wcjoin
	wcjoin = "//*[contains(@id, 'BiLabel') and contains(text(), 'Join')]"
	#Insert Child button
	global wcinsertchild
	wcinsertchild = "//*[contains(@id, 'BiLabel') and contains(text(), 'Insert Child')]"
	#Baseapp folder selection
	global wcibisampsel
	wcibisampsel = ".//*[contains(text(), 'ibisamp')]"
	#DMCB synonym selection
	global wcselectdmterm
	wcselectdmterm = ".//*[contains(text(), 'dmterm')]"
	#Ok button
	global wcpressok
	wcpressok = ".//*[contains(@id, 'BiLabel') and contains(text(), 'OK')]"
	#Arrow from dmhr to dmqcb selection
	global wcjoinarrow
	wcjoinarrow = "(//*[@stroke-width='2'])[1]"
	#Edit Parent Link option selection
	global wceditparentlink
	wceditparentlink = "//*[contains(text(), 'Edit Parent Link')]"
	#Advanced button
	global wcadvancedbutton
	wcadvancedbutton = "//div[contains(@class, 'wc-dbl-obj-bottom-panel')]//div[contains(text(), 'Advanced')]"
	#Click on right outer join
	global wcsetrightouterjoin
	wcsetrightouterjoin = ".//*[contains(@id, '_right_b')]"
	#List selection From, Name
	global wcfromlistsel
	wcfromlistsel = "//div[contains(@id, 'row-0-col-1-object')]"
	#Test button
	global wctestbutton
	wctestbutton = "//img[contains(@src,'wc_test_join_16.png')]"
	#Select item in the combo box
	global wcpositiondescription
	wcpositiondescription = ".//*[contains(@id, 'BiComboBoxItem') and contains(text(), 'Salary')]"

#Create HTML page
def initcreatehtml():	
	global logfile
	global filename
	global getdir
	filename = os.path.basename(__file__[0:-3])
	logfile = os.path.join(getdir, filename +'_' + br + '.html')
	f = open(logfile, 'a')
	tags = """<htlm><head><title>""" + filename + """</title></head>"""
	f.write(tags)

#Create closing tags for html page
def initclosehtml():
	f = open(logfile, 'a')
	closetags = """</body></html>"""
	f.write(closetags)
	

#Creating output logging
def logfileibi():
	#Creating output file where test status will be passed
	#global bdrive
	global logfile
	global filename
	global logger
	filename = os.path.basename(__file__[0:-3])
	logfile = os.path.join(getdir, filename +'_' + br + '.html')
	#Setting logging options using logger as a utility 
	logger = logging.getLogger()
	#Setting logger level
	logger.setLevel(logging.DEBUG)
	#Setting file handler
	fh = logging.FileHandler(logfile)
	#Defining what format to use
	formatter = FormatterNotFormattingInfo()
	#Setting logging level for new handler
	fh.setLevel(logging.DEBUG)
	#Telling handler what format to use
	fh.setFormatter(formatter)
	#Intitiating handler
	logger.addHandler(fh)
	#First line in output
	logging.info("Test script: '"+ filename +"' output "+".")

#Function to take print screen and insirt into the output file
def printscreen(step):
	f = open(logfile, 'a')
	global driver
	savedir2 = os.path.join(getdir, filename + '_' + br +'_' + step + '_' + '.png')
	driver.save_screenshot(savedir2)
	imagedef = base64.b64encode(open(getdir + filename + '_' + br + '_' +  step + '_' + '.png', 'rb').read()).decode('utf-8').replace('\n', '')
	imgtag = '<img src="data:image/png;base64,%s">' % imagedef
	f.write('<b>')
	f.write(step)
	f.write('</b>')
	f.write(imgtag)
	f.close()
	
def RightClickSvgLine():
  global driver
  global bdrive
  bdrive = os.environ.get('BrSelect')
  if bdrive  == 'chrome':
  	actionChains = ActionChains(driver)
  	arrow = driver.find_element_by_xpath(wcjoinarrow)
  	actionChains.context_click(arrow).perform()
  elif bdrive  == 'IE' or 'firefox':
  	elem = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'svg01-line')))
  	x = 0
  	y = 0
  	x1 = elem.get_attribute("x1")
  	x2 = elem.get_attribute("x2")
  	x = ((float(x1)+float(x2))/2)+5
  	y1 = elem.get_attribute("y1")
  	y2 = elem.get_attribute("y2")
  	y = ((float(y1)+float(y2))/2)+5
  	ActionChains(driver).move_to_element_with_offset(elem, x, y).perform()
  	ActionChains(driver).context_click().perform()

#Removing dir defined in pyworkdir
def removdir():
	global getdir
	with contextlib.suppress(FileNotFoundError):
		shutil.rmtree(getdir)

#Creating dir defined in pyworkdir
def makedir():
	os.mkdir(getdir)	


def wctestcase1():
	#Open DMHR synonym, select Join, added a child, Edit Parent link, change parameters and test sample data.
	#Deleting output file before test starts. If file is not find supress errors
	try:
		logfileibi()
		global driver
		global logger
		#Defining what browser to use. Value passed from bset.getdriver that receives value set in env variable
		driver = bset.getdriver()
		#Calling defined server
		driver.get(http+server+sep+port)
		#Maximazing browser window
		driver.maximize_window()
		#Delete all cookies
		driver.delete_all_cookies()
		#Wating for page to load 
		driver.implicitly_wait(5)
		#Input UserID that is passed from user input
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wclogin)))
		driver.find_element_by_xpath(wclogin).send_keys(user)
		#Input Password that is passed from user input
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wcloginpass)))
		driver.find_element_by_xpath(wcloginpass).send_keys(password)
		printscreen('Login Page')
		#Press Sign In button and take a screenshot
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wcsingin)))
		driver.find_element_by_xpath(wcsingin).click()
		#Take a scren shot of main window
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wcfilterbutton)))
		driver.find_element_by_xpath(wcfilterbutton).click()
		#Select advanced option in Filter and take a scren shot
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wcadvancedselect)))
		printscreen("Click on the Filter")
		driver.find_element_by_xpath(wcadvancedselect).click()
		#input synonym value in File name and take a screen shot
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wcvaluetextfield)))
		printscreen("Filter Options") 
		driver.find_element_by_xpath(wcvaluetextfield).send_keys(wcinputvalue)
		#Click on set Filter button
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wcsetfilter)))
		driver.find_element_by_xpath(wcsetfilter).click()
		#Need add wait for the object
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wcselectsyn)))
		#Double click on Car synonym
		printscreen("Synonym Select")
		actionChains = ActionChains(driver)
		dmhrsel = driver.find_element_by_xpath(wcselectsyn)
		actionChains.double_click(dmhrsel).perform()
		#Click on add Join button and take a print screen
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wcjoin)))
		printscreen("Synonym Opened")
		driver.find_element_by_xpath(wcjoin).click()
		#Click insert child button and take a print screen
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wcinsertchild)))
		printscreen("Modeling View")
		driver.find_element_by_xpath(wcinsertchild).click()
		#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wcbaseappsel)))
		#Select baseapp foler and take a print screen
		#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, wcibisampsel)))
		printscreen("Folder Selected")
		#actionChains = ActionChains(driver)
		#driver.find_element_by_xpath(wcibisampsel).click()
		#openibisamp = driver.find_element_by_xpath(wcibisampsel)
		#ctionChains.double_click(openibisamp).perform()
		#Selecting DMQCB synonym and take a screen shot
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wcselectdmterm)))
		driver.find_element_by_xpath(wcselectdmterm).click()
		printscreen("Synonym to add is selected")
		#Pressing Ok button
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wcpressok)))
		driver.find_element_by_xpath(wcpressok).click()
		#Double click on arrow button
		#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, wcjoinarrow)))
		printscreen("Arrow")
		RightClickSvgLine()
		#Selecting Edit Parent Link
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, wceditparentlink)))
		printscreen("Edit Parent Link")
		driver.find_element_by_xpath(wceditparentlink).click()
		#Selectng Right Outer Join
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, wcsetrightouterjoin)))
		printscreen("Right Join")
		driver.find_element_by_xpath(wcsetrightouterjoin).click()
		#Selecting Advanced option
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, wcadvancedbutton)))
		printscreen("Advanced option")
		driver.find_element_by_xpath(wcadvancedbutton).click()
		#Selecting arrow down under from field
		WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, wcfromlistsel)))
		printscreen("List Select")
		driver.find_element_by_xpath(wcfromlistsel).click()
		#Showing that drop donw box is open
		#Selectiong Position, Description item in combo box
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, wcpositiondescription)))
		printscreen("Description")
		driver.find_element_by_xpath(wcpositiondescription).click()
		#Showing that drop donw box is open
		#Displaying Sample Data
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, wctestbutton)))
		printscreen("Pressing Sample Data")
		driver.find_element_by_xpath(wctestbutton).click()
		#Keeping browser open to see end the data
		time.sleep(5)
		printscreen("Sample Data")
		logger.info('Test Passed')	
		driver.quit()
		statusfile = os.path.join(getdir, filename +'_' + br + '_passed' '.txt')
		f = open(statusfile, 'w')
		f.close()	
	except:
		#If test if passed following message is displayed
		logger.info('Test Failed')	
		statusfile = os.path.join(getdir, filename +'_' + br + '_failed' '.txt')
		f = open(statusfile, 'w')
		f.close()
		driver.close()
		driver.quit()
		logger.exception('Error Message')
		raise SystemExit
#Defining xpath links as variables used in steps
getinfo()
#removdir()
#makedir()
initcreatehtml()
#Defining xpath links as variables used in steps
wcglobalitems()
#Executing defined steps
wctestcase1()
initclosehtml()
