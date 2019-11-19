from selenium import webdriver
import time

fdriver = webdriver.Firefox()
fdriver.get('https://www.seleniumeasy.com/test/')
print(fdriver.title)
fdriver.find_element_by_id('btn_basic_example').click()
fdriver.find_element_by_class_name('list-group-item').click()
print(fdriver.title)
fdriver.find_element_by_id('user-message').send_keys('hello world!')
fdriver.find_element_by_xpath("//button[text()='Show Message']").click()
element = fdriver.find_element_by_xpath("//span[@id='display']")
print("text entered is:", element.text)
#time.sleep(5)
#handling two inputs
fdriver.find_element_by_id('sum1').send_keys(10)
fdriver.find_element_by_id('sum2').send_keys(20)
fdriver.find_element_by_xpath("//button[text()='Get Total']").click()
element = fdriver.find_element_by_xpath("//span[@id='displayvalue']")
print("sum of two values is:", element.text)
time.sleep(5)
fdriver.close()



