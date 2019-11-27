from selenium import webdriver
import time
class ui_auto() :
    def __init__(self, url, browser = 'firefox') :
        self.url = url
        self.browser = browser
        self.driver = None
        
    def start_browser(self) :
        if self.browser == 'firefox' :
            self.driver = webdriver.Firefox()
            time.sleep(2)
        else :
            print("error: unsupported browser %s"%self.browser)
            exit(1)
        print("browser started")
        
    def close_browser(self):
        print("closing the browser")
        self.driver.close()
        
    def goto_demohome(self) :
        self.driver.get(self.url)
        print(self.driver.title)
        self.driver.find_element_by_link_text('Demo Home').click()
        time.sleep(2)
        print("came back to demohome page")
        
    def find_and_click_startpractising(self) :
        self.driver.find_element_by_id('btn_basic_example').click()
        print("clicked on startpractising")
        
    def test1_simpleformdemo(self, message) :
        self.driver.find_element_by_class_name('list-group-item').click()
        print(self.driver.title)
        self.driver.find_element_by_id('user-message').send_keys(message)
        self.driver.find_element_by_xpath("//button[text()='Show Message']").click()
        element = self.driver.find_element_by_xpath("//span[@id='display']")
        print("text entered is:", element.text)
        
    def test2_simpleformdemo(self, value1, value2):
        self.driver.find_element_by_id('sum1').send_keys(value1)
        self.driver.find_element_by_id('sum2').send_keys(value2)
        print(self.driver.title)
        self.driver.find_element_by_xpath("//button[text()='Get Total']").click()
        element = self.driver.find_element_by_xpath("//span[@id='displayvalue']")
        print("sum of two values is:", element.text)
        
    
        

if __name__ == '__main__' :
    
    ui_auto_obj = ui_auto('https://www.seleniumeasy.com/test/', 'firefox')
    ui_auto_obj.start_browser()
    ui_auto_obj.goto_demohome()
    ui_auto_obj.find_and_click_startpractising() 
    ui_auto_obj.test1_simpleformdemo('hello world!')
    ui_auto_obj.test2_simpleformdemo(10, 20)
    ui_auto_obj.goto_demohome()
    ui_auto_obj.close_browser()
    
    
        