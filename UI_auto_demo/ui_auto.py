"""
    UI Automation
"""
from selenium import webdriver
import time
# open the firefox browser
fdriver = webdriver.Firefox()
fdriver.get('https://www.seleniumeasy.com/test/')
print(fdriver.title)

# click on startpractising
fdriver.find_element_by_id('btn_basic_example').click()
# click on simpleformdemo
fdriver.find_element_by_class_name('list-group-item').click()
print(fdriver.title)
# enter text in the text field
fdriver.find_element_by_id('user-message').send_keys('hello world!')
# click on show message
fdriver.find_element_by_xpath("//button[text()='Show Message']").click()
# collect the text in a variable element and print it
element = fdriver.find_element_by_xpath("//span[@id='display']")
print("text entered is:", element.text)
#time.sleep(5)
# handling two inputs
fdriver.find_element_by_id('sum1').send_keys(10)
fdriver.find_element_by_id('sum2').send_keys(20)
fdriver.find_element_by_xpath("//button[text()='Get Total']").click()
element = fdriver.find_element_by_xpath("//span[@id='displayvalue']")
print("sum of two values is:", element.text)

#going back to home page
fdriver.find_element_by_link_text('Demo Home').click()
time.sleep(2)
# Start Practising
fdriver.find_element_by_id('btn_basic_example').click()
time.sleep(2)
# click on checkboxdemo
fdriver.find_element_by_link_text('Check Box Demo').click()
time.sleep(2)
# click on checkbox
fdriver.find_element_by_id('isAgeSelected').click()
time.sleep(2)
# click on check all option so you can see the option changing to uncheckall
fdriver.find_element_by_id('check1').click()
print("clicked on check all")
time.sleep(2)
# uncheck any one of the option
fdriver.find_element_by_xpath("//label[text()='Option 1']").click()
print("option 1 is unchecked")
time.sleep(2)
# again click on checkall
#fdriver.find_element_by_id('check1').click()
#print("clicked on check all")
#time.sleep(2)

#going back to home page
fdriver.find_element_by_link_text('Demo Home').click()
time.sleep(2)
# Start Practising
fdriver.find_element_by_id('btn_basic_example').click()
time.sleep(2)
# click on radio button demo
fdriver.find_element_by_link_text('Radio Buttons Demo').click()
time.sleep(2)
#
fdriver.find_element_by_xpath("//label[value()='Female']").click()
time.sleep(2)
#
fdriver.find_element_by_id('buttoncheck').click()
element1 = fdriver.find_element_by_class_name('radiobutton')
print("the text displayed is:", element1.text())

fdriver.close()




