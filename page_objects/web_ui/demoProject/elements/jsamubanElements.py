#-*- coding:utf8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from page_objects.web_ui.locator_type import Locator_Type
from page_objects.createElement import CreateElement
from page_objects.web_ui.wait_type import Wait_Type as Wait_By
class jsamubanPageElements:
    def __init__(self):
        self.path = '/hses/tjsh#eyJtYyI6ImhzZSIsImZjIjoiSFNFX0pTQV9URU1QTEVURV9ORVciLCJ1YyI6IjAxMzA0MTAwIn0='
        self.title = CreateElement.create(None, None, None, Wait_By.TITLE_IS)
        self.tianjia_button = CreateElement.create(Locator_Type.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div/div[3]/div/div[2]/div[2]/div/ul/li[1]/a',wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.chakan_button = CreateElement.create(Locator_Type.XPATH,
                                            '/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div/div[3]/div/div[2]/div[2]/div/ul/li[3]/a',
                                            wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.xiugai_button = CreateElement.create(Locator_Type.XPATH,
                                           '/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div/div[3]/div/div[2]/div[2]/div/ul/li[2]/a',
                                           wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.fuxuankuang = CreateElement.create(Locator_Type.XPATH,
                                           '/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div/div[3]/div/div[2]/div[3]/div[1]/div/div[4]/table/tbody/tr[1]/td[1]/span',
                                           wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.suoshubumen = CreateElement.create(Locator_Type.XPATH,
                                                '/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div/div[1]/div/table/tbody/tr/td[2]/span[2]/div/i',
                                                wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.mubanmingcheng = CreateElement.create(Locator_Type.XPATH,
                                                '/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/span[2]/div/div',
                                                wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.chaxun_button = CreateElement.create(Locator_Type.XPATH,
                                                 '/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/ul/li[1]/a',
                                                 wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)