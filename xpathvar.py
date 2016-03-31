# =============================================================================
# Defining global variables                              
# =============================================================================
#Login field
global close
close = "')]"
global wclogin
wclogin = "//*[contains(@id, 'BiTextField')]"
#Password field
global wcloginpass
wcloginpass = "//*[contains(@id, 'BiPasswordField')]"
#Filter button
global regbutton
regbutton = "//*[contains(@id, 'BiLabel') and contains(text(), '"
#Advanced filter option
global textsel
textsel = "//*[contains(text(), '"
#File Name input field
global textinput
textinput = "//div[contains(text(), '"
global textinputsib
textinputsib = "')]/following-sibling::div[1]/input"
global textinputsib2
textinputsib2 = "')]/following-sibling::input[1]"
#Input value in File Name field
#Advanced button
global rightpanelcont
rightpanelcont = "//div[contains(@class, 'wc-dbl-obj-right-panel')]"
global bottompanelcont
bottompanelcont = "//div[contains(@class, 'wc-dbl-obj-bottom-panel')]"
#Click on right outer join
global idsel
idsel = ".//*[contains(@id, '"
#List selection From, Name
global wcfromlistsel
wcfromlistsel = "//div[contains(@id, 'row-0-col-1-object')]"
#Test button
global wcimagesel
wcimagesel = "//img[contains(@src,'"
#Select item in the combo box
global wclisteitem
wclisteitem = ".//*[contains(@id, 'BiComboBoxItem') and contains(text(), '"
global specialsel
specialsel = "//*[contains(@class, 'text') and contains(text(), '"
global newinput
newinput = ".//*[contains(@id, 'BiTextArea') and contains(@class, 'bi-text-field text-field')]"
global closebutton
closebutton = "//div[contains(@id, 'Validate Expression') and contains(@class, 'bi-button window-close-button')]"

def xpathset(passx):
	if passx == rbutton:
		return regbutton