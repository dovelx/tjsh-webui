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

class TestSgzyp():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(10)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sgzyp(self):
    # Test name: sgzyp
    # Step # | name | target | value
    # 1 | open | /passports/login?service=https%3A%2F%2Ftjsh.ushayden.com%2Fportals%2Fcas&tenantCode=tjsh&trial=false | 
    self.driver.get("https://tjsh.ushayden.com/passports/login?service=https%3A%2F%2Ftjsh.ushayden.com%2Fportals%2Fcas&tenantCode=tjsh&trial=false")
    # 2 | setWindowSize | 1550x840 | 
    #self.driver.set_window_size(1550, 840)
    # 3 | click | id=name | 
    self.driver.find_element(By.ID, "name").click()
    # 4 | type | id=name | zhai
    self.driver.find_element(By.ID, "name").send_keys("zhai")
    # 5 | type | id=pwd1 | 123456
    self.driver.find_element(By.ID, "pwd1").send_keys("123456")
    # 6 | click | linkText=登录 | 
    #self.driver.find_element(By.LINK_TEXT, "登录").click()
    self.driver.find_element(By.XPATH, '/html/body/form/div[2]/a').click()
    time.sleep(10)
    # 7 | mouseOver | linkText=0 | 
    element = self.driver.find_element(By.LINK_TEXT, "0")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 8 | click | css=.sl-navitem:nth-child(1) .title | -点击作业许可
    self.driver.find_element(By.CSS_SELECTOR, ".sl-navitem:nth-child(1) .title").click()
    #time.sleep(3)
    # 9 | click | css=.children .sl-navitem:nth-child(3) .title | -点击施工作业票
    self.driver.find_element(By.CSS_SELECTOR, ".children .sl-navitem:nth-child(3) .title").click()
    #time.sleep(5)
    # 10 | click | linkText=添加 | 
    self.driver.find_element(By.LINK_TEXT, "添加").click()
    time.sleep(3)
    # 11 | click | css=tr:nth-child(2) li:nth-child(2) | -选择项目类型
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) li:nth-child(2)").click()
    # 12 | click | css=tr:nth-child(2) > .searchfunc div > div | 选择通知单编码

    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .searchfunc div > div").click()
    time.sleep(3)
    # 13 | click | css=.selected > .label:nth-child(4) div | 选择通知单数据
    self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/div[3]/div[1]/div/div[4]/table/tbody/tr[1]/td[2]/span/div").click()
    # 14 | click | linkText=确定 | 
    self.driver.find_element(By.LINK_TEXT, "确定").click()
    # 15 | click | css=tr:nth-child(3) > .textinput div > div | 点击作业名称输入框
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > .textinput div > div").click()
    # 16 | type | css=.fixed input | test-name 输入作业名称
    self.driver.find_element(By.CSS_SELECTOR, ".fixed input").send_keys("test-name")
    # 17 | click | css=.exists:nth-child(3) li:nth-child(1) | 选择作业票级别
    self.driver.find_element(By.CSS_SELECTOR, ".exists:nth-child(3) li:nth-child(1)").click()
    # 18 | click | css=tr:nth-child(4) > .textinput div > div | 点击设备位号输入框
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > .textinput div > div").click()
    # 19 | type | css=.fixed input | test-weihao 输入位号数据
    self.driver.find_element(By.CSS_SELECTOR, ".fixed input").send_keys("test-weihao")
    # 20 | click | css=tr:nth-child(5) li:nth-child(2) | 是否承包商-选否
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) li:nth-child(2)").click()
    # # 21 | click | css=tr:nth-child(5) > .searchfunc div > div | 进入选择作业单位界面
    # self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) > .searchfunc div > div").click()
    # # 22 | click | css=.selected > .label:nth-child(2) div | 选择作业单位
    # self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/div[3]/div[1]/div/div[4]/table/tbody/tr[1]/td[2]").click()
    # # 23 | click | linkText=确定 | 确认作业单位数据输入
    # self.driver.find_element(By.LINK_TEXT, "确定").click()
    # 24 | click | css=tr:nth-child(6) > .textinput div > div | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > .textinput div > div").click()
    # 25 | type | css=.fixed input | test-didian 输入作业地点
    self.driver.find_element(By.CSS_SELECTOR, ".fixed input").send_keys("test-didian")
    # 26 | click | css=tr:nth-child(7) > .textinput:nth-child(2) div > div | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > .textinput:nth-child(2) div > div").click()
    # 27 | type | css=.fixed input | jiezhi1 输入介质
    self.driver.find_element(By.CSS_SELECTOR, ".fixed input").send_keys("jiezhi1")
    # 28 | click | css=tr:nth-child(7) > .textinput:nth-child(3) div > div | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > .textinput:nth-child(3) div > div").click()
    # 29 | type | css=.fixed input | 12 输入操作温度
    self.driver.find_element(By.CSS_SELECTOR, ".fixed input").send_keys("12")
    # 30 | click | css=tr:nth-child(8) div > div | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) div > div").click()
    # 31 | type | css=.fixed input | 1024 输入压力值
    self.driver.find_element(By.CSS_SELECTOR, ".fixed input").send_keys("1024")
    # 32 | click | css=.textarea div > div | 
    self.driver.find_element(By.CSS_SELECTOR, ".textarea div > div").click()
    # 33 | type | css=textarea | sgnr-content 输入施工内容
    self.driver.find_element(By.CSS_SELECTOR, "textarea").send_keys("sgnr-content")
    # 34 | click | css=tr:nth-child(12) > .dateinput:nth-child(2) div > div | 选择计划开始时间
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(12) > .dateinput:nth-child(2) div > div").click()
    # 35 | click | css=tr:nth-child(6) > td:nth-child(2) > .date |
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(2) > .date").click()
    # 36 | click | css=.hour input | 
    self.driver.find_element(By.CSS_SELECTOR, ".hour input").click()
    # 37 | type | css=.hour input | 11  修改计划开始时间
    self.driver.find_element(By.CSS_SELECTOR, ".hour input").send_keys("11")
    # 38 | click | linkText=确定 | 
    self.driver.find_element(By.LINK_TEXT, "确定").click()
    # 39 | click | css=tr:nth-child(12) > .dateinput:nth-child(3) div > div | 选择计划结束时间
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(12) > .dateinput:nth-child(3) div > div").click()
    # 40 | click | xpath=//div[2]/table/tbody/tr[6]/td[2]/span | 
    self.driver.find_element(By.XPATH, "//div[2]/table/tbody/tr[6]/td[2]/span").click()
    # 41 | click | css=.hour input | 
    self.driver.find_element(By.CSS_SELECTOR, ".hour input").click()
    # 42 | type | css=.hour input | 16 修改结束时间
    self.driver.find_element(By.CSS_SELECTOR, ".hour input").send_keys("16")
    # 43 | click | linkText=确定 | 
    self.driver.find_element(By.LINK_TEXT, "确定").click()
    # 44 | click | css=tr:nth-child(13) div > div | 选择作业类型
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(13) div > div").click()
  
if __name__ == '__main__':
    pytest.main(['-v','--html=report04.html','test_shigongzuoyepiao_2.py'])