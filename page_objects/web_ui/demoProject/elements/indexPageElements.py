#-*- coding:utf8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from page_objects.createElement import CreateElement
from page_objects.web_ui.wait_type import Wait_Type as Wait_By
from page_objects.web_ui.locator_type import Locator_Type
class IndexPageElements:
    def __init__(self):
        self.path = '/passports/login?service=https%3A%2F%2Ftjsh.ushayden.com%2Fportals%2Fcas&tenantCode=tjsh&trial=false'
        self.title = CreateElement.create(None,None,None,Wait_By.TITLE_IS,'现场总管-欢迎登录')
        self.username_input = CreateElement.create(Locator_Type.ID,'name',wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.password_input = CreateElement.create(Locator_Type.ID, 'pwd1', wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.denglu_button =  CreateElement.create(Locator_Type.XPATH,'/html/body/form/div[2]/a',wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)

