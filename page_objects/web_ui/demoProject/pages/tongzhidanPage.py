#-*- coding:utf-8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from page_objects.web_ui.demoProject.elements.tongzhidanElements import tongzhidanPageElements
class TongzhidanPage:
    def __init__(self,browserOperator):
        self._browserOperator=browserOperator
        self._tongzhidanPageElements=tongzhidanPageElements()
        #self._tongzhidanPageElements.title.wait_expected_value=title
        #self._browserOperator.explicit_wait_page_title(self._tongzhidanPageElements.title)
        #self._browserOperator.explicit_wait_page_title(self._indexPageElements.title)
        self._browserOperator.get_screenshot('tongzhidanPage')

    def _pick_fuxuankuang(self):
        self._browserOperator.click(self._tongzhidanPageElements.fuxuankuang)
        self._browserOperator.get_screenshot('pick_fuxuankuang')

    def _click_chakan_button(self):
        self._browserOperator.click(self._tongzhidanPageElements.chankan_button)
        self._browserOperator.get_screenshot('click_chakan_button')

    def _input_tongzhidanmiaoshu(self,tongzhidanmiaoshu):
        self._browserOperator.sendText(self._tongzhidanPageElements.tongzhidanmiaoshu,tongzhidanmiaoshu)
        self._browserOperator.get_screenshot('input_tongzhidanmiaoshu')

    def _click_chaxun_button(self):
        self._browserOperator.click(self._tongzhidanPageElements.chaxun_button)
        self._browserOperator.get_screenshot('click_chaxun_button')

    def chakantongzhidan(self):
        self._pick_fuxuankuang()
        self._click_chakan_button()

    def chaxuntongzhidan(self,tongzhidanmiaoshu):
        self._input_tongzhidanmiaoshu(tongzhidanmiaoshu)
        self._click_chaxun_button()


    def getElements(self):
        return self._tongzhidanPageElements