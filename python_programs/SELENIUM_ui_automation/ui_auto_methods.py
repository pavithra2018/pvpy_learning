from selenium import webdriver
import time

def start_browser(url, browser = 'firefox') :
    if browser == 'firefox' :
        fdriver = webdriver.Firefox()
    else :
        print("unsupported browser %s"%browser)
        exit(1)
    fdriver.get(url)
    print("webpage is opened and title of that is:",fdriver.title)
    return(fdriver)
   
def goto_demohome(fdriver):
    fdriver.find_element_by_link_text('Demo Home').click()
    time.sleep(2)
    
def find_and_click_startpractising(fdriver) :
    fdriver.find_element_by_id('btn_basic_example').click()
    time.sleep(2)
    
def test1_simpleformdemo(fdriver, message) :
    fdriver.find_element_by_class_name('list-group-item').click()
    print(fdriver.title)
    fdriver.find_element_by_id('user-message').send_keys(message)
    fdriver.find_element_by_xpath("//button[text()='Show Message']").click()
    element = fdriver.find_element_by_xpath("//span[@id='display']")
    print("text entered is:", element.text)
    
def test2_simpleformdemo(fdriver, value1, value2):
    fdriver.find_element_by_id('sum1').send_keys(value1)
    fdriver.find_element_by_id('sum2').send_keys(value2)
    print(fdriver.title)
    fdriver.find_element_by_xpath("//button[text()='Get Total']").click()
    element = fdriver.find_element_by_xpath("//span[@id='displayvalue']")
    print("sum of two values is:", element.text)
    
def closebrowser(fdriver) :
    print("closing the browser")
    fdriver.close()
    
if __name__ == '__main__' :
    
    fdriver = start_browser('https://www.seleniumeasy.com/test/')
    find_and_click_startpractising(fdriver)
    test1_simpleformdemo(fdriver, 'hello world')
    test2_simpleformdemo(fdriver, 10, 20)
    print("returned to home page")
    goto_demohome(fdriver)
    closebrowser(fdriver)
