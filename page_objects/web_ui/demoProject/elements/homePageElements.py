#-*- coding:utf8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from page_objects.web_ui.locator_type import Locator_Type
from page_objects.createElement import CreateElement
from page_objects.web_ui.wait_type import Wait_Type as Wait_By
class homePageElements:
    def __init__(self):
        self.path = '/portals/tjsh'
        self.title = CreateElement.create(None, None, None, Wait_By.TITLE_IS, '天津石化公司')
        self.check_yuyue = CreateElement.create(Locator_Type.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div[1]',wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)

