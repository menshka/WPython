# ---------------------------------------------------------------------
# Copyright (c) Information Builders, Inc.  All rights reserved.
#
# _Name_        ===> actions.py
# _Description_ ===>
#
# _History_:
#  Date  Time Who Proj       Project Title
# ====== ==== === ====== ==============================================
# 160321 1651 anm 175587 Testing Selenium tool with python
# 160321 1650 anm 175587 Testing Selenium tool with python
#
# END %&$
# ---------------------------------------------------------------------
from selenium import webdriver
#Import lib to use browswer commons keys, return, up, down etc...
from selenium.webdriver.common.keys import Keys
#Import expected conditions to check existence of items on the pages
from selenium.webdriver.support import expected_conditions as EC
#Import wait option
from selenium.webdriver.support.ui import WebDriverWait
#Import option to chain actions
from selenium.webdriver.common.action_chains import ActionChains
#Using by sytnaxe
from selenium.webdriver.common.by import By
#Importing OS lib
import os
#Importing all var from appconfig
from appconfig import *
import appconfig
#from gvar import *
import xpathvar
import logging
#Importing appconfig to use closedriver function
#import appconfig
import tstlog
global passt
global closev
closev = xpathvar.close
global inputsib
inputsib = xpathvar.textinputsib
global inputsib2
inputsib2 = xpathvar.textinputsib2
bottompanel = xpathvar.bottompanelcont
global closebutton
closebutton = xpathvar.closebutton
# =============================================================================
# Right click on arrow in Modeling View                      
# =============================================================================
def RightClickSvgLine(text, x):
	global driver
	global bdrive
	bdrive = os.environ.get('BrSelect')
	if bdrive  == 'chrome':
		actionChains = ActionChains(driver)
		arrow = driver.find_element_by_xpath(wcjoinarrow)
		actionChains.context_click(arrow).perform()
	elif bdrive  == 'IE' or 'firefox':
		elem = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, text)))
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
	if x == 'y':
		tstlog.printscreen(text)
	else:	
		tstlog.noprintscreen(text) 	
# =============================================================================

# =============================================================================
# Single Click                     
# =============================================================================
def singleclick(container, xpathvar, xpath, text, ptext, x):
	global closev
	global driver
	global link
	global passt
	xpathl = xpathvar.xpathset(xpath)
	passt = ptext
	if container == "":
		link = xpathl + xpathvar + closev
	elif container != "":
		link = container + xpath + xpathvar + closev
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link)))
	driver.find_element_by_xpath(link).click()
	if ptext != "":
		texttobepresent()
	elif ptext == "":
		pass
	if x == 'y':
		tstlog.printscreen(text)
	else:	
		tstlog.noprintscreen(text) 
# =============================================================================

# =============================================================================
# Single Login
# =============================================================================
def serverlogin(username, password, text, x):
	global driver
	luser = "//div[contains(text(), 'User ID')]/following-sibling::input[1]"
	lpass = "//div[contains(text(), 'Password')]/following-sibling::input[1]"
	usern = username
	passw = password
	if username == "":
		usern = os.environ.get('wcusername')	
	else: 	
		logging.error("Incorrect User ID")
	if password == "":
		passw = os.environ.get('wcuserpassword')	
	else: 	
		logging.error("Incorrect Password")	
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, luser)))
	driver.find_element_by_xpath(luser).send_keys(usern)
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, lpass)))
	driver.find_element_by_xpath(lpass).send_keys(passw)
	if x == 'y':
		tstlog.printscreen(text)
	else:	
		tstlog.noprintscreen(text) 
# =============================================================================

# =============================================================================
# Text Input
# =============================================================================
def textinput(xpathvar, xpath, inputvalue, text, x):
	global driver
	global inputsib
	link = xpath + xpathvar + inputsib
	#f = open('test22.txt', 'a')
	#f.write(link)
	#f.close()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link)))
	driver.find_element_by_xpath(link).send_keys(inputvalue)
	if x == 'y':
		tstlog.printscreen(text)
	else:	
		tstlog.noprintscreen(text) 
# =============================================================================

# =============================================================================
# Double Click
# =============================================================================
def doubleclick(xpathvar, xpath, text, ptext, x):
	global closev
	global driver
	link = xpath + xpathvar + closev
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link)))
	actionChains = ActionChains(driver)
	objsel = driver.find_element_by_xpath(link)
	actionChains.double_click(objsel).perform()
	if ptext != "":
		texttobepresent()
	elif ptext == "":
		pass
	if x == 'y':
		tstlog.printscreen(text)
	else:	
		tstlog.noprintscreen(text) 
# =============================================================================	

# =============================================================================
# Text to be present
# =============================================================================
def texttobepresent():
	global driver
	global passt
	text = passt
	link = "//*[contains(text(),'" + text + "')]"
	WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, link), text ))
# =============================================================================

# =============================================================================
def textinput2(xpathvar, xpath, inputvalue, text, x):
	global driver
	global inputsib2
	link = xpath + xpathvar + inputsib2
	#f = open('test22.txt', 'a')
	#f.write(link)
	#f.close()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link)))
	driver.find_element_by_xpath(link).send_keys(inputvalue)
	if x == 'y':
		tstlog.printscreen(text)
	else:	
		tstlog.noprintscreen(text) 
# =============================================================================

# =============================================================================
def textinput3(xpath, inputvalue, text, x):
	global driver
	link = xpath
	#f = open('test22.txt', 'a')
	#f.write(link)
	#f.close()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link)))
	driver.find_element_by_xpath(link).send_keys(inputvalue)
	if x == 'y':
		tstlog.printscreen(text)
	else:	
		tstlog.noprintscreen(text) 
# =============================================================================

# =============================================================================
def close():
	global closebutton
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, closebutton)))
	driver.find_element_by_xpath(closebutton).click()
# =============================================================================