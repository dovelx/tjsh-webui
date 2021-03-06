# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTongzhidian11():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(30)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tongzhidian11(self):
    # Test name: tongzhidian-11
    # Step # | name | target | value
    # 1 | open | /passports/login?service=https%3A%2F%2Ftjsh.ushayden.com%2Fportals%2Fcas&tenantCode=tjsh&trial=false | 
    self.driver.get("https://tjsh.ushayden.com/passports/login?service=https%3A%2F%2Ftjsh.ushayden.com%2Fportals%2Fcas&tenantCode=tjsh&trial=false")
    # 2 | setWindowSize | 550x697 | 
    #self.driver.set_window_size(550, 697)
    # 3 | type | id=name | liyh490
    self.driver.find_element(By.ID, "name").send_keys("zhai")
    # 4 | type | id=pwd1 | 137156449503bb614f22a6f56b3254522f208df670cb88d83d2347c0f20be3a2a241ae7e94db2ab4e23d1e76f1779d62f4fa2f915e4de006d7ecdaa36338dc767e64096500de235da80702d9e83cde8b23359e544b770c4d162d6538824722b8c4e277d41fef03b5d53184389cdce57bf21b00ba0a8d035a8222d8139c8fb915
    #self.driver.find_element(By.ID, "pwd1").send_keys("137156449503bb614f22a6f56b3254522f208df670cb88d83d2347c0f20be3a2a241ae7e94db2ab4e23d1e76f1779d62f4fa2f915e4de006d7ecdaa36338dc767e64096500de235da80702d9e83cde8b23359e544b770c4d162d6538824722b8c4e277d41fef03b5d53184389cdce57bf21b00ba0a8d035a8222d8139c8fb915")
    # 5 | click | id=name | 
    self.driver.find_element(By.ID, "name").click()
    # 6 | click | id=pwd1 | 
    self.driver.find_element(By.ID, "pwd1").click()
    # 7 | type | id=pwd1 | 123456
    self.driver.find_element(By.ID, "pwd1").send_keys("123456")
    # 8 | click | linkText=?????? | 
    #self.driver.find_element(By.LINK_TEXT, "??????").click()
    self.driver.find_element(By.XPATH, '/html/body/form/div[2]/a').click()


    time.sleep(10)
    # 14 | click | css=.sl-navitem:nth-child(1) .title | 
    self.driver.find_element(By.CSS_SELECTOR, ".sl-navitem:nth-child(1) .title").click()
    # 15 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    time.sleep(3)
    # 16 | click | css=.children .sl-navitem:nth-child(1) .title | 
    self.driver.find_element(By.CSS_SELECTOR, ".children .sl-navitem:nth-child(1) .title").click()
    time.sleep(3)
    # 17 | runScript | window.scrollTo(0,0) | 

    # 18 | click | css=.selected > .check > .value | 
    self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[4]/div/div/div[3]/div/div[2]/div[3]/div[1]/div/div[4]/table/tbody/tr[1]/td[1]/span").click()
    time.sleep(3)

    # 20 | click | linkText=?????? | 
    self.driver.find_element(By.LINK_TEXT, "??????").click()
    # 21 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    time.sleep(3)
    # 22 | click | linkText=?????? | 
    self.driver.find_element(By.LINK_TEXT, "??????").click()
    # 23 | click | css=.textinput:nth-child(5) div > div | 
    self.driver.find_element(By.CSS_SELECTOR, ".textinput:nth-child(5) div > div").click()
    # 24 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 25 | type | css=.fixed input | ???
    self.driver.find_element(By.CSS_SELECTOR, ".fixed input").send_keys("???")
    # 26 | click | linkText=?????? | 
    self.driver.find_element(By.LINK_TEXT, "??????").click()
    time.sleep(10)

    # 27 | click | css=.user-name | ????????????
    self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]").click()
    # 28 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    time.sleep(10)
    # 29 | click | css=.sl-menubox | 
    self.driver.find_element(By.CSS_SELECTOR, ".sl-menubox").click()
    # 30 | click | css=.user-name | 
    self.driver.find_element(By.CSS_SELECTOR, ".user-name").click()
    # 31 | click | css=.icon-headermenu-logout | 
    self.driver.find_element(By.CSS_SELECTOR, ".icon-headermenu-logout").click()

if __name__ == '__main__':
    pytest.main(['-v','--html=report02.html','test_tongzhidan_1.py'])
  
