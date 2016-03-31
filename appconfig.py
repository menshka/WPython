# ---------------------------------------------------------------------
# Copyright (c) Information Builders, Inc.  All rights reserved.
#
# _Name_        ===> appconfig.py
# _Description_ ===>
#
# _History_:
#  Date  Time Who Proj       Project Title
# ====== ==== === ====== ==============================================
# 160323 1638 anm 175587 Testing Selenium tool with python
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
#Import time for wait option
import time
#Inmport sys for SysExit
import sys
#Import webdriver 
#Import lib to use browser commons keys, return, up, down etc...
from selenium.webdriver.common.keys import Keys
#Import expected conditions to check existence of items on the pages
from selenium.webdriver.support import expected_conditions as EC
#Import wait option
from selenium.webdriver.support.ui import WebDriverWait
#Import option to chain actions
from selenium.webdriver.common.action_chains import ActionChains
#Import lib to use by
from selenium.webdriver.common.by import By
#OS Module
import os
#Import Selenium webdriver
from selenium import webdriver
#Import Derired Cap for IE 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#Get global var for browser selection
global bdrive
bdrive = os.environ.get('BrSelect')
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
global driver
if bdrive == 'chrome':
	driver = webdriver.Chrome()
	driver.get(http+server+sep+port)
	driver.maximize_window()
	driver.delete_all_cookies()
elif bdrive == 'firefox':
	driver = webdriver.Firefox()
	driver.get(http+server+sep+port)
	driver.maximize_window()
	driver.delete_all_cookies()
elif bdrive == 'ie':
	os.system('RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 2')
	caps = DesiredCapabilities.INTERNETEXPLORER
	caps['ignoreProtectedModeSettings'] = True
	driver = webdriver.Ie('iedriverserver.exe', caps)
	driver.get(http+server+sep+port)
	driver.maximize_window()

# =============================================================================
# Closing Webdriver                            
# =============================================================================	
def closedriver():
	global driver
	driver.close()
	driver.quit()
# =============================================================================